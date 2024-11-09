from finance_scraper import FinanceScraper
from article_formatter import ArticleFormatter
import os
from dotenv import load_dotenv
import time

def main():
    # Load OpenAI API key from environment variable
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        raise ValueError("Please set OPENAI_API_KEY environment variable")
    
    # Initialize scraper and formatter
    scraper = FinanceScraper()
    formatter = ArticleFormatter(api_key)
    
    # Get all available bundles
    all_bundles = list(scraper.URL_BUNDLES.keys())
    
    print("Starting comprehensive finance article scraping...")
    print(f"\nWill scrape {len(all_bundles)} bundles:")
    for bundle in all_bundles:
        print(f"- {bundle.replace('_', ' ').title()}")
    
    # Process each bundle
    for i, bundle in enumerate(all_bundles, 1):
        print(f"\n[{i}/{len(all_bundles)}] Processing bundle: {bundle.replace('_', ' ').title()}")
        try:
            # Create bundle directory path
            bundle_dir = os.path.join("./mdforfinance", bundle)
            
            # Scrape the bundle
            scraper.scrape_bundle(bundle)
            
            # Get paths for combined and formatted files
            combined_file = os.path.join(bundle_dir, "finance_articles_combined.md")
            formatted_file = os.path.join(bundle_dir, "finance_articles_formatted.md")
            
            # Verify combined file exists
            if os.path.exists(combined_file):
                print(f"\nFormatting combined content for {bundle}...")
                formatter.format_articles(combined_file, formatted_file)
            else:
                print(f"Warning: Combined file not found for {bundle}")
            
            # Add delay between bundles
            if i < len(all_bundles):
                print("Waiting 30 seconds before next bundle...")
                time.sleep(30)
                
        except Exception as e:
            print(f"Error processing bundle {bundle}: {str(e)}")
            continue
    
    print("\nProcessing completed!")
    print("Check the following locations for results:")
    print(f"1. Individual articles: ./mdforfinance/[bundle_name]/")
    print(f"2. Combined articles: ./mdforfinance/[bundle_name]/finance_articles_combined.md")
    print(f"3. Formatted articles: ./mdforfinance/[bundle_name]/finance_articles_formatted.md")

if __name__ == "__main__":
    main() 