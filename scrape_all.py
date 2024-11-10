from finance_crawler import FinanceCrawler
from article_formatter import ArticleFormatter
from url_bundles import URLBundles
from bundle_detector import BundleDetector
import os
from dotenv import load_dotenv
import time
import json
import argparse
from urllib.parse import urlparse

def parse_args():
    parser = argparse.ArgumentParser(description='Finance Article Scraper with Bundle Detection')
    parser.add_argument('--max-urls', type=int, default=100,
                       help='Maximum number of URLs to crawl (default: 100)')
    parser.add_argument('--delay', type=int, default=15,
                       help='Delay between processing bundles in seconds (default: 15)')
    parser.add_argument('--timeout', type=int, default=45,
                       help='Request timeout in seconds (default: 45)')
    parser.add_argument('--domain-limit', type=int, default=10,
                       help='Maximum URLs to process per domain (default: 10)')
    parser.add_argument('--min-content', type=int, default=500,
                       help='Minimum unique content length (default: 500 chars)')
    return parser.parse_args()

def get_safe_directory_name(url: str) -> str:
    """Convert URL to a safe directory name"""
    parsed = urlparse(url)
    # Combine netloc and path, replace unsafe chars with underscores
    path = (parsed.netloc + parsed.path).rstrip('/')
    safe_name = ''.join(c if c.isalnum() or c in ['.', '-'] else '_' for c in path)
    return safe_name

def main():
    # Parse command line arguments
    args = parse_args()
    
    # Load OpenAI API key
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        raise ValueError("Please set OPENAI_API_KEY environment variable")
    
    # Create base output directory consistently
    base_output_dir = "output"
    os.makedirs(base_output_dir, exist_ok=True)
    
    # Initialize run_dir at the start
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    run_dir = os.path.join(base_output_dir, f"run_{timestamp}")
    os.makedirs(run_dir, exist_ok=True)
    
    # Ask user for bundle source
    print("\nChoose bundle source:")
    print("1. Use predefined bundles")
    print("2. Detect bundles from website")
    choice = input("Enter choice (1 or 2): ")
    
    if choice == "2":
        # Get website URL from user
        base_url = input("\nEnter website URL to analyze: ")
        
        # Initialize detector with run_dir
        detector = BundleDetector(api_key, base_url, max_urls=args.max_urls, output_dir=run_dir)
        
        # Detect bundles
        detected_bundles = detector.detect_bundles()
        
        if not detected_bundles or not any(urls for urls in detected_bundles.values()):
            print("\nError: No valid bundles were detected from the website.")
            print("Please check the URL and try again.")
            return
        
        # Convert GPT's rich bundle format to URLBundles format
        simplified_bundles = {}
        if isinstance(detected_bundles, dict) and 'categories' in detected_bundles:
            # New GPT format
            for category, data in detected_bundles['categories'].items():
                if data.get('urls'):  # Only add if there are URLs
                    simplified_bundles[category] = data['urls']
        else:
            # Old format
            simplified_bundles = {k: v for k, v in detected_bundles.items() if v}  # Only keep non-empty bundles
        
        if not simplified_bundles:
            print("\nError: No valid bundles were created.")
            print("Please check the URL and try again.")
            return
        
        # Allow user to review and edit bundles
        print("\nDetected bundles:")
        for bundle_name, urls in simplified_bundles.items():
            print(f"\n{bundle_name}:")
            for url in urls:
                print(f"- {url}")
        
        proceed = input("\nProceed with these bundles? (y/n): ")
        if proceed.lower() != 'y':
            print("Exiting...")
            return
        
        # Clear existing bundles before updating
        URLBundles.BUNDLES.clear()
        URLBundles.BUNDLES.update(simplified_bundles)
    
    else:
        # Use same run_dir for predefined bundles
        scraper = FinanceCrawler(output_dir=run_dir, timeout=args.timeout)
        formatter = ArticleFormatter(api_key)
    
    # Rest of the scraping logic...
    all_bundles = URLBundles.list_bundles()
    
    print("\nConfiguration:")
    print(f"- Max URLs per bundle: {args.max_urls}")
    print(f"- Delay between bundles: {args.delay} seconds")
    print(f"- Request timeout: {args.timeout} seconds")
    print(f"- Output directory: {run_dir}")
    
    print("\nStarting comprehensive article scraping...")
    print(f"Will scrape {len(all_bundles)} bundles:")
    for bundle in all_bundles:
        print(f"- {bundle.replace('_', ' ').title()}")
    
    # Process each bundle
    for i, bundle in enumerate(all_bundles, 1):
        print(f"\n[{i}/{len(all_bundles)}] Processing bundle: {bundle.replace('_', ' ').title()}")
        try:
            # Create bundle directory inside articles directory
            bundle_dir = os.path.join(detector.articles_dir, bundle)
            os.makedirs(bundle_dir, exist_ok=True)
            
            # Set output directory for this specific bundle
            scraper.output_dir = bundle_dir
            
            # Scrape the bundle
            scraper.scrape_bundle(bundle)
            
            # Rename the combined file to include bundle name
            old_combined = os.path.join(bundle_dir, "finance_articles_combined.md")
            new_combined = os.path.join(bundle_dir, f"{bundle}_combined.md")
            if os.path.exists(old_combined):
                os.rename(old_combined, new_combined)
            
            time.sleep(args.delay)  # Configurable delay
                
        except Exception as e:
            print(f"Error processing bundle {bundle}: {str(e)}")
            continue
    
    # Combine all bundle files into one master file
    master_combined = os.path.join(run_dir, "master_combined.md")
    combine_all_bundles(run_dir, master_combined)
    
    # Format the master file
    master_formatted = os.path.join(run_dir, "master_formatted.md")
    formatter.format_articles(master_combined, master_formatted)
    
    print("\nProcessing completed!")
    print("Check the following locations for results:")
    print(f"1. Individual bundles: {run_dir}/[bundle_name]/")
    print(f"2. Master combined file: {master_combined}")
    print(f"3. Master formatted file: {master_formatted}")

if __name__ == "__main__":
    main()