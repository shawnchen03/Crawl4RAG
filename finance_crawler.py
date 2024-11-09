import requests
import urllib.parse
import os
from typing import List, Dict
import time
import tiktoken
from datetime import datetime
from bs4 import BeautifulSoup

class FinanceCrawler:
    def __init__(self, output_dir: str = "finance_documents"):
        self.output_dir = output_dir
        self.reader_base_url = "https://r.jina.ai/"
        self.chunk_size = 512
        self.overlap = 50
        self.encoder = tiktoken.encoding_for_model("gpt-3.5-turbo")
        os.makedirs(output_dir, exist_ok=True)
        
    def _count_tokens(self, text: str) -> int:
        return len(self.encoder.encode(text))
    
    def _chunk_text(self, text: str) -> List[Dict]:
        chunks = []
        tokens = self.encoder.encode(text)
        
        start = 0
        while start < len(tokens):
            end = start + self.chunk_size
            chunk_tokens = tokens[start:end]
            chunk_text = self.encoder.decode(chunk_tokens)
            
            chunks.append({
                "content": chunk_text,
                "token_count": len(chunk_tokens),
                "chunk_index": len(chunks),
                "start_position": start
            })
            
            start = end - self.overlap
            
        return chunks

    def _fetch_content(self, url: str) -> Dict:
        encoded_url = urllib.parse.quote(url, safe='')
        reader_url = f"{self.reader_base_url}{encoded_url}"
        
        headers = {
            "Accept": "text/markdown",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "x-with-generated-alt": "true",
            "x-timeout": "30",
        }
        
        try:
            print(f"\nFetching URL: {reader_url}")
            response = requests.get(reader_url, headers=headers, timeout=45)
            response.raise_for_status()
            
            content = response.text
            
            image_sections = []
            soup = BeautifulSoup(content, 'html.parser')
            
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
                    "token_count": self._count_tokens(content),
                    "category": self._get_category(url),
                    "has_images": len(image_sections) > 0,
                    "image_count": len(image_sections)
                }
            }
            
        except Exception as e:
            print(f"Error fetching {url}: {str(e)}")
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
            chunks = self._chunk_text(document["content"])
            
            with open(filepath, 'w', encoding='utf-8') as f:
                # Write metadata section
                f.write("---\n")
                for key, value in document["metadata"].items():
                    f.write(f"{key}: {value}\n")
                f.write("---\n\n")
                
                # Write original content
                f.write("# Original Content\n\n")
                f.write(document["content"])
                
                # Write chunked content
                f.write("\n\n# Chunked Content\n\n")
                for chunk in chunks:
                    f.write(f"\n## Chunk {chunk['chunk_index']} ")
                    f.write(f"(Tokens: {chunk['token_count']})\n\n")
                    f.write(chunk["content"])
                    f.write("\n")
                
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
        documents = []
        for url in urls:
            try:
                print(f"\nProcessing: {url}")
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