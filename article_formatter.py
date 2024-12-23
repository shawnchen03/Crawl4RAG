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
        self.total_tokens_used = 0
        self.total_chunks_processed = 0
        
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
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": """You are a content editor focused on creating clean, structured educational content.
                        
                        Your tasks:
                        1. Preserve and enhance all metadata sections
                        2. Maintain bundle and article relationships
                        3. Keep relevance descriptions and topic connections
                        4. Format content with clear headers and structure
                        5. Clean up formatting while preserving information
                        6. Ensure all bundle metadata is prominently displayed
                        7. Keep content factual and educational
                        
                        Expected structure:
                        # Bundle: [name]
                        ## Bundle Metadata
                        - Topic: [topic]
                        - Main Theme: [theme]
                        - Key Concepts: [concepts]
                        - Target Audience: [audience]
                        - Difficulty Level: [level]
                        
                        ## Article: [url]
                        Relevance: [relevance description]
                        [content]
                        """},
                        {"role": "user", "content": f"Format this content (chunk {i+1}/{len(chunks)}):\n\n{chunk}"}
                    ],
                    temperature=0.3,
                    max_tokens=4000
                )
                
                # Track token usage
                self.total_tokens_used += response.usage.total_tokens
                self.total_chunks_processed += 1
                
                formatted_chunks.append(response.choices[0].message.content)
                
            # Combine chunks and ensure clean formatting
            formatted_content = '\n\n'.join(formatted_chunks)
            return self._clean_markdown_links(formatted_content)
            
        except Exception as e:
            print(f"Error in GPT formatting: {str(e)}")
            # Return cleaned original content as fallback
            return self._clean_markdown_links(content)

    def calculate_cost(self) -> Dict:
        """Calculate estimated cost based on GPT-4o-mini pricing"""
        # GPT-4o-mini pricing (as of 2024): $0.03/1K tokens for input, $0.06/1K tokens for output
        # Assuming roughly 2:1 ratio of input:output tokens
        input_tokens = int(self.total_tokens_used * 0.67)  # Approximate input tokens
        output_tokens = int(self.total_tokens_used * 0.33)  # Approximate output tokens
        
        input_cost = (input_tokens / 1000) * 0.03
        output_cost = (output_tokens / 1000) * 0.06
        total_cost = input_cost + output_cost
        
        return {
            "total_tokens": self.total_tokens_used,
            "chunks_processed": self.total_chunks_processed,
            "estimated_input_tokens": input_tokens,
            "estimated_output_tokens": output_tokens,
            "estimated_cost_usd": round(total_cost, 2)
        }

    def format_articles(self, input_file: str, output_file: str):
        """Format articles with improved section handling"""
        try:
            self.total_tokens_used = 0
            self.total_chunks_processed = 0
            
            # Read master combined file
            with open(input_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Format content
            formatted_content = self._format_with_gpt(content)
            
            # Save formatted version
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(formatted_content)
            
            # Calculate and display usage statistics
            stats = self.calculate_cost()
            print("\nFormatting Statistics:")
            print(f"Total tokens used: {stats['total_tokens']:,}")
            print(f"Chunks processed: {stats['chunks_processed']}")
            print(f"Estimated cost: ${stats['estimated_cost_usd']:.2f}")
            
        except Exception as e:
            print(f"Error formatting articles: {str(e)}")
            # Create backup
            backup_file = f"{output_file}.backup"
            with open(backup_file, 'w', encoding='utf-8') as f:
                f.write(content)