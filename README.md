# Finance Article Tools

A comprehensive tool for scraping, organizing, and formatting financial articles, with special handling for Medium and other content platforms.

## Project Status (Updated 2024-11-10 02:00 AM)

Current Implementation Status:
1. ✅ Bundle detection working with GPT-4
2. ✅ Article scraping functional
3. ✅ Directory structure established
4. ⚠️ OpenAI API version needs update
5. ⚠️ Directory nesting needs fixing

Last Working Point:
- Successfully creating bundles from Medium tag pages
- Articles being scraped and saved
- Content organization working
- Rich metadata preserved

Next Steps:
1. Update OpenAI API calls to v1.0.0 format
2. Fix nested directory structure
3. Improve error handling
4. Add content validation

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up your environment:
```bash
# Create .env file
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

3. Run the scraper:
```bash
python scrape_all.py --max-urls 15 --delay 5 --timeout 60
# Choose option 2 when prompted
# Enter URL: https://medium.com/tag/data-science/recommended
```

## Features

- **Bundle Detection**: 
  - Uses GPT-4 for intelligent content analysis
  - Creates thematic bundles based on content
  - Preserves rich metadata for later use

- **Content Processing**:
  - Fetches content using Jina reader
  - Handles article extraction
  - Manages content organization

- **Directory Structure**:
```
output/run_[timestamp]/
├── raw_data/
│   ├── raw_content.md
│   └── all_links.json
├── gpt_data/
│   ├── raw_gpt_response.txt
│   └── gpt_analysis.json
├── bundles/
│   └── detected_bundles.json
└── [bundle_directories]/
    ├── medium_com_*.md
    └── finance_articles_combined.md
```

## Command-Line Options

```bash
python scrape_all.py [options]

Options:
  --max-urls N     Maximum articles to process (default: 100)
  --delay N        Delay between requests in seconds (default: 5)
  --timeout N      Request timeout in seconds (default: 60)
```

## Known Issues

1. OpenAI API Version:
   ```
   Error in GPT formatting: openai.ChatCompletion no longer supported in openai>=1.0.0
   ```
   - Need to update API calls or pin version

2. Directory Structure:
   - Nested bundle directories need flattening
   - Some paths too deep

3. Content Processing:
   - Rate limiting needs better handling
   - Some content duplication

## Development Notes

Current Focus:
1. API version compatibility
2. Directory structure cleanup
3. Error handling improvements
4. Content validation

Testing:
```bash
# Basic test (15 URLs, 5s delay)
python scrape_all.py --max-urls 15 --delay 5 --timeout 60

# Enter URL when prompted:
https://medium.com/tag/data-science/recommended
```

## Contributing

1. Check current issues in CHANGELOG
2. Test with different websites
3. Focus on API and directory fixes
4. Add error handling improvements

## License

[Your License Here]