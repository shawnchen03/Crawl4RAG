import openai
from typing import List, Dict
from urllib.parse import urlparse, quote
import requests
import json
import time
import os
import re
from jina_reader import JinaReader

class BundleDetector:
    """Simple bundle detector using Jina reader and GPT"""
    
    def __init__(self, api_key: str, base_url: str, max_urls: int = 100, 
                 output_dir: str = None, bundle_preferences: dict = None,
                 jina_reader: JinaReader = None, api_logger = None):
        self.api_key = api_key
        self.base_url = base_url
        self.max_urls = max_urls
        self.bundle_preferences = bundle_preferences
        self.jina_reader = jina_reader or JinaReader()
        
        # Setup directories
        self.output_dir = output_dir
        self.raw_dir = os.path.join(output_dir, "raw_data")
        self.gpt_dir = os.path.join(output_dir, "gpt_data")
        
        for dir_path in [self.raw_dir, self.gpt_dir]:
            os.makedirs(dir_path, exist_ok=True)
        
        self.api_logger = api_logger

    def _fetch_with_jina(self, url: str) -> str:
        """Use shared JinaReader instance"""
        return self.jina_reader.fetch_content(url)

    def detect_bundles(self) -> Dict[str, List[str]]:
        """Main method to detect and create URL bundles"""
        print("Starting bundle detection...")
        
        # Use shared reader
        content = self.jina_reader.fetch_content(self.base_url)
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
            
            # Construct prompt based on preferences
            if self.bundle_preferences:
                if self.bundle_preferences.get('auto_detect'):
                    bundle_instruction = f"""Analyze these links and:
                    1. Create 2-4 thematic bundles based on content similarity
                    2. Each bundle should contain 1-6 URLs
                    3. Total URLs across ALL bundles must not exceed {self.max_urls}
                    4. Name bundles based on their common themes
                    5. Provide detailed metadata for each bundle
                    """
                else:
                    bundle_instruction = f"""Analyze these links and organize them into exactly {self.bundle_preferences['num_bundles']} bundles:
                    {', '.join(self.bundle_preferences['bundle_names'])}

                    Rules:
                    1. Use ONLY the specified bundle names
                    2. Each bundle should contain 1-6 URLs
                    3. Total URLs across ALL bundles must not exceed {self.max_urls}
                    4. Distribute URLs based on relevance to each topic
                    5. Skip any URLs that don't fit the specified topics
                    """
            else:
                bundle_instruction = f"""Analyze these links and:
                1. Create 1-6 thematic bundles
                2. Total URLs must not exceed {self.max_urls}
                3. Group by content similarity
                """

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system", 
                        "content": f"""You are a content organization assistant.
                        
                        {bundle_instruction}
                        
                        Return as JSON:
                        {{
                            "bundles": {{
                                "bundle_name": {{
                                    "urls": ["url1", "url2"],
                                    "topic": "Topic description",
                                    "metadata": {{
                                        "main_theme": "Core theme of this bundle",
                                        "key_concepts": ["concept1", "concept2"],
                                        "target_audience": "Who this content is for",
                                        "difficulty_level": "beginner/intermediate/advanced"
                                    }},
                                    "articles": [
                                        {{
                                            "url": "article_url",
                                            "relevance": "One sentence explaining how this article relates to the bundle topic"
                                        }}
                                    ]
                                }}
                            }},
                            "total_urls": "Total number of URLs",
                            "selection_logic": "Explain your selection process"
                        }}"""
                    },
                    {
                        "role": "user",
                        "content": f"Here are the links to organize:\n\n{json.dumps(all_links, indent=2)}"
                    }
                ],
                temperature=0.3,
                max_tokens=2000
            )
            
            if self.api_logger:
                self.api_logger.log_gpt_call(
                    response.usage.prompt_tokens,
                    response.usage.completion_tokens,
                    True,
                    task="bundle_detection"
                )
            
            # 1. First save raw response
            raw_response = response.choices[0].message.content
            raw_response_file = os.path.join(self.gpt_dir, "raw_gpt_response.txt")
            with open(raw_response_file, 'w', encoding='utf-8') as f:
                f.write(raw_response)
            print(f"Raw GPT response saved to: {raw_response_file}")
            
            # 2. Clean response - remove any JSON code block markers
            cleaned_response = raw_response.strip()
            if cleaned_response.startswith('```json'):
                cleaned_response = cleaned_response[7:]
            if cleaned_response.endswith('```'):
                cleaned_response = cleaned_response[:-3]
            cleaned_response = cleaned_response.strip()
            
            # 3. Try to parse JSON
            try:
                rich_analysis = json.loads(cleaned_response)
                print("Successfully parsed GPT response")
            except json.JSONDecodeError as e:
                print(f"Failed to parse GPT response: {str(e)}")
                print("Attempting alternate parsing method...")
                # Try alternate parsing
                try:
                    import ast
                    # Remove any potential markdown formatting
                    cleaned_text = cleaned_response.replace('```json', '').replace('```', '')
                    rich_analysis = ast.literal_eval(cleaned_text)
                    print("Successfully parsed using alternate method")
                except Exception as parse_error:
                    print(f"All parsing attempts failed: {str(parse_error)}")
                    return None
            
            # 4. Save rich analysis
            gpt_output_file = os.path.join(self.gpt_dir, "gpt_analysis.json")
            with open(gpt_output_file, 'w', encoding='utf-8') as f:
                json.dump({
                    'input_links': all_links,
                    'gpt_analysis': rich_analysis
                }, f, indent=2)
            
            # Add URL count validation
            total_urls = sum(len(data['urls']) for data in rich_analysis['bundles'].values())
            if total_urls > self.max_urls:
                print(f"Warning: GPT returned {total_urls} URLs, exceeding limit of {self.max_urls}")
                # Trim URLs to meet limit
                remaining = self.max_urls
                trimmed_bundles = {}
                for name, data in rich_analysis['bundles'].items():
                    urls_to_take = min(remaining, len(data['urls']))
                    if urls_to_take > 0:
                        trimmed_data = data.copy()
                        trimmed_data['urls'] = data['urls'][:urls_to_take]
                        trimmed_bundles[name] = trimmed_data
                        remaining -= urls_to_take
                    if remaining <= 0:
                        break
                rich_analysis['bundles'] = trimmed_bundles
            
            # Convert to simplified format for scrape_all.py
            simple_bundles = {}
            for name, data in rich_analysis['bundles'].items():
                bundle_name = name.lower().replace(' ', '_')
                simple_bundles[bundle_name] = data['urls']
            
            # Verify final count
            final_total = sum(len(urls) for urls in simple_bundles.values())
            print(f"\nTotal URLs to process: {final_total} (max allowed: {self.max_urls})")
            
            return simple_bundles
            
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