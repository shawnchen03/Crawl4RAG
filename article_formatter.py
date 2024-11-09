import os
from typing import Dict, List
import re
from pathlib import Path
import openai
import tiktoken

class ArticleFormatter:
    def __init__(self, api_key: str):
        """Initialize formatter with API key and setup token counter"""
        openai.api_key = api_key
        self.encoder = tiktoken.encoding_for_model("gpt-4")
        self.max_chunk_tokens = 3000  # Leave room for prompt and response
        
    def _count_tokens(self, text: str) -> int:
        """Count tokens in text"""
        return len(self.encoder.encode(text))
        
    def _chunk_content(self, content: str) -> List[str]:
        """Split content into chunks that fit within token limits"""
        chunks = []
        current_chunk = []
        current_tokens = 0
        
        for paragraph in content.split('\n\n'):
            paragraph_tokens = self._count_tokens(paragraph)
            
            if current_tokens + paragraph_tokens > self.max_chunk_tokens:
                # Save current chunk and start new one
                chunks.append('\n\n'.join(current_chunk))
                current_chunk = [paragraph]
                current_tokens = paragraph_tokens
            else:
                current_chunk.append(paragraph)
                current_tokens += paragraph_tokens
        
        if current_chunk:
            chunks.append('\n\n'.join(current_chunk))
            
        return chunks

    def _clean_markdown_links(self, content: str) -> str:
        """Remove markdown links but keep the text"""
        # Remove image links
        content = re.sub(r'!\[([^\]]*)\]\([^)]+\)', '', content)
        # Replace [text](url) with just text
        content = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', content)
        # Remove bare URLs
        content = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', content)
        return content

    def _format_with_gpt(self, content: str) -> str:
        """Format content using GPT-4 with improved error handling and chunking"""
        try:
            chunks = self._chunk_content(content)
            formatted_chunks = []
            
            for i, chunk in enumerate(chunks):
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": """You are a financial content editor focused on creating clean, structured educational content.
                        Your tasks:
                        1. Remove all URLs and links while preserving the link text
                        2. Organize content into clear sections with proper headers
                        3. Format with clean markdown
                        4. Ensure NO LINKS remain in the output
                        5. Keep the content factual and educational"""},
                        {"role": "user", "content": f"Format this content (chunk {i+1}/{len(chunks)}):\n\n{chunk}"}
                    ],
                    temperature=0.3,
                    max_tokens=4000
                )
                formatted_chunks.append(response.choices[0].message.content)
                
            # Combine chunks and ensure clean formatting
            formatted_content = '\n\n'.join(formatted_chunks)
            return self._clean_markdown_links(formatted_content)
            
        except Exception as e:
            print(f"Error in GPT formatting: {str(e)}")
            # Return cleaned original content as fallback
            return self._clean_markdown_links(content)

    def format_articles(self, input_file: str, output_file: str):
        """Format articles with improved section handling and error recovery"""
        try:
            # Read and clean input content
            with open(input_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Initial cleaning
            content = self._clean_markdown_links(content)
            
            # Format content
            formatted_content = self._format_with_gpt(content)
            
            # Save formatted content
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(formatted_content)
                
            print(f"Successfully formatted and saved to {output_file}")
            
        except Exception as e:
            print(f"Error formatting articles: {str(e)}")
            # Create backup of original content
            backup_file = f"{output_file}.backup"
            with open(backup_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Original content saved to {backup_file}")