from typing import Dict, List
import os
from pathlib import Path
from finance_crawler import FinanceCrawler  # We'll rename this later

class ContentScraper:
    def __init__(self, output_dir: str = "./content"):
        """
        Initialize content scraper for any field
        
        Args:
            output_dir: Base directory for output files
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        self.crawler = FinanceCrawler(output_dir=output_dir)
        
    def define_content_bundle(self, field: str, urls: Dict[str, List[str]]) -> None:
        """
        Define URL bundles for any field
        
        Args:
            field: Name of the field (e.g., 'finance', 'technology', 'healthcare')
            urls: Dictionary of URL bundles for that field
        """
        self.field = field
        self.URL_BUNDLES = urls
        
    def scrape_bundle(self, bundle_name: str) -> str:
        """Scrape a specific bundle and return the output directory"""
        if bundle_name not in self.URL_BUNDLES:
            print(f"Error: Bundle '{bundle_name}' not found!")
            self.list_available_bundles()
            return None
            
        urls = self.URL_BUNDLES[bundle_name]
        output_subdir = os.path.join(self.output_dir, self.field, bundle_name)
        os.makedirs(output_subdir, exist_ok=True)
        
        print(f"\nScraping {bundle_name.replace('_', ' ')} bundle...")
        print(f"Output directory: {os.path.abspath(output_subdir)}")
        
        self.crawler.process_urls(urls)
        return output_subdir
    
    def list_available_bundles(self) -> None:
        """Display available URL bundles"""
        print(f"\nAvailable {self.field} bundles:")
        for bundle, urls in self.URL_BUNDLES.items():
            print(f"\n{bundle.replace('_', ' ').title()}:")
            for url in urls:
                print(f"  - {url}")

# Example usage:
if __name__ == "__main__":
    # Example for Technology articles
    TECH_BUNDLES = {
        "artificial_intelligence": [
            "https://techcrunch.com/category/artificial-intelligence/",
            "https://venturebeat.com/category/ai/"
        ],
        "blockchain": [
            "https://cointelegraph.com/",
            "https://decrypt.co/"
        ]
    }
    
    # Example for Healthcare articles
    HEALTHCARE_BUNDLES = {
        "medical_research": [
            "https://www.nature.com/subjects/medical-research",
            "https://www.thelancet.com/"
        ],
        "healthcare_policy": [
            "https://www.healthaffairs.org/",
            "https://www.modernhealthcare.com/"
        ]
    }
    
    # Initialize scraper for technology content
    tech_scraper = ContentScraper(output_dir="./tech_content")
    tech_scraper.define_content_bundle("technology", TECH_BUNDLES)
    
    # Initialize scraper for healthcare content
    health_scraper = ContentScraper(output_dir="./health_content")
    health_scraper.define_content_bundle("healthcare", HEALTHCARE_BUNDLES)
    
    # Scrape specific bundles
    tech_scraper.scrape_bundle("artificial_intelligence")
    health_scraper.scrape_bundle("medical_research") 