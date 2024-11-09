from finance_crawler import FinanceCrawler
import os
from typing import Dict

class TestBundleScraper:
    def __init__(self, base_dir: str = "./mdforfinance"):
        self.base_dir = base_dir
        self.test_urls = {
            "investment_banking_basics": {
                "url": "https://mergersandinquisitions.com/investment-banking/",
                "index": "01"
            },
            "financial_modeling_skills": {
                "url": "https://mergersandinquisitions.com/financial-modeling/",
                "index": "02"
            },
            "private_equity_careers": {
                "url": "https://mergersandinquisitions.com/private-equity/",
                "index": "03"
            },
            "career_paths_comparison": {
                "url": "https://mergersandinquisitions.com/investment-banking-vs-consulting/",
                "index": "04"
            },
            "interview_preparation": {
                "url": "https://mergersandinquisitions.com/investment-banking-interview-questions/",
                "index": "05"
            },
            "valuation_concepts": {
                "url": "https://mergersandinquisitions.com/dcf-modeling/",
                "index": "06"
            },
            "industry_specific": {
                "url": "https://mergersandinquisitions.com/technology-investment-banking/",
                "index": "07"
            },
            "deal_analysis": {
                "url": "https://mergersandinquisitions.com/mergers-and-acquisitions/",
                "index": "08"
            }
        }
        
    def create_directory_structure(self):
        """Create organized directory structure"""
        for bundle, info in self.test_urls.items():
            bundle_dir = os.path.join(self.base_dir, f"{info['index']}_{bundle}")
            os.makedirs(bundle_dir, exist_ok=True)
            
    def scrape_test_articles(self):
        """Scrape one test article from each bundle"""
        for bundle, info in self.test_urls.items():
            print(f"\nProcessing bundle: {bundle}")
            bundle_dir = os.path.join(self.base_dir, f"{info['index']}_{bundle}")
            
            # Initialize crawler for this bundle
            crawler = FinanceCrawler(output_dir=bundle_dir)
            
            # Process single URL
            try:
                print(f"Testing URL: {info['url']}")
                crawler.process_urls([info['url']])
                
                # Rename combined file to include bundle index
                old_combined = os.path.join(bundle_dir, "finance_articles_combined.md")
                new_combined = os.path.join(bundle_dir, f"{info['index']}_{bundle}_combined.md")
                
                if os.path.exists(old_combined):
                    os.rename(old_combined, new_combined)
                    
            except Exception as e:
                print(f"Error processing {bundle}: {str(e)}")
            
            print(f"Completed {bundle} test")

if __name__ == "__main__":
    # Initialize and run test scraper
    print("Starting test bundle scraping...")
    scraper = TestBundleScraper()
    
    # Create directory structure
    scraper.create_directory_structure()
    
    # Scrape test articles
    scraper.scrape_test_articles()
    
    print("\nTest scraping completed!") 