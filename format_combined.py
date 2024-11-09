from article_formatter import ArticleFormatter
import os
from dotenv import load_dotenv
from pathlib import Path

def main():
    """Format the combined markdown file using GPT"""
    # Load OpenAI API key
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        raise ValueError("Please set OPENAI_API_KEY environment variable")
    
    # Initialize formatter
    formatter = ArticleFormatter(api_key)
    
    # Define input and output files
    input_file = "./mdforfinance/finance_articles_combined.md"
    output_file = "./mdforfinance/finance_articles_formatted.md"
    
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Combined file not found at {input_file}")
    
    print(f"\nFormatting combined articles file...")
    print(f"Input: {input_file}")
    print(f"Output: {output_file}")
    
    try:
        # Format the combined file
        formatter.format_articles(input_file, output_file)
        print(f"\nSuccessfully formatted combined articles!")
        print(f"Formatted content saved to: {output_file}")
        
    except Exception as e:
        print(f"Error formatting combined file: {str(e)}")
        # Create backup of original content if formatting fails
        backup_file = f"{output_file}.backup"
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                content = f.read()
            with open(backup_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Original content backed up to: {backup_file}")
        except Exception as be:
            print(f"Error creating backup: {str(be)}")

if __name__ == "__main__":
    main() 