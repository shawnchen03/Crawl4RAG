class URLBundles:
    """Manages predefined and dynamically detected URL bundles"""
    
    BUNDLES = {
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
        # ... other bundles ...
    }
    
    @classmethod
    def get_bundle(cls, bundle_name: str) -> list:
        """Get URLs for a specific bundle"""
        return cls.BUNDLES.get(bundle_name, [])
    
    @classmethod
    def list_bundles(cls) -> list:
        """Get list of available bundle names"""
        return list(cls.BUNDLES.keys())
    
    @classmethod
    def get_all_urls(cls) -> list:
        """Get all URLs across all bundles"""
        all_urls = []
        for urls in cls.BUNDLES.values():
            all_urls.extend(urls)
        return all_urls 
    
    @classmethod
    def update_bundles(cls, new_bundles: dict):
        """Update bundles with new detected ones"""
        # Convert any complex bundle format to simple {name: [urls]} format
        simplified_bundles = {}
        for name, data in new_bundles.items():
            if isinstance(data, dict) and 'urls' in data:
                simplified_bundles[name] = data['urls']
            elif isinstance(data, list):
                simplified_bundles[name] = data
        
        cls.BUNDLES.update(simplified_bundles)