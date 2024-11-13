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
from jina_reader import JinaReader
import json

class ContentCrawler:
    def __init__(self, output_dir: str = "./content", timeout: int = 130,
                 jina_reader: JinaReader = None):
        """Initialize crawler with output directory and timeout"""
        self.output_dir = output_dir
        self.reader_base_url = "https://r.jina.ai/"
        self.site_patterns = defaultdict(list)
        self.content_hashes = set()  # For duplicate checking
        self.url_content_map = {}    # Store URL to content mapping
        self.timeout = timeout
        self.jina_reader = jina_reader or JinaReader()
        
        # Create required directories
        self.articles_dir = os.path.join(output_dir, "articles")
        self.bundles_dir = os.path.join(output_dir, "bundles")
        os.makedirs(self.articles_dir, exist_ok=True)
        os.makedirs(self.bundles_dir, exist_ok=True)

    def scrape_bundle(self, bundle_name: str) -> List[Dict]:
        """Scrape a bundle and create its combined file"""
        urls = URLBundles.get_bundle(bundle_name)
        if not urls:
            print(f"Error: Bundle '{bundle_name}' not found!")
            return []
        
        print(f"\nProcessing bundle: {bundle_name}")
        
        # Create bundle directory under articles/
        bundle_dir = os.path.join(self.articles_dir, bundle_name)
        os.makedirs(bundle_dir, exist_ok=True)
        
        documents = []
        successful_articles = []
        
        # Process all URLs in bundle
        for url in urls:
            try:
                print(f"\nProcessing article: {url}")
                document = self._fetch_content(url)
                if document:
                    # Save article and track success
                    filepath = self._save_to_markdown(document, url, bundle_name)
                    if filepath:
                        documents.append(document)
                        successful_articles.append(filepath)
                        print(f"Successfully saved article to: {os.path.relpath(filepath, self.output_dir)}")
                    time.sleep(2)
            except Exception as e:
                print(f"Failed to process {url}: {str(e)}")
        
        # Create bundle's combined file only if we have articles
        if successful_articles:
            print(f"\nSuccessfully processed {len(successful_articles)} articles in bundle '{bundle_name}':")
            for article in successful_articles:
                print(f"- {os.path.relpath(article, self.output_dir)}")
            
            # Create combined file
            bundle_combined = os.path.join(bundle_dir, f"{bundle_name}_combined.md")
            num_unique = self._save_combined_markdown(documents, bundle_name, bundle_combined)
            print(f"Created combined file with {num_unique} unique articles: {os.path.relpath(bundle_combined, self.output_dir)}")
            return documents
        else:
            print(f"No articles were successfully processed for bundle '{bundle_name}'")
            return []

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

    def _is_duplicate_content(self, content: str, url: str) -> bool:
        """Enhanced duplicate checking using content similarity"""
        # Clean and normalize content
        cleaned_content = ' '.join(content.lower().split())
        content_hash = hash(cleaned_content)
        
        # Check exact duplicates
        if content_hash in self.content_hashes:
            print(f"Exact duplicate found for {url}")
            return True
            
        # Check similarity with existing content
        for stored_content in self.url_content_map.values():
            cleaned_stored = ' '.join(stored_content.lower().split())
            similarity = SequenceMatcher(None, cleaned_content, cleaned_stored).ratio()
            if similarity > 0.85:  # 85% similarity threshold
                print(f"Similar content found for {url} (similarity: {similarity:.2f})")
                return True
        
        # Store new content
        self.content_hashes.add(content_hash)
        self.url_content_map[url] = content
        return False

    def _fetch_content(self, url: str) -> Dict:
        """Fetch content using shared JinaReader"""
        content = self.jina_reader.fetch_content(url, timeout=self.timeout)
        if not content:
            return None
        
        # Check for duplicate content
        if self._is_duplicate_content(content, url):
            print(f"Skipping {url}: Duplicate content detected")
            return None
        
        # Process content
        content = self._detect_site_patterns(content, url)
        
        # Process images if present
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
        
        # Create document with metadata
        document = {
            "content": content,
            "metadata": {
                "url": url,
                "fetch_date": datetime.now().isoformat(),
                "length": len(content),
                "category": self._get_category(url),
                "cleaned_patterns": bool(self.site_patterns[self._get_domain(url)])
            }
        }
        
        print(f"Successfully fetched and processed content from: {url}")
        return document

    def _get_category(self, url: str) -> str:
        """Extract category from URL path"""
        path = url.split('/')[-2].replace('-', ' ').title()
        return path if path else 'General'

    def _save_to_markdown(self, document: Dict, url: str, bundle_name: str):
        """Save individual article in bundle-specific directory"""
        if not document:
            return None
        
        try:
            # Create bundle-specific directory under articles/
            bundle_dir = os.path.join(self.articles_dir, bundle_name)
            os.makedirs(bundle_dir, exist_ok=True)
            
            # Create filename
            parsed = urllib.parse.urlparse(url)
            safe_name = ''.join(c if c.isalnum() else '_' for c in parsed.netloc)
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"{safe_name}_{timestamp}_{abs(hash(url))}.md"
            
            filepath = os.path.join(bundle_dir, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                # Write metadata
                f.write("---\n")
                f.write(f"bundle: {bundle_name}\n")
                for key, value in document["metadata"].items():
                    f.write(f"{key}: {value}\n")
                f.write("---\n\n")
                
                # Write content
                f.write(document["content"])
            
            print(f"Saved article to: {os.path.relpath(filepath, self.output_dir)}")
            return filepath
        
        except Exception as e:
            print(f"Error saving article: {str(e)}")
            return None

    def _save_combined_markdown(self, documents: List[Dict], bundle_name: str, output_file: str):
        """Save bundle's combined markdown with metadata"""
        try:
            # Get bundle metadata
            gpt_analysis_file = os.path.join(self.output_dir, "gpt_data", "gpt_analysis.json")
            bundle_metadata = {}
            if os.path.exists(gpt_analysis_file):
                with open(gpt_analysis_file, 'r', encoding='utf-8') as f:
                    analysis = json.load(f)
                    bundle_metadata = analysis.get('gpt_analysis', {}).get('bundles', {}).get(bundle_name, {})
            
            with open(output_file, 'w', encoding='utf-8') as f:
                # Write bundle metadata
                f.write(f"# Bundle: {bundle_name}\n\n")
                f.write("## Bundle Metadata\n")
                f.write(f"Topic: {bundle_metadata.get('topic', '')}\n")
                f.write(f"Main Theme: {bundle_metadata.get('metadata', {}).get('main_theme', '')}\n")
                f.write(f"Key Concepts: {', '.join(bundle_metadata.get('metadata', {}).get('key_concepts', []))}\n")
                f.write(f"Target Audience: {bundle_metadata.get('metadata', {}).get('target_audience', '')}\n")
                f.write(f"Difficulty Level: {bundle_metadata.get('metadata', {}).get('difficulty_level', '')}\n\n")
                
                # Write articles with their relevance
                for doc in documents:
                    url = doc['metadata']['url']
                    article_metadata = next(
                        (a for a in bundle_metadata.get('articles', []) if a['url'] == url),
                        {'relevance': ''}
                    )
                    
                    f.write(f"## Article: {url}\n")
                    f.write(f"Relevance: {article_metadata.get('relevance', '')}\n\n")
                    f.write(doc['content'])
                    f.write("\n\n---\n\n")
            
            return len(documents)
        except Exception as e:
            print(f"Error saving combined markdown: {str(e)}")
            return 0

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
            combined_file = os.path.join(self.output_dir, "combined_articles.md")
            self._save_combined_markdown(documents, combined_file)