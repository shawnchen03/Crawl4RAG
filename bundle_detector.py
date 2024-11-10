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
    """Detects article bundles using Jina's search capabilities"""
    
    def __init__(self, api_key: str, base_url: str, max_urls: int = 100, output_dir: str = None):
        """Initialize detector with API key and base URL"""
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

    def detect_bundles(self) -> Dict[str, List[str]]:
        """Main method to detect and create URL bundles"""
        print("Starting bundle detection using Jina search...")
        
        # Get domain for site-specific search
        domain = urlparse(self.base_url).netloc
        
        # Extract topic from URL (e.g., 'data-science' from medium.com/tag/data-science)
        path_parts = urlparse(self.base_url).path.strip('/').split('/')
        if 'tag' in path_parts:
            topic = path_parts[path_parts.index('tag') + 1]
        else:
            topic = "articles"
            
        print(f"Searching for {topic} content on {domain}")
        
        # Try different search strategies
        search_queries = [
            f"{topic} articles",  # Basic search
            f"best {topic} articles",  # Quality focus
            f"popular {topic} articles",  # Popularity focus
            f"technical {topic} articles",  # Technical focus
            f"{topic} tutorials"  # Tutorial focus
        ]
        
        all_articles = []
        for query in search_queries:
            articles = self._search_with_jina(query, domain)
            if articles:
                all_articles.extend(articles)
                print(f"Found {len(articles)} articles for query: {query}")
                
                # Save intermediate results
                query_results = os.path.join(self.raw_dir, f"search_results_{query.replace(' ', '_')}.json")
                with open(query_results, 'w', encoding='utf-8') as f:
                    json.dump(articles, f, indent=2)
                    
                if len(all_articles) >= self.max_urls:
                    all_articles = all_articles[:self.max_urls]
                    break
                    
        if not all_articles:
            print("No articles found through any search query")
            return None
            
        # Process and bundle the articles
        return self._process_articles(all_articles)

    def _search_with_jina(self, query: str, domain: str) -> List[Dict]:
        """Search for articles using Jina's search endpoint"""
        try:
            encoded_query = quote(query)
            search_url = f"https://s.jina.ai/{encoded_query}?site={domain}"
            
            headers = {
                "Accept": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }
            
            response = requests.get(search_url, headers=headers, timeout=45)
            
            if response.status_code != 200:
                print(f"Search failed for query '{query}' with status {response.status_code}")
                return []
                
            results = response.json()
            
            # Filter and clean results
            articles = []
            for result in results:
                if all(k in result for k in ['title', 'content', 'url']):
                    # Clean and validate the article
                    if self._is_valid_article(result):
                        articles.append({
                            'title': result['title'],
                            'content': result['content'],
                            'url': result['url'],
                            'query': query  # Keep track of which query found this
                        })
            
            return articles
            
        except Exception as e:
            print(f"Error searching with query '{query}': {str(e)}")
            return []

    def _is_valid_article(self, article: Dict) -> bool:
        """Validate if the result is a proper article"""
        url = article['url'].lower()
        
        # Skip unwanted URLs
        if any(skip in url for skip in [
            '/signin', '/login', 
            'miro.medium.com', 'rsci.app.link',
            'javascript:', 'mailto:', 
            '.png', '.jpg', '.gif'
        ]):
            return False
            
        # Verify it's an article URL
        if not any(indicator in url for indicator in [
            '/article/', '/post/', '/blog/', 
            '/p/', '/story/', '/towards-data-science/',
            '/stackademic/'
        ]):
            return False
            
        # Check content length
        if len(article['content']) < 500:  # Minimum content length
            return False
            
        return True

    def _process_articles(self, articles: List[Dict]) -> Dict[str, List[str]]:
        """Process and bundle the found articles"""
        try:
            # Send to GPT for analysis
            client = openai.OpenAI()
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": f"""You are a content analyzer specializing in article discovery.
                    Analyze these {len(articles)} articles and:
                    1. Group them into 2-4 thematic bundles
                    2. Only include substantive technical articles
                    3. Ignore promotional or non-technical content
                    
                    Return as JSON with this structure:
                    {{
                        "bundles": {{
                            "bundle_name": {{
                                "urls": ["url1", "url2"],
                                "topic": "Topic description",
                                "reason": "Why these articles belong together",
                                "articles": ["Article 1 title", "Article 2 title"],
                                "search_queries": ["query1", "query2"]  # Which queries found these articles
                            }}
                        }},
                        "total_articles": "number of articles found",
                        "analysis_summary": "Brief summary of the content themes"
                    }}"""},
                    {"role": "user", "content": f"Analyze these articles and create thematic bundles:\n\n{json.dumps(articles, indent=2)}"}
                ],
                temperature=0.3,
                max_tokens=4000
            )
            
            # Process and save results
            result = json.loads(response.choices[0].message.content)
            
            # Save full analysis
            gpt_output_file = os.path.join(self.gpt_dir, "gpt_content_analysis.json")
            with open(gpt_output_file, 'w', encoding='utf-8') as f:
                json.dump({
                    'timestamp': time.strftime("%Y%m%d_%H%M%S"),
                    'gpt_response': response.choices[0].message.content,
                    'processed_results': result
                }, f, indent=2)
            
            # Store bundles
            self.url_categories = result['bundles']
            bundles_file = os.path.join(self.bundles_dir, "detected_bundles.json")
            with open(bundles_file, 'w', encoding='utf-8') as f:
                json.dump(result['bundles'], f, indent=2)
            
            return result['bundles']
            
        except Exception as e:
            print(f"Error processing articles: {str(e)}")
            return None