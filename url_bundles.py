class URLBundles:
    """Manages predefined and dynamically detected URL bundles"""
    
    BUNDLES = {
        "probability_statistics": [
            "https://towardsdatascience.com/understanding-descriptive-statistics-c9c2b0641291",
            "https://www.analyticsvidhya.com/blog/2017/04/40-questions-on-probability-for-all-aspiring-data-scientists/",
            "https://towardsdatascience.com/40-statistics-interview-problems-and-answers-for-data-scientists-6971a02b7eee",
            "https://towardsdatascience.com/probability-and-statistics-explained-in-the-context-of-deep-learning-ed1509b2eb3f",
            "https://www.youtube.com/watch?v=pYxNSUDSFH4",
            "https://medium.com/data-science-journal/the-bootstrap-the-swiss-army-knife-of-any-data-scientist-acd6e592be13",
            "https://mlwhiz.com/blog/2020/02/21/ci/",
            "https://towardsdatascience.com/p-value-explained-simply-for-data-scientists-4c0cd7044f14",
            "https://towardsdatascience.com/pdf-is-not-a-probability-5a4b8a5d9531",
            "https://mlwhiz.com/blog/2019/07/30/sampling/",
            "https://www.kdnuggets.com/2017/11/10-statistical-techniques-data-scientists-need-master.html",
            "https://youtu.be/wkxgZirbCr4"
        ],
        "sql_data_acquisition": [
            "https://towardsdatascience.com/5-common-sql-interview-problems-for-data-scientists-1bfa02d8bae6",
            "https://www.analyticsvidhya.com/blog/2017/01/46-questions-on-sql-to-test-a-data-science-professional-skilltest-solution/",
            "https://www.nicksingh.com/posts/30-sql-and-database-design-questions-from-real-data-science-interviews",
            "https://365datascience.com/sql-interview-questions/",
            "https://towardsdatascience.com/how-to-ace-data-science-interviews-sql-b71de212e433",
            "https://medium.com/@jayfeng/three-must-know-sql-questions-to-pass-your-data-science-interview-463311c7eaea",
            "https://www.java67.com/2013/04/10-frequently-asked-sql-query-interview-questions-answers-database.html",
            "https://hackernoon.com/technical-data-science-interview-questions-sql-and-coding-jv1k32bf",
            "https://www.datacamp.com/community/tutorials/sql-tutorial-query",
            "https://towardsdatascience.com/ten-sql-concepts-you-should-know-for-data-science-interviews-7acf3e428185"
        ],
        # ... Additional bundles can be added similarly ...
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