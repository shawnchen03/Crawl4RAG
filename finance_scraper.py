from finance_crawler import FinanceCrawler
import os
from typing import Dict, List

class FinanceScraper:
    def __init__(self, output_dir: str = "./mdforfinance"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        self.crawler = FinanceCrawler(output_dir=output_dir)
        
    # Expanded URL bundles with more comprehensive coverage
    URL_BUNDLES = {
        "investment_banking_basics": [
            "https://mergersandinquisitions.com/investment-banking/",
            "https://mergersandinquisitions.com/investment-banking-career-path/",
            "https://mergersandinquisitions.com/investment-banking-analyst/",
            "https://mergersandinquisitions.com/investment-banking-associate/",
            "https://mergersandinquisitions.com/investment-banking-vice-president/",
            "https://mergersandinquisitions.com/investment-banking-managing-director/"
        ],
        "financial_modeling_skills": [
            "https://mergersandinquisitions.com/financial-modeling/",
            "https://mergersandinquisitions.com/financial-modeling-tests/",
            "https://mergersandinquisitions.com/investment-banking-financial-modeling-test/",
            "https://mergersandinquisitions.com/excel-modeling/",
            "https://mergersandinquisitions.com/financial-modeling-courses/",
            "https://mergersandinquisitions.com/financial-modeling-mistakes/"
        ],
        "private_equity_careers": [
            "https://mergersandinquisitions.com/private-equity/",
            "https://mergersandinquisitions.com/private-equity-recruitment/",
            "https://mergersandinquisitions.com/healthcare-private-equity/",
            "https://mergersandinquisitions.com/private-equity-associate/",
            "https://mergersandinquisitions.com/private-equity-interview-questions/",
            "https://mergersandinquisitions.com/private-equity-case-studies/"
        ],
        "career_paths_comparison": [
            "https://mergersandinquisitions.com/investment-banking-vs-consulting/",
            "https://mergersandinquisitions.com/project-finance-vs-corporate-finance/",
            "https://mergersandinquisitions.com/wealth-management-vs-investment-banking/",
            "https://mergersandinquisitions.com/private-equity-vs-investment-banking/",
            "https://mergersandinquisitions.com/hedge-fund-vs-private-equity/",
            "https://mergersandinquisitions.com/venture-capital-vs-private-equity/"
        ],
        "interview_preparation": [
            "https://mergersandinquisitions.com/investment-banking-interview-questions/",
            "https://mergersandinquisitions.com/investment-banking-superday/",
            "https://mergersandinquisitions.com/walk-me-through-your-resume/",
            "https://mergersandinquisitions.com/why-investment-banking/",
            "https://mergersandinquisitions.com/technical-investment-banking-interview-questions/"
        ],
        "valuation_concepts": [
            "https://mergersandinquisitions.com/dcf-modeling/",
            "https://mergersandinquisitions.com/comparable-company-analysis/",
            "https://mergersandinquisitions.com/precedent-transactions-analysis/",
            "https://mergersandinquisitions.com/enterprise-value/",
            "https://mergersandinquisitions.com/terminal-value/"
        ],
        "industry_specific": [
            "https://mergersandinquisitions.com/technology-investment-banking/",
            "https://mergersandinquisitions.com/healthcare-investment-banking/",
            "https://mergersandinquisitions.com/real-estate-investment-banking/",
            "https://mergersandinquisitions.com/energy-investment-banking/",
            "https://mergersandinquisitions.com/consumer-retail-investment-banking/"
        ],
        "deal_analysis": [
            "https://mergersandinquisitions.com/mergers-and-acquisitions/",
            "https://mergersandinquisitions.com/merger-models/",
            "https://mergersandinquisitions.com/lbo-model/",
            "https://mergersandinquisitions.com/restructuring/",
            "https://mergersandinquisitions.com/pitch-books/"
        ]
    }
    
    def list_available_bundles(self) -> None:
        """Display available URL bundles"""
        print("\nAvailable URL bundles:")
        for bundle, urls in self.URL_BUNDLES.items():
            print(f"\n{bundle.replace('_', ' ').title()}:")
            for url in urls:
                print(f"  - {url}")

    def scrape_bundle(self, bundle_name: str) -> bool:
        """Scrape a specific predefined bundle"""
        if bundle_name not in self.URL_BUNDLES:
            print(f"Error: Bundle '{bundle_name}' not found!")
            self.list_available_bundles()
            return False
            
        urls = self.URL_BUNDLES[bundle_name]
        output_subdir = os.path.join(self.output_dir, bundle_name)
        os.makedirs(output_subdir, exist_ok=True)
        
        print(f"\nScraping {bundle_name.replace('_', ' ')} bundle...")
        print(f"Output directory: {os.path.abspath(output_subdir)}")
        
        self.crawler.process_urls(urls)
        return True

    def scrape_custom_urls(self, urls: List[str], bundle_name: str = "custom") -> bool:
        """Scrape a custom list of URLs"""
        output_subdir = os.path.join(self.output_dir, bundle_name)
        os.makedirs(output_subdir, exist_ok=True)
        
        print(f"\nScraping custom URL bundle: {bundle_name}")
        print(f"Output directory: {os.path.abspath(output_subdir)}")
        
        self.crawler.process_urls(urls)
        return True

    def scrape_multiple_bundles(self, bundle_names: List[str]) -> None:
        """Scrape multiple predefined bundles"""
        for bundle in bundle_names:
            self.scrape_bundle(bundle)

if __name__ == "__main__":
    # Initialize scraper
    scraper = FinanceScraper()
    
    # Example usage:
    print("Finance Article Scraper")
    print("1. List available bundles")
    print("2. Scrape a specific bundle")
    print("3. Scrape multiple bundles")
    print("4. Scrape custom URLs")
    
    choice = input("\nEnter your choice (1-4): ")
    
    if choice == "1":
        scraper.list_available_bundles()
        
    elif choice == "2":
        scraper.list_available_bundles()
        bundle = input("\nEnter bundle name to scrape: ")
        scraper.scrape_bundle(bundle)
        
    elif choice == "3":
        scraper.list_available_bundles()
        bundles = input("\nEnter bundle names separated by comma: ").split(",")
        scraper.scrape_multiple_bundles([b.strip() for b in bundles])
        
    elif choice == "4":
        urls = []
        print("\nEnter URLs (one per line, empty line to finish):")
        while True:
            url = input()
            if not url:
                break
            urls.append(url)
        name = input("Enter a name for this bundle: ")
        scraper.scrape_custom_urls(urls, name)
    
    else:
        print("Invalid choice!")