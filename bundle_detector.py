import openai
from typing import List, Dict
from urllib.parse import urlparse, quote
import requests
import json
import time
import os
import re

class BundleDetector:
    """Simple bundle detector using Jina reader and GPT"""
    
    def __init__(self, api_key: str, base_url: str, max_urls: int = 100, output_dir: str = None):
        self.api_key = api_key
        self.base_url = base_url
        self.max_urls = max_urls
        
        # Setup directories
        domain = urlparse(base_url).netloc.replace('.', '_')
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        self.run_id = f"{domain}_{timestamp}"
        
        self.output_dir = output_dir or "output"
        self.run_dir = os.path.join(self.output_dir, self.run_id)
        self.raw_dir = os.path.join(self.run_dir, "raw_data")
        self.gpt_dir = os.path.join(self.run_dir, "gpt_data")
        self.bundles_dir = os.path.join(self.run_dir, "bundles")
        self.articles_dir = os.path.join(self.run_dir, "articles")
        
        for dir_path in [self.raw_dir, self.gpt_dir, self.bundles_dir, self.articles_dir]:
            os.makedirs(dir_path, exist_ok=True)

    def _fetch_with_jina(self, url: str) -> str:
        """Fetch content using Jina's reader"""
        encoded_url = quote(url, safe='')
        reader_url = f"https://r.jina.ai/{encoded_url}"
        
        headers = {
            "Accept": "text/markdown",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "x-timeout": "45"
        }
        
        try:
            print(f"Fetching with Jina: {url}")
            response = requests.get(reader_url, headers=headers, timeout=45)
            
            if response.status_code != 200:
                print(f"Error fetching {url}: {response.status_code}")
                return None
                
            return response.text
            
        except Exception as e:
            print(f"Error fetching {url}: {str(e)}")
            return None

    def detect_bundles(self) -> Dict[str, List[str]]:
        """Main method to detect and create URL bundles"""
        print("Starting bundle detection...")
        
        # 1. Fetch content with Jina
        content = self._fetch_with_jina(self.base_url)
        if not content:
            print("Failed to fetch content")
            return None
            
        # 2. Save raw content
        raw_content_file = os.path.join(self.raw_dir, "raw_content.md")
        with open(raw_content_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Raw content saved to: {raw_content_file}")
        
        # 3. Extract ALL links and their context
        links = re.findall(r'\[([^\]]+)\]\((https://[^)]+)\)', content)
        all_links = [
            {
                'title': title.strip(),
                'url': url,
                'context': self._extract_context(content, title)  # Get surrounding text
            }
            for title, url in links
        ]
        
        # Save all extracted links
        extracted_file = os.path.join(self.raw_dir, "all_links.json")
        with open(extracted_file, 'w', encoding='utf-8') as f:
            json.dump(all_links, f, indent=2)
        print(f"All links saved to: {extracted_file}")
        
        # 4. Let GPT analyze everything
        try:
            client = openai.OpenAI()
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "system", 
                        "content": f"""Analyze these links from a Medium tag page and:
                        1. Identify up to {self.max_urls} most relevant technical articles
                        2. Create 2-4 thematic bundles based on content relationships
                        3. Explain your selection and grouping logic
                        
                        Return as JSON:
                        {{
                            "bundles": {{
                                "bundle_name": {{
                                    "urls": ["url1", "url2"],
                                    "topic": "Topic description",
                                    "reason": "Why these articles belong together",
                                    "articles": ["Article 1 title", "Article 2 title"]
                                }}
                            }},
                            "selection_logic": "Explain how you chose these articles",
                            "grouping_logic": "Explain how you created the bundles"
                        }}"""
                    },
                    {
                        "role": "user",
                        "content": f"Here are all the links from the page:\n\n{json.dumps(all_links, indent=2)}"
                    }
                ],
                temperature=0.3,
                max_tokens=2000
            )
            
            # 1. First save raw response
            raw_response = response.choices[0].message.content
            raw_response_file = os.path.join(self.gpt_dir, "raw_gpt_response.txt")
            with open(raw_response_file, 'w', encoding='utf-8') as f:
                f.write(raw_response)
            print(f"Raw GPT response saved to: {raw_response_file}")
            
            # 2. Try to clean the response
            cleaned_response = raw_response.strip()
            # Remove any BOM or hidden characters
            cleaned_response = cleaned_response.encode('utf-8', errors='ignore').decode('utf-8')
            
            # 3. Try to parse JSON
            try:
                rich_analysis = json.loads(cleaned_response)
                print("Successfully parsed GPT response")
            except json.JSONDecodeError as e:
                print(f"Failed to parse GPT response: {str(e)}")
                print("Raw response:")
                print(cleaned_response)
                return None
            
            # 4. Save rich analysis
            gpt_output_file = os.path.join(self.gpt_dir, "gpt_analysis.json")
            with open(gpt_output_file, 'w', encoding='utf-8') as f:
                json.dump({
                    'input_links': all_links,
                    'gpt_analysis': rich_analysis
                }, f, indent=2)
            
            # Convert to simple format for scrape_all.py
            simple_bundles = {}
            for name, data in rich_analysis['bundles'].items():
                # Convert spaces to underscores and lowercase for bundle names
                bundle_name = name.lower().replace(' ', '_')
                simple_bundles[bundle_name] = data['urls']
            
            # Save simple format
            bundles_file = os.path.join(self.bundles_dir, "detected_bundles.json")
            with open(bundles_file, 'w', encoding='utf-8') as f:
                json.dump(simple_bundles, f, indent=2)
            
            return simple_bundles  # Return simple format for scrape_all.py
            
        except Exception as e:
            print(f"Error in GPT processing: {str(e)}")
            print("Full error:")
            import traceback
            traceback.print_exc()
            return None
        except Exception as e:
            print(f"\nGPT API Error: {str(e)}")
            print("Full error:")
            import traceback
            traceback.print_exc()
            return None

    def _extract_context(self, content: str, title: str, chars=200) -> str:
        """Extract text around a title for context"""
        try:
            idx = content.index(title)
            start = max(0, idx - chars)
            end = min(len(content), idx + len(title) + chars)
            return content[start:end].strip()
        except ValueError:
            return ""