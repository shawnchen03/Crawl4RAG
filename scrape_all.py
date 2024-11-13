from content_crawler import ContentCrawler
from article_formatter import ArticleFormatter
from url_bundles import URLBundles
from bundle_detector import BundleDetector
import os
from dotenv import load_dotenv
import time
import json
import argparse
from urllib.parse import urlparse
from jina_reader import JinaReader
from api_logger import APILogger

def parse_args():
    parser = argparse.ArgumentParser(description='Content Scraper with Bundle Detection')
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

def get_bundle_preferences(max_urls: int):
    """Get user preferences for bundle organization"""
    print("\nBundle Configuration:")
    
    # First, choose bundle naming approach
    print("\nChoose bundle organization method:")
    print("1. Define your own bundle names")
    print("2. Let GPT suggest bundles")
    bundle_choice = input("Enter choice (1 or 2): ")
    
    if bundle_choice == "1":
        # User-defined bundles
        while True:
            try:
                num_bundles = int(input("\nHow many topic bundles would you like? (0 or 1-6)\n0 = Let GPT decide: "))
                if num_bundles == 0 or 1 <= num_bundles <= 6:
                    break
                print("Please enter 0 or a number between 1 and 6")
            except ValueError:
                print("Please enter a valid number")
        
        print(f"\nMaximum URLs to process: {max_urls}")
        
        if num_bundles == 0:
            return {
                "auto_detect": True,
                "max_urls": max_urls,
                "bundle_names": []
            }
        
        # Get bundle names
        bundle_names = []
        print("\nEnter the topic/name for each bundle:")
        for i in range(num_bundles):
            while True:
                name = input(f"Bundle {i+1}: ").strip()
                if name and name not in bundle_names:
                    bundle_names.append(name)
                    break
                print("Please enter a unique, non-empty name")
        
        return {
            "auto_detect": False,
            "num_bundles": num_bundles,
            "max_urls": max_urls,
            "bundle_names": bundle_names
        }
    else:
        # GPT-suggested bundles
        print(f"\nMaximum URLs to process: {max_urls}")
        print("\nGPT will analyze the content and suggest appropriate bundles")
        return {
            "auto_detect": True,
            "max_urls": max_urls,
            "bundle_names": []
        }

def main():
    args = parse_args()
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        raise ValueError("Please set OPENAI_API_KEY environment variable")
    
    # Create directory structure
    base_output_dir = "output"
    os.makedirs(base_output_dir, exist_ok=True)
    
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    run_dir = os.path.join(base_output_dir, f"run_{timestamp}")
    os.makedirs(run_dir, exist_ok=True)
    
    print("\nChoose bundle source:")
    print("1. Use predefined bundles")
    print("2. Detect bundles from website")
    choice = input("Enter choice (1 or 2): ")
    
    if choice == "2":
        # Pass max_urls from command line args
        bundle_prefs = get_bundle_preferences(args.max_urls)
        
        base_url = input("\nEnter website URL to analyze: ")
        # Initialize API logger
        api_logger = APILogger(run_dir)
        
        # Initialize shared components with logger
        reader = JinaReader()
        reader.set_cache_file(run_dir)
        reader.set_logger(api_logger)
        
        detector = BundleDetector(
            api_key, 
            base_url, 
            max_urls=args.max_urls,
            output_dir=run_dir,
            bundle_preferences=bundle_prefs,  # Now includes auto_detect flag
            jina_reader=reader,
            api_logger=api_logger
        )
        
        detected_bundles = detector.detect_bundles()
        
        if not detected_bundles:
            print("No bundles detected")
            return
        
        # Show detected bundles for confirmation
        print("\nDetected/Created bundles:")
        for name, urls in detected_bundles.items():
            print(f"\n{name}:")
            for url in urls:
                print(f"- {url}")
        
        proceed = input("\nProceed with these bundles? (y/n): ")
        if proceed.lower() != 'y':
            return
        
        # Convert and store bundles
        URLBundles.BUNDLES.clear()
        URLBundles.BUNDLES.update(detected_bundles)
    
    # Initialize crawler with shared reader
    scraper = ContentCrawler(
        output_dir=run_dir, 
        timeout=args.timeout,
        jina_reader=reader  # Pass same reader instance
    )
    
    # Process bundles
    bundle_combined_files = []
    successful_bundles = []
    
    for bundle_name in URLBundles.list_bundles():
        print(f"\nProcessing bundle: {bundle_name}")
        articles = scraper.scrape_bundle(bundle_name)
        
        if articles:
            bundle_dir = os.path.join(scraper.articles_dir, bundle_name)
            bundle_combined = os.path.join(bundle_dir, f"{bundle_name}_combined.md")
            
            if os.path.exists(bundle_combined):
                bundle_combined_files.append(bundle_combined)
                successful_bundles.append(bundle_name)
            
            time.sleep(args.delay)
    
    # Create master combined file
    master_combined = os.path.join(run_dir, "master_combined.md")
    
    if successful_bundles:
        print(f"\nSuccessfully processed {len(successful_bundles)} bundles:")
        for bundle in successful_bundles:
            print(f"- {bundle}")
        
        print("\nCreating master combined file...")
        with open(master_combined, 'w', encoding='utf-8') as outfile:
            for bundle_file in bundle_combined_files:
                bundle_name = os.path.basename(os.path.dirname(bundle_file))
                outfile.write(f"\n\n# Bundle: {bundle_name}\n\n")
                
                with open(bundle_file, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())
                    outfile.write("\n\n---\n\n")
        
        print(f"Master combined file created: {master_combined}")
        proceed = input("Would you like to format the combined content? (y/n): ")
        
        if proceed.lower() == 'y':
            print("\nFormatting combined content...")
            master_formatted = os.path.join(run_dir, "master_formatted.md")
            formatter = ArticleFormatter(api_key)
            formatter.format_articles(master_combined, master_formatted)
            print(f"\nFormatted content saved to: {master_formatted}")
        else:
            print("\nSkipping formatting. Process completed.")
            master_formatted = None
    else:
        print("\nNo bundles were successfully processed.")
        return
    
    print("\nProcessing completed!")
    print("Check the following locations for results:")
    print(f"1. Individual articles by bundle: {scraper.articles_dir}/[bundle_name]/")
    print("2. Bundle combined files:")
    for f in bundle_combined_files:
        print(f"   - {os.path.relpath(f, run_dir)}")
    print(f"3. Master combined file: {master_combined}")
    if master_formatted:
        print(f"4. Master formatted file: {master_formatted}")
    
    # Print API usage summary
    if api_logger:
        summary = api_logger.get_summary()
        print("\nAPI Usage Summary:")
        print(f"Jina Reader: {summary['jina_reader']['total_calls']} calls "
              f"({summary['jina_reader']['failed_calls']} failed)")
        print(f"GPT-4-40-mini: {summary['gpt-4-40-mini']['total_calls']} calls, "
              f"Total tokens: {summary['gpt-4-40-mini']['total_tokens']}, "
              f"Cost: ${summary['gpt-4-40-mini']['total_cost']:.4f}")

if __name__ == "__main__":
    main()