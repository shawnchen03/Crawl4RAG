class URLBundles:
    """Static class to store and manage URL bundles"""
    
    # Class variable to store bundles
    BUNDLES = {}
    
    @classmethod
    def get_bundle(cls, bundle_name: str) -> list:
        """Get URLs for a specific bundle"""
        return cls.BUNDLES.get(bundle_name, [])
    
    @classmethod
    def list_bundles(cls) -> list:
        """List all available bundle names"""
        return list(cls.BUNDLES.keys())
    
    @classmethod
    def add_bundle(cls, bundle_name: str, urls: list):
        """Add or update a bundle"""
        cls.BUNDLES[bundle_name] = urls
    
    @classmethod
    def clear_bundles(cls):
        """Clear all bundles"""
        cls.BUNDLES.clear()