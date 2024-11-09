import json
import os
from typing import Dict, List
import openai
from dotenv import load_dotenv

class LinkOrganizer:
    def __init__(self, api_key: str = None):
        """Initialize with OpenAI API key"""
        if api_key:
            openai.api_key = api_key
        
    def _chunk_links(self, links: List[Dict]) -> List[List[Dict]]:
        """Split links into chunks of reasonable size"""
        MAX_LINKS_PER_CHUNK = 20
        return [links[i:i + MAX_LINKS_PER_CHUNK] 
                for i in range(0, len(links), MAX_LINKS_PER_CHUNK)]
    
    def _organize_with_gpt(self, links: List[Dict]) -> Dict:
        """Use GPT to organize links into categories"""
        links_text = "\n".join([f"{link['text']}: {link['url']}" 
                               for link in links])
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": """You are a content organizer.
                    Analyze these links and group them into logical bundles.
                    Return the result as a JSON with bundle names as keys and lists of URLs as values.
                    Bundle names should be snake_case."""},
                    {"role": "user", "content": f"Organize these links into bundles:\n{links_text}"}
                ],
                temperature=0.3,
                max_tokens=2000
            )
            
            return json.loads(response.choices[0].message.content)
            
        except Exception as e:
            print(f"Error in GPT organization: {str(e)}")
            return {}
    
    def organize_links(self, input_file: str, output_file: str = "organized_bundles.json"):
        """
        Organize crawled links into bundles using GPT
        
        Args:
            input_file: JSON file with crawled links
            output_file: Output file for organized bundles
        """
        # Load crawled links
        with open(input_file, 'r', encoding='utf-8') as f:
            topic_links = json.load(f)
        
        # Flatten the structure
        all_links = []
        for topic, data in topic_links.items():
            all_links.extend(data['articles'])
        
        # Process in chunks
        chunks = self._chunk_links(all_links)
        organized_bundles = {}
        
        print(f"Processing {len(chunks)} chunks of links...")
        
        for i, chunk in enumerate(chunks, 1):
            print(f"Processing chunk {i}/{len(chunks)}...")
            chunk_bundles = self._organize_with_gpt(chunk)
            
            # Merge with existing bundles
            for bundle, urls in chunk_bundles.items():
                if bundle in organized_bundles:
                    organized_bundles[bundle].extend(urls)
                else:
                    organized_bundles[bundle] = urls
        
        # Save organized bundles
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(organized_bundles, f, indent=4)
            
        print(f"\nOrganization completed! Bundles saved to {output_file}")
        
        return organized_bundles

if __name__ == "__main__":
    # Load API key
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        raise ValueError("Please set OPENAI_API_KEY environment variable")
    
    # Initialize organizer
    organizer = LinkOrganizer(api_key)
    
    # Organize links
    bundles = organizer.organize_links("crawled_links.json") 