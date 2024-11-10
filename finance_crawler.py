import requests
import urllib.parse
import os
from typing import List, Dict
import time
from datetime import datetime
from bs4 import BeautifulSoup
from url_bundles import URLBundles
import re
from difflib import SequenceMatcher
from collections import defaultdict
from urllib.parse import urlparse

class FinanceCrawler:
    def __init__(self, output_dir: str = "./mdforfinance", timeout: int = 45):
        """Initialize crawler with output directory and timeout"""
        self.output_dir = output_dir
        self.reader_base_url = "https://r.jina.ai/"
        self.site_patterns = defaultdict(list)  # Store common patterns by domain
        self.content_hashes = set()  # Store hashes of processed content
        self.timeout = timeout  # Store timeout value
        os.makedirs(output_dir, exist_ok=True)

    def scrape_bundle(self, bundle_name: str) -> bool:
        """Scrape a specific bundle of URLs"""
        urls = URLBundles.get_bundle(bundle_name)
        if not urls:
            print(f"Error: Bundle '{bundle_name}' not found!")
            return False
            
        bundle_dir = os.path.join(self.output_dir, bundle_name)
        os.makedirs(bundle_dir, exist_ok=True)
        
        # Set output directory for this specific bundle
        self.output_dir = bundle_dir
        
        print(f"\nScraping {bundle_name.replace('_', ' ')} bundle...")
        print(f"Output directory: {os.path.abspath(bundle_dir)}")
        
        self.process_urls(urls)
        return True

    def scrape_custom_urls(self, urls: List[str], bundle_name: str = "custom") -> bool:
        """Scrape a custom list of URLs"""
        bundle_dir = os.path.join(self.output_dir, bundle_name)
        os.makedirs(bundle_dir, exist_ok=True)
        
        self.output_dir = bundle_dir
        print(f"\nScraping custom URL bundle: {bundle_name}")
        print(f"Output directory: {os.path.abspath(bundle_dir)}")
        
        self.process_urls(urls)
        return True

    def _get_domain(self, url: str) -> str:
        """Extract domain from URL"""
        return urlparse(url).netloc

    def _detect_site_patterns(self, content: str, url: str) -> str:
        """Detect and remove common site-wide patterns"""
        domain = self._get_domain(url)
        
        # Split content into paragraphs
        paragraphs = content.split('\n\n')
        
        # If this is the first URL from this domain
        if not self.site_patterns[domain]:
            self.site_patterns[domain] = paragraphs
            return content
        
        # Find common patterns across pages from the same domain
        common_patterns = []
        for existing_para in self.site_patterns[domain]:
            for current_para in paragraphs:
                similarity = SequenceMatcher(None, existing_para, current_para).ratio()
                if similarity > 0.8:  # 80% similarity threshold
                    common_patterns.append(current_para)
        
        # Remove common patterns from content
        cleaned_paragraphs = [p for p in paragraphs if p not in common_patterns]
        
        # Update site patterns with new unique content
        self.site_patterns[domain].extend([p for p in paragraphs 
                                         if p not in common_patterns 
                                         and p not in self.site_patterns[domain]])
        
        return '\n\n'.join(cleaned_paragraphs)

    def _is_duplicate_content(self, content: str) -> bool:
        """Check if content is duplicate using simhash"""
        # Create a simple hash of the content's key phrases
        content_words = set(content.lower().split())
        content_hash = hash(frozenset(content_words))
        
        if content_hash in self.content_hashes:
            return True
        
        self.content_hashes.add(content_hash)
        return False

    def _fetch_content(self, url: str) -> Dict:
        """Fetch content using Jina's reader"""
        encoded_url = urllib.parse.quote(url, safe='')
        reader_url = f"{self.reader_base_url}{encoded_url}"
        
        headers = {
            "Accept": "text/markdown",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "x-with-generated-alt": "true",
            "x-timeout": str(self.timeout),
        }
        
        try:
            print(f"\nFetching URL: {reader_url}")
            response = requests.get(reader_url, headers=headers, timeout=self.timeout)
            
            # Extensive error handling
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
            
            content = response.text
            
            # Check for duplicate content
            if self._is_duplicate_content(content):
                print(f"Skipping {url}: Duplicate content detected")
                return None
            
            # Remove common site-wide patterns
            content = self._detect_site_patterns(content, url)
            
            # Process images if present (this is from Jina's reader output)
            image_sections = []
            soup = BeautifulSoup(content, 'html.parser')
            
            # Find image references in Jina's markdown output
            image_refs = soup.find_all(string=lambda text: text and '![' in text)
            for img in image_refs:
                caption = img.strip()
                if "Image" in caption and ":" in caption:
                    image_sections.append(f"\n### Image Analysis\n{caption}\n")
            
            if image_sections:
                content += "\n\n## Visual Content Analysis\n"
                content += "\n".join(image_sections)
            
            return {
                "content": content,
                "metadata": {
                    "url": url,
                    "fetch_date": datetime.now().isoformat(),
                    "length": len(content),
                    "category": self._get_category(url),
                    "cleaned_patterns": bool(self.site_patterns[self._get_domain(url)])
                }
            }
            
        except requests.exceptions.RequestException as e:
            if "timeout" in str(e).lower():
                print(f"Skipping {url}: Request timed out")
            elif "connection" in str(e).lower():
                print(f"Skipping {url}: Connection error")
            else:
                print(f"Skipping {url}: {str(e)}")
            return None
        except Exception as e:
            print(f"Skipping {url}: Unexpected error - {str(e)}")
            return None

    def _get_category(self, url: str) -> str:
        """Extract category from URL"""
        path = url.split('/')[-2]
        categories = {
            'financial-modeling': 'Technical Skills',
            'project-finance-vs-corporate-finance': 'Career Paths',
            'healthcare-private-equity': 'Industry Focus',
            'wealth-management-vs-investment-banking': 'Career Paths'
        }
        return categories.get(path, 'General')

    def _save_to_markdown(self, document: Dict, url: str):
        if not document:
            return
        
        parsed = urllib.parse.urlparse(url)
        safe_name = ''.join(c if c.isalnum() else '_' for c in parsed.netloc)
        filename = f"{safe_name}_{abs(hash(url))}.md"
        filepath = os.path.join(self.output_dir, filename)
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                # Write metadata section
                f.write("---\n")
                for key, value in document["metadata"].items():
                    f.write(f"{key}: {value}\n")
                f.write("---\n\n")
                
                # Write content
                f.write("# Original Content\n\n")
                f.write(document["content"])
                
            print(f"Successfully saved to {filepath}")
            
        except Exception as e:
            print(f"Error saving markdown file: {str(e)}")
    
    def _save_combined_markdown(self, documents: List[Dict], output_file: str):
        """Save all documents to a single markdown file with categorization"""
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                # Write title and introduction
                f.write("# Finance Articles Collection\n\n")
                
                # Group documents by category
                categories = {}
                for doc in documents:
                    cat = doc['metadata']['category']
                    if cat not in categories:
                        categories[cat] = []
                    categories[cat].append(doc)
                
                # Write table of contents with image indicators
                f.write("## Table of Contents\n\n")
                for category in sorted(categories.keys()):
                    f.write(f"### {category}\n")
                    for doc in categories[category]:
                        title = doc['metadata']['url'].split('/')[-2].replace('-', ' ').title()
                        image_indicator = "📸 " if doc['metadata'].get('has_images') else ""
                        f.write(f"- {image_indicator}[{title}](#{title.lower().replace(' ', '-')})\n")
                
                f.write("\n---\n\n")
                
                # Write articles by category
                for category in sorted(categories.keys()):
                    f.write(f"# {category}\n\n")
                    for doc in categories[category]:
                        title = doc['metadata']['url'].split('/')[-2].replace('-', ' ').title()
                        f.write(f"## {title}\n\n")
                        f.write(f"Source: {doc['metadata']['url']}\n")
                        f.write(f"Date fetched: {doc['metadata']['fetch_date']}\n")
                        if doc['metadata'].get('has_images'):
                            f.write(f"Images analyzed: {doc['metadata']['image_count']}\n")
                        f.write("\n---\n\n")
                        f.write(doc['content'])
                        f.write("\n\n---\n\n")
                    
            print(f"Successfully saved combined markdown to {output_file}")
            
        except Exception as e:
            print(f"Error saving combined markdown file: {str(e)}")

    def process_urls(self, urls: List[str]):
        """Process a list of URLs with duplicate detection"""
        documents = []
        domain_counts = defaultdict(int)
        
        for url in urls:
            domain = self._get_domain(url)
            domain_counts[domain] += 1
            
            # Skip if too many URLs from same domain
            if domain_counts[domain] > 10:  # Configurable limit
                print(f"Skipping {url}: Domain limit reached")
                continue
            
            try:
                document = self._fetch_content(url)
                if document:
                    self._save_to_markdown(document, url)
                    documents.append(document)
                time.sleep(2)
            except Exception as e:
                print(f"Failed to process {url}: {str(e)}")
        
        # Save combined markdown if we have documents
        if documents:
            combined_file = os.path.join(self.output_dir, "finance_articles_combined.md")
            self._save_combined_markdown(documents, combined_file)