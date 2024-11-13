import requests
from urllib.parse import quote
import json
import os
from bs4 import BeautifulSoup
from datetime import datetime

class JinaReader:
    """Singleton class to handle Jina reader API calls with caching"""
    
    _instance = None
    _cache = {}  # URL to content mapping
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(JinaReader, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.reader_base_url = "https://r.jina.ai/"
        self.cache_file = None
        self.api_logger = None
    
    def set_cache_file(self, run_dir: str):
        """Set cache file location for persistence"""
        self.cache_file = os.path.join(run_dir, "raw_data", "jina_cache.json")
        os.makedirs(os.path.dirname(self.cache_file), exist_ok=True)
        self._load_cache()
    
    def _load_cache(self):
        """Load cache from file if exists"""
        if self.cache_file and os.path.exists(self.cache_file):
            with open(self.cache_file, 'r', encoding='utf-8') as f:
                self._cache = json.load(f)
    
    def _save_cache(self):
        """Save cache to file"""
        if self.cache_file:
            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump(self._cache, f, indent=2)
    
    def set_logger(self, api_logger):
        """Set API logger"""
        self.api_logger = api_logger
    
    def _ensure_markdown_format(self, content: str, url: str) -> str:
        """Ensure content is properly formatted as markdown"""
        if not content:
            return None
            
        # Parse with BeautifulSoup to handle any HTML
        soup = BeautifulSoup(content, 'html.parser')
        
        # Extract title
        title = soup.find('h1')
        title_text = title.get_text() if title else url.split('/')[-1]
        
        # Format as markdown
        markdown_content = f"# {title_text}\n\n"
        markdown_content += f"Source URL: {url}\n\n"
        
        # Add metadata section
        markdown_content += "---\n"
        markdown_content += f"url: {url}\n"
        markdown_content += f"fetch_date: {datetime.now().isoformat()}\n"
        markdown_content += "---\n\n"
        
        # Add main content
        markdown_content += content
        
        return markdown_content
    
    def fetch_content(self, url: str, timeout: int = 130) -> str:
        """Fetch content with caching and logging"""
        if url in self._cache:
            if self.api_logger:
                self.api_logger.log_jina_call(url, 200, True)
            return self._cache[url]
        
        encoded_url = quote(url, safe='')
        reader_url = f"{self.reader_base_url}{encoded_url}"
        
        headers = {
            "Accept": "text/markdown",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "x-timeout": str(timeout),
        }
        
        try:
            print(f"Fetching from Jina (timeout: {timeout}s): {url}")
            response = requests.get(reader_url, headers=headers, timeout=timeout)
            
            if response.status_code == 200:
                if self.api_logger:
                    self.api_logger.log_jina_call(url, response.status_code, True)
                
                # Format content as markdown
                content = self._ensure_markdown_format(response.text, url)
                if content:
                    self._cache[url] = content
                    self._save_cache()
                    return content
                return None
            else:
                if self.api_logger:
                    self.api_logger.log_jina_call(url, response.status_code, False)
                print(f"Error fetching {url}: {response.status_code}")
                return None
                
        except Exception as e:
            if self.api_logger:
                self.api_logger.log_jina_call(url, 0, False, str(e))
            print(f"Error fetching {url}: {str(e)}")
            return None 