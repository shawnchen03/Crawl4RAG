from link_crawler import LinkCrawler
from link_organizer import LinkOrganizer
import os
from dotenv import load_dotenv
import time
import argparse
from urllib.parse import urlparse

def validate_url(url: str) -> bool:
    """Validate if string is a proper URL"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description='Crawl and organize links from a website. Example: python run_pipeline.py "https://example.com"'
    )
    parser.add_argument('url', type=str, 
                       help='The website URL to crawl (e.g., "https://example.com")')
    parser.add_argument('--output-dir', type=str, default='./output', 
                       help='Directory for output files (default: ./output)')
    
    args = parser.parse_args()
    
    # Validate URL
    if not validate_url(args.url):
        raise ValueError("Please provide a valid URL (e.g., 'https://example.com')")
    
    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Load environment variables
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        raise ValueError("Please set OPENAI_API_KEY environment variable")
    
    # Define output files
    crawled_file = os.path.join(args.output_dir, "crawled_links.json")
    bundles_file = os.path.join(args.output_dir, "organized_bundles.json")
    
    # Step 1: Crawl links
    print(f"\nStarting link crawling for: {args.url}")
    crawler = LinkCrawler(args.url, output_file=crawled_file)
    crawler.crawl()  # Using default depth in LinkCrawler
    
    # Wait a bit to avoid rate limiting
    time.sleep(2)
    
    # Step 2: Organize links
    print("\nStarting link organization...")
    organizer = LinkOrganizer(api_key)
    bundles = organizer.organize_links(crawled_file, output_file=bundles_file)
    
    print("\nPipeline completed!")
    print(f"1. Crawled links saved to: {crawled_file}")
    print(f"2. Organized bundles saved to: {bundles_file}")
    
    # Print bundle summary
    print("\nBundle Summary:")
    for bundle, urls in bundles.items():
        print(f"\n{bundle}: {len(urls)} articles")

if __name__ == "__main__":
    main() 