#backed up version of bundle_detector.py
import openai
from typing import List, Dict
from urllib.parse import urlparse, quote
import requests
from bs4 import BeautifulSoup
import json
from collections import defaultdict
import re
import time
import os

class BundleDetector:
    def __init__(self, api_key: str, base_url: str, max_urls: int = 100, output_dir: str = None):
        """Initialize bundle detector with OpenAI API key and base URL to crawl"""
        self.api_key = api_key
        openai.api_key = api_key
        self.base_url = base_url
        self.visited_urls = set()
        self.max_urls = max_urls
        self.reader_base_url = "https://r.jina.ai/"
        
        # Setup output directories
        domain = urlparse(base_url).netloc.replace('.', '_')
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        self.run_id = f"{domain}_{timestamp}"
        
        # Create directory structure
        self.output_dir = output_dir or "output"
        self.run_dir = os.path.join(self.output_dir, self.run_id)
        self.raw_dir = os.path.join(self.run_dir, "raw_data")
        self.gpt_dir = os.path.join(self.run_dir, "gpt_data")
        self.bundles_dir = os.path.join(self.run_dir, "bundles")
        self.articles_dir = os.path.join(self.run_dir, "articles")
        
        # Create all directories
        for dir_path in [self.raw_dir, self.gpt_dir, self.bundles_dir, self.articles_dir]:
            os.makedirs(dir_path, exist_ok=True)

    def _extract_urls_from_jina_content(self, content: str) -> List[str]:
        """Extract URLs and their context from Jina's reader formatted content"""
        try:
            # Extract all markdown links with their text
            markdown_links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
            
            # Filter out non-article URLs
            filtered_links = []
            for text, url in markdown_links:
                # Skip unwanted URLs
                if any(skip in url.lower() for skip in [
                    '/signin', '/login', 
                    'miro.medium.com', 'rsci.app.link',
                    'javascript:', 'mailto:', 
                    '.png', '.jpg', '.gif'
                ]):
                    continue
                    
                # Only keep article URLs
                if any(article_indicator in url.lower() for article_indicator in [
                    '/article/', '/post/', '/blog/', 
                    '/tag/', '/p/', '/story/'
                ]):
                    filtered_links.append({
                        'text': text,
                        'url': url.split('?')[0].split('#')[0],  # Clean URL
                        'type': 'article'
                    })
            
            if not filtered_links:
                print("Warning: No article URLs found. Check URL patterns.")
                return []
                
            # Save raw extracted data
            raw_data_file = os.path.join(self.raw_dir, "extracted_links.json")
            with open(raw_data_file, 'w', encoding='utf-8') as f:
                json.dump({
                    'base_url': self.base_url,
                    'extraction_time': time.strftime("%Y%m%d_%H%M%S"),
                    'link_count': len(filtered_links),
                    'extracted_data': filtered_links
                }, f, indent=2)
            
            print(f"\nFound {len(filtered_links)} article URLs:")
            for link in filtered_links[:5]:
                print(f"- {link['url']}")
            if len(filtered_links) > 5:
                print(f"... and {len(filtered_links)-5} more")
            
            return [link['url'] for link in filtered_links]
                
        except Exception as e:
            print(f"Error extracting URLs: {str(e)}")
            return []

    def _analyze_links_with_gpt(self, link_data: List[Dict]) -> List[str]:
        """Use GPT to analyze links and make intelligent decisions about them"""
        try:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            domain = urlparse(self.base_url).netloc.replace('.', '_')
            
            # Save input data
            gpt_input_file = os.path.join(self.gpt_dir, "gpt_input.json")
            links_text = "\n".join([
                f"Content: {link['text']}\nURL: {link['url']}\nType: {link['type']}"
                for link in link_data
            ])
            
            with open(gpt_input_file, 'w', encoding='utf-8') as f:
                json.dump({
                    'base_url': self.base_url,
                    'timestamp': timestamp,
                    'link_data': link_data,
                    'formatted_prompt': links_text
                }, f, indent=2)
            
            print(f"\nGPT input data saved to: {gpt_input_file}")
            
            # Updated to use GPT-4-mini
            client = openai.OpenAI()
            response = client.chat.completions.create(
                model="gpt-4-0125-preview",  # Changed to GPT-4-mini
                messages=[
                    {"role": "system", "content": """You are a content curator. Analyze all links, including navigation, images, and articles.
                    Create meaningful bundles based on content relationships and site structure."""},
                    {"role": "user", "content": f"""Analyze these links and create content bundles:
                    {links_text}
                    
                    Group ALL links (including navigation, images, etc.) into meaningful bundles.
                    Return as JSON:
                    {{
                        "bundles": {{
                            "bundle_name": {{
                                "urls": ["url1", "url2"],
                                "reason": "Why these links belong together"
                            }}
                        }},
                        "summary": "Brief explanation of your grouping logic"
                    }}"""}
                ],
                temperature=0.3,
                max_tokens=4000  # Adjusted for GPT-4-mini
            )
            
            # Save and display GPT's response
            gpt_output_file = os.path.join(self.gpt_dir, "gpt_output.json")
            result = json.loads(response.choices[0].message.content)
            
            with open(gpt_output_file, 'w', encoding='utf-8') as f:
                json.dump({
                    'base_url': self.base_url,
                    'timestamp': timestamp,
                    'gpt_response': response.choices[0].message.content,
                    'processed_results': result
                }, f, indent=2)
            
            print("\n=== GPT Analysis Results ===")
            print("\nBundles Created:")
            for bundle_name, data in result['bundles'].items():
                print(f"\n{bundle_name}:")
                print(f"Reason: {data['reason']}")
                print("URLs:")
                for url in data['urls']:
                    print(f"- {url}")
            
            print(f"\nAnalysis Summary: {result['summary']}")
            print(f"\nFull results saved to: {gpt_output_file}")
            
            # Convert GPT bundles to the format expected by the rest of the system
            simplified_bundles = {
                name: data['urls'] 
                for name, data in result['bundles'].items()
            }
            
            # Save detected bundles
            bundles_file = os.path.join(self.bundles_dir, "detected_bundles.json")
            with open(bundles_file, 'w', encoding='utf-8') as f:
                json.dump(simplified_bundles, f, indent=2)
            
            return list(set([url for urls in simplified_bundles.values() for url in urls]))
            
        except Exception as e:
            print(f"Error in GPT analysis: {str(e)}")
            return [link['url'] for link in link_data]

    def _fetch_with_jina(self, url: str) -> str:
        """Fetch content using Jina's reader"""
        encoded_url = quote(url, safe='')
        reader_url = f"{self.reader_base_url}{encoded_url}"
        
        headers = {
            "Accept": "text/markdown",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "x-with-generated-alt": "true",
            "x-timeout": "45",  # Increased timeout
        }
        
        try:
            print(f"Fetching with Jina: {url}")
            response = requests.get(reader_url, headers=headers, timeout=45)
            
            if response.status_code == 404:
                print(f"Skipping {url}: Page not found (404)")
                return None
            elif response.status_code == 403:
                print(f"Skipping {url}: Access denied (403)")
                return None
            elif response.status_code == 401:
                print(f"Skipping {url}: Authentication required (401)")
                return None
            elif response.status_code != 200:
                print(f"Skipping {url}: Unexpected status code {response.status_code}")
                return None
                
            return response.text
            
        except requests.exceptions.Timeout:
            print(f"Timeout while fetching {url}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {str(e)}")
            return None
        except Exception as e:
            print(f"Unexpected error fetching {url}: {str(e)}")
            return None

    def crawl_site_map(self) -> List[str]:
        """Crawl site for article URLs using Jina's reader"""
        try:
            print(f"Fetching page: {self.base_url}")
            content = self._fetch_with_jina(self.base_url)
            
            if not content:
                print("Failed to fetch initial content")
                return []

            # 1. Save raw content
            raw_content_file = os.path.join(self.raw_dir, "raw_content.md")
            with open(raw_content_file, 'w', encoding='utf-8') as f:
                f.write(content)
                
            # 2. Send to GPT for analysis
            client = openai.OpenAI()
            
            # Save GPT input
            gpt_input_file = os.path.join(self.gpt_dir, "gpt_input.json")
            with open(gpt_input_file, 'w', encoding='utf-8') as f:
                json.dump({
                    'content': content,
                    'max_urls': self.max_urls,
                    'base_url': self.base_url
                }, f, indent=2)
                
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": f"""You are a content analyzer specializing in article discovery.
                    The input is a Medium tag page in markdown format that contains article listings.
                    Each article has:
                    - Title in markdown heading format
                    - Author and publication info
                    - Link to the article
                    - Sometimes preview text or description
                    
                    Your task:
                    1. Find exactly {self.max_urls} most relevant and substantive articles
                    2. Group them into 2-4 thematic bundles
                    3. Ignore navigation links, sign-in prompts, and image URLs
                    4. Only include links that go to actual articles (usually containing /towards-data-science/ or /stackademic/ etc)
                    
                    Return as JSON with this structure:
                    {{
                        "bundles": {{
                            "bundle_name": {{
                                "urls": ["url1", "url2"],
                                "topic": "Topic description",
                                "reason": "Why these articles belong together",
                                "articles": ["Article 1 title", "Article 2 title"]
                            }}
                        }},
                        "total_articles": "number of articles found",
                        "analysis_summary": "Brief summary of the content themes"
                    }}"""},
                    {"role": "user", "content": f"Analyze this Medium tag page content and extract {self.max_urls} substantive articles into thematic bundles:\n\n{content}"}
                ],
                temperature=0.3,
                max_tokens=4000
            )
            
            # 4. Save GPT response and process results
            try:
                result = json.loads(response.choices[0].message.content)
                
                # Save full GPT analysis
                gpt_output_file = os.path.join(self.gpt_dir, "gpt_content_analysis.json")
                with open(gpt_output_file, 'w', encoding='utf-8') as f:
                    json.dump({
                        'timestamp': time.strftime("%Y%m%d_%H%M%S"),
                        'gpt_response': response.choices[0].message.content,
                        'processed_results': result
                    }, f, indent=2)
                
                # Extract URLs and save bundles
                all_urls = []
                for bundle_name, bundle_data in result.get('bundles', {}).items():
                    urls = bundle_data.get('urls', [])
                    # Only add URLs that look like actual articles
                    article_urls = [url for url in urls if any(x in url.lower() for x in [
                        '/towards-data-science/',
                        '/stackademic/',
                        '/article/',
                        '/post/',
                        '/p/'
                    ])]
                    all_urls.extend(article_urls)
                
                if not all_urls:
                    print("No article URLs found in GPT analysis")
                    return []
                
                print(f"\nFound {len(all_urls)} article URLs:")
                for url in all_urls[:5]:
                    print(f"- {url}")
                if len(all_urls) > 5:
                    print(f"... and {len(all_urls)-5} more")
                
                # Save final bundles
                bundles_file = os.path.join(self.bundles_dir, "detected_bundles.json")
                with open(bundles_file, 'w', encoding='utf-8') as f:
                    json.dump(result['bundles'], f, indent=2)
                
                # Store for later use
                self.url_categories = result['bundles']
                
                return all_urls
                    
            except json.JSONDecodeError as e:
                print(f"Error parsing GPT response: {str(e)}")
                print("GPT Response:", response.choices[0].message.content)
                return []
                    
        except Exception as e:
            print(f"Error crawling site: {str(e)}")
            return []

    def _should_try_pagination(self) -> bool:
        """Determine if we should try pagination based on the URL structure"""
        path = urlparse(self.base_url).path
        return any(x in path.lower() for x in ['/tag/', '/category/', '/archive/', '/page/'])

    def _handle_pagination(self) -> List[str]:
        """Handle pagination for sites that use it"""
        all_urls = []
        try:
            # Try common pagination patterns
            patterns = [
                f"{self.base_url}/page/{{}}", 
                f"{self.base_url}?page={{}}"
            ]
            
            for pattern in patterns:
                for page in range(2, 4):  # Try first few pages
                    page_url = pattern.format(page)
                    content = self._fetch_with_jina(page_url)
                    if content:
                        urls = self._extract_urls_from_jina_content(content)
                        all_urls.extend(urls)
                        if len(all_urls) >= self.max_urls:
                            return all_urls[:self.max_urls]
                    time.sleep(2)  # Be nice to the server
                    
        except Exception as e:
            print(f"Error handling pagination: {str(e)}")
            
        return all_urls

    def _extract_topics(self, urls: List[str]) -> List[Dict]:
        """Extract topics and metadata from URLs"""
        url_data = []
        for url in urls:
            try:
                # Get content preview using Jina
                content = self._fetch_with_jina(url)
                if not content:
                    continue
                
                # Extract title from content (first heading)
                title_match = re.search(r'^#\s+(.+?)(?:\n|$)', content, re.MULTILINE)
                title = title_match.group(1) if title_match else ''
                
                # Clean up title and extract keywords
                title = re.sub(r'[-_]', ' ', title)
                keywords = [word.lower() for word in title.split() 
                          if word.lower() not in {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for'}]
                
                url_data.append({
                    'url': url,
                    'title': title,
                    'keywords': keywords
                })
                
                time.sleep(1)  # Rate limiting
                
            except Exception as e:
                print(f"Error processing URL {url}: {str(e)}")
                continue
        
        return url_data

    def _cluster_urls(self, url_data: List[Dict]) -> Dict[str, List[str]]:
        """Use GPT to cluster URLs into meaningful bundles"""
        try:
            # Prepare data for GPT
            urls_text = "\n".join([
                f"Title: {d['title']}\nKeywords: {', '.join(d['keywords'])}\nURL: {d['url']}" 
                for d in url_data
            ])
            
            client = openai.OpenAI()  # Create client instance
            response = client.chat.completions.create(  # Use client.chat.completions
                model="gpt-4",
                messages=[
                    {"role": "system", "content": """You are a URL clustering expert.
                    Create meaningful topic bundles based on article titles and keywords.
                    Focus on the main topics and themes, ignoring images or media.
                    Return a JSON object where:
                    - Keys are bundle names (use snake_case)
                    - Values are lists of URLs
                    - Each bundle should have 2-5 related articles"""},
                    {"role": "user", "content": f"Create topic bundles for these articles:\n{urls_text}"}
                ],
                temperature=0.3,
                max_tokens=2000
            )
            
            # Parse GPT response into bundles
            try:
                bundles = json.loads(response.choices[0].message.content)  # Access content through message
                if not bundles:
                    raise ValueError("Empty bundles returned")
                return bundles
            except (json.JSONDecodeError, ValueError) as e:
                print(f"Error parsing GPT response: {str(e)}")
                print("GPT Response:", response.choices[0].message.content)
                return self._simple_clustering(url_data)
                
        except Exception as e:
            print(f"Error clustering URLs: {str(e)}")
            return self._simple_clustering(url_data)

    def _simple_clustering(self, url_data: List[Dict]) -> Dict[str, List[str]]:
        """Simple fallback clustering based on keywords"""
        clusters = defaultdict(list)
        for data in url_data:
            if data['keywords']:
                # Use most common keyword as cluster key
                key = max(set(data['keywords']), key=data['keywords'].count)
                clusters[key].append(data['url'])
        
        # Return None instead of empty dict if no clusters were created
        return dict(clusters) if clusters else None

    def detect_bundles(self) -> Dict[str, List[str]]:
        """Main method to detect and create URL bundles"""
        print("Starting bundle detection...")
        
        # Crawl site for URLs
        urls = self.crawl_site_map()
        if not urls:
            print("No URLs found to process")
            return None
        
        # Use the categories from GPT analysis if available
        if hasattr(self, 'url_categories') and self.url_categories:
            bundles = self.url_categories
        else:
            # Fallback to traditional clustering
            url_data = self._extract_topics(urls)
            if not url_data:
                print("No valid article data extracted")
                return None
                
            bundles = self._cluster_urls(url_data)
            if not bundles:
                print("No bundles could be created from the URLs")
                return None
        
        # Verify bundles have content
        if not any(urls for urls in bundles.values()):
            print("Bundles were created but contain no URLs")
            return None
        
        # Save bundles to file in proper directory
        output_file = os.path.join(self.bundles_dir, "detected_bundles.json")
        with open(output_file, 'w') as f:
            json.dump(bundles, f, indent=2)
        print(f"Bundles saved to {output_file}")
        
        return bundles