# Finance Article Tools

A comprehensive tool for scraping, organizing, and formatting financial articles, with special handling for Medium and other content platforms.

## Project Status

Current Implementation Status:
1. ✅ Enhanced content analysis with GPT-4
2. ✅ Full page content processing (not just links)
3. ✅ Support for Medium and other platforms
4. ✅ Duplicate content detection
5. ✅ Site-wide pattern removal
6. ✅ Command-line configuration

Last Working Point:
- Upgraded to OpenAI API v1.0
- Improved content analysis using full page context
- Enhanced bundle detection with GPT-4
- Added better error handling and validation
- Fixed silent fallbacks to predefined bundles

Next Steps:
1. Add more website-specific handlers
2. Implement rate limiting for API calls
3. Add support for authentication if needed
4. Improve bundle categorization logic

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
python scrape_all.py --max-urls 20 --delay 5 --timeout 45
# Choose option 2 when prompted
# Enter URL: https://medium.com/tag/data-science/recommended
```

## Features

- **Advanced Content Analysis**: 
  - Uses GPT-4 for comprehensive page analysis
  - Processes entire page content, not just links
  - Creates meaningful content bundles based on full context

- **Comprehensive Data Collection**:
  - Captures all relevant article content
  - Filters out navigation and system URLs
  - Handles pagination and dynamic content

- **Smart Processing**:
  - Detects and removes duplicate content
  - Removes common site-wide patterns
  - Validates bundle content before processing

- **Content Processing**:
  - The system uses two Jina AI approaches:
    1. **In-site Search**: Uses `s.jina.ai` to find relevant articles within a domain
    2. **Adaptive Crawler**: Uses `r.jina.ai` with adaptive crawler to recursively find content

  Benefits:
  - More focused article discovery
  - Better handling of large sites
  - Automatic relevance filtering
  - Reduced processing overhead

  GPT-4 analyzes this clean content to:
  1. Extract relevant article URLs
  2. Group them based on content relationships
  3. Provide context for grouping decisions
  4. Generate meaningful bundle descriptions

## Output Files

The system generates several JSON files for analysis:
1. `raw_content.md`: Full page content from Jina reader
2. `gpt_content_analysis.json`: GPT's detailed content analysis
3. `detected_bundles.json`: Final organized bundles
4. Individual article files in bundle directories

## Command-Line Options

```bash
python scrape_all.py [options]

Options:
  --max-urls N       Maximum articles to extract per page (default: 100)
  --delay N         Delay between requests in seconds (default: 15)
  --timeout N       Request timeout in seconds (default: 45)
  --domain-limit N  Max URLs per domain (default: 10)
  --min-content N   Minimum content length (default: 500)
```

## Directory Structure

```
output/
├── [timestamp]/
│   ├── raw_data/
│   │   ├── raw_content.md
│   │   └── extracted_links.json
│   ├── gpt_data/
│   │   ├── gpt_content_analysis.json
│   │   └── gpt_output.json
│   ├── bundles/
│   │   └── detected_bundles.json
│   └── articles/
│       └── [bundle_name]/
│           ├── individual_articles.md
│           └── bundle_combined.md
```

## Workflow

1. **Content Fetching**:
   - Uses Jina AI reader to fetch full page content
   - Saves raw content for analysis
   - Handles timeouts and errors

2. **Content Analysis**:
   - Sends full page content to GPT-4
   - Identifies article URLs and topics
   - Creates meaningful content bundles

3. **Bundle Processing**:
   - Validates bundle content
   - Filters out non-article URLs
   - Prevents empty bundle processing

4. **Output Generation**:
   - Creates organized directory structure
   - Saves all intermediate data
   - Generates combined and formatted output

## Error Handling

The system now handles:
- Network timeouts
- Access restrictions
- Invalid GPT responses
- Empty bundles
- Invalid URLs
- Silent fallbacks

## Development Notes

Key Classes:
- `BundleDetector`: Full page analysis and bundle creation
- `FinanceCrawler`: Content fetching and processing
- `ArticleFormatter`: Content cleanup and formatting

API Dependencies:
- OpenAI GPT-4 for content analysis
- Jina AI reader for content extraction

## Testing

Test the scraper with:
```bash
# Basic test (5 URLs)
python scrape_all.py --max-urls 5 --delay 5 --timeout 30

# Medium test
python scrape_all.py --max-urls 10 --delay 10 --timeout 45
# Enter: https://medium.com/tag/data-science/recommended
```

## Contributing

1. Check the Project Status section
2. Review known issues
3. Test with different websites
4. Submit PRs with website-specific improvements

## License

[Your License Here]