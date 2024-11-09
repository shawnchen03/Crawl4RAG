import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json
from typing import List, Dict
import re

class LinkCrawler:
    def __init__(self, base_url: str, output_file: str = "crawled_links.json"):
        """
        Initialize link crawler
        
        Args:
            base_url: Main website URL to start crawling
            output_file: File to save crawled links
        """
        self.base_url = base_url
        self.output_file = output_file
        self.visited_links = set()
        self.topic_links = {}
        
    def _is_valid_link(self, link: str) -> bool:
        """Check if link is valid and belongs to same domain"""
        if not link:
            return False
        
        # Add more patterns to exclude if needed
        excluded_patterns = [
            r'\.(jpg|jpeg|png|gif|pdf|doc|docx)$',
            r'javascript:',
            r'mailto:',
            r'tel:',
            r'#'
        ]
        
        for pattern in excluded_patterns:
            if re.search(pattern, link.lower()):
                return False
                
        return self.base_url in link
        
    def _extract_links(self, url: str) -> List[str]:
        """Extract all links from a page"""
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            links = []
            for a_tag in soup.find_all('a', href=True):
                link = urljoin(self.base_url, a_tag['href'])
                if self._is_valid_link(link):
                    links.append({
                        'url': link,
                        'text': a_tag.get_text().strip(),
                        'parent_url': url
                    })
            
            return links
            
        except Exception as e:
            print(f"Error extracting links from {url}: {str(e)}")
            return []
            
    def crawl(self, max_depth: int = 2):
        """
        Crawl website starting from base_url
        
        Args:
            max_depth: Maximum depth of crawling
        """
        def _crawl_recursive(url: str, depth: int):
            if depth > max_depth or url in self.visited_links:
                return
                
            print(f"Crawling: {url}")
            self.visited_links.add(url)
            
            links = self._extract_links(url)
            for link_data in links:
                link = link_data['url']
                if link not in self.visited_links:
                    # Store link with metadata
                    if url == self.base_url:
                        # Top-level links might be topic pages
                        self.topic_links[link] = {
                            'text': link_data['text'],
                            'articles': []
                        }
                    else:
                        # Add to parent topic if exists
                        parent = link_data['parent_url']
                        if parent in self.topic_links:
                            self.topic_links[parent]['articles'].append({
                                'url': link,
                                'text': link_data['text']
                            })
                    
                    _crawl_recursive(link, depth + 1)
        
        _crawl_recursive(self.base_url, 0)
        
        # Save results
        with open(self.output_file, 'w', encoding='utf-8') as f:
            json.dump(self.topic_links, f, indent=4)
            
        print(f"\nCrawling completed! Links saved to {self.output_file}")

if __name__ == "__main__":
    # Example usage
    crawler = LinkCrawler("https://mergersandinquisitions.com")
    crawler.crawl(max_depth=2) 