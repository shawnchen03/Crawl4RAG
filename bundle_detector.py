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
                model="gpt-4o-mini",
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
            
            # Add debug logging
            print("\nGPT Raw Response (first 100 chars):")
            print(repr(response.choices[0].message.content[:100]))  # Use repr() to see hidden chars
            
            # Save raw response before parsing
            raw_response_file = os.path.join(self.gpt_dir, "raw_gpt_response.txt")
            with open(raw_response_file, 'w', encoding='utf-8') as f:
                f.write(response.choices[0].message.content)
            
            try:
                # Clean the response string before parsing
                response_text = response.choices[0].message.content
                # Remove any BOM and whitespace
                response_text = response_text.encode().decode('utf-8-sig').strip()
                # Remove any null bytes
                response_text = response_text.replace('\x00', '')
                
                print("\nCleaned text (first 100 chars):")
                print(repr(response_text[:100]))
                
                result = json.loads(response_text)
                
                # Validate the structure we need
                if not isinstance(result, dict) or 'bundles' not in result:
                    print("Invalid response structure")
                    return None
                
                # Save GPT's analysis
                gpt_output_file = os.path.join(self.gpt_dir, "gpt_analysis.json")
                with open(gpt_output_file, 'w', encoding='utf-8') as f:
                    json.dump({
                        'input_links': all_links,
                        'gpt_analysis': result
                    }, f, indent=2)
                
                print("\nGPT's Selection Logic:")
                print(result.get('selection_logic', ''))
                print("\nGPT's Grouping Logic:")
                print(result.get('grouping_logic', ''))
                
                # Print bundles for verification
                print("\nDetected Bundles:")
                for name, data in result['bundles'].items():
                    print(f"\n{name}:")
                    print(f"Topic: {data['topic']}")
                    print("Articles:")
                    for article in data['articles']:
                        print(f"- {article}")
                
                return result['bundles']
                
            except json.JSONDecodeError as e:
                print(f"\nJSON Parse Error at position {e.pos}:")
                print(f"Line {e.lineno}, Column {e.colno}")
                print("Character causing the error:", repr(response_text[e.pos:e.pos+1]))
                # Try alternate parsing
                try:
                    import ast
                    print("\nTrying alternate parsing with ast.literal_eval")
                    result = ast.literal_eval(response_text)
                    return result['bundles']
                except Exception as ast_error:
                    print(f"Alternate parsing failed: {str(ast_error)}")
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