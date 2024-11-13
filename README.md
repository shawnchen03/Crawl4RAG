# Content Scraping & Organization Pipeline

A comprehensive tool for scraping, organizing, and formatting articles, with special handling for Medium and other content platforms.

## preperation:
Set up your environment:
install python dependencies:
```bash
pip install -r requirements.txt
```
set up your openai api key:
```bash
# Create .env file
echo "OPENAI_API_KEY=your_api_key_here" > .env
```
## Core Workflow
The pipeline operates in a clear sequence:

1. **Initial Content Fetch** (`bundle_detector.py`)
   ```
   Input URL → Jina Reader → raw_content.md
                          → Extract Links → all_links.json
   ```

2. **Bundle Organization** (`bundle_detector.py`)
   ```
   all_links.json → User Input → Bundle Topics
                 → GPT Analysis → detected_bundles.json
                               → bundles/[bundle_name]/
   ```
   

3. **Content Processing** (`content_crawler.py`)
   ```
   For each bundle in detected_bundles.json:
      For each URL in bundle:
         → Cached Jina Reader
         → Duplicate Check
         → Save to articles/[bundle_name]_*.md
         → Create bundles/[bundle_name]/combined.md
   ```

4. **Final Formatting** (`article_formatter.py`)
   ```
   Combined content → GPT Formatting → master_formatted.md
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
├── api_logs/                 # API tracking
│   ├── jina_calls.jsonl     # Jina API logs
│   └── gpt_calls.jsonl      # GPT API logs
├── raw_data/                # Initial processing
│   ├── raw_content.md      # Source page content
│   ├── all_links.json      # Extracted links
│   └── jina_cache.json     # API response cache
├── gpt_data/               # GPT processing
│   ├── raw_gpt_response.txt
│   └── detected_bundles.json
├── articles/               # Content by bundle
│   ├── bundle1/
│   │   ├── article1.md
│   │   ├── article2.md
│   │   └── bundle1_combined.md
│   └── bundle2/
│       ├── article3.md
│       ├── article4.md
│       └── bundle2_combined.md
├── master_combined.md      # All bundles combined
└── master_formatted.md     # Optional GPT formatting
```

### Features

1. **API Management**
   - Shared JinaReader singleton
   - Request caching (130s timeout)
   - API call logging
   - Cost tracking (GPT-4-40-mini: $3/1M tokens)

2. **Content Organization**
   - User-defined bundle topics (1-6 bundles)
   - Automatic content categorization
   - Duplicate detection
   - Size-limited bundles

3. **Processing Control**
   - Configurable URL limits
   - Domain-based throttling
   - Error recovery
   - Progress tracking

### Usage & Testing

1. Basic Test Run (5 articles):
```bash
# Navigate to the pipeline directory
cd finance_tools/crawler_scraper_pipeline

# Run with minimal articles for testing
python scrape_all.py --max-urls 5 --delay 3 --timeout 30

# When prompted:
1. Choose option 2 (Detect bundles from website)
2. Choose bundle organization method:
   - Option 1: Define your own bundles (1-6)
   - Option 2: Let GPT suggest bundles
3. Enter test URL: https://medium.com/tag/data-science/recommended
```

2. Production Run (15-20 articles):
```bash
python scrape_all.py \
  --max-urls 20 \
  --delay 5 \
  --timeout 130 \
  --domain-limit 5 \
  --min-content 500
```

3. Interactive Bundle Setup Examples:

Option 1 - User-defined bundles:
```
Choose bundle organization method:
1. Define your own bundle names
2. Let GPT suggest bundles
Enter choice (1 or 2): 1

How many topic bundles would you like? (0 or 1-6)
0 = Let GPT decide: 3

Enter the topic/name for each bundle:
Bundle 1: machine_learning
Bundle 2: data_analysis
Bundle 3: visualization
```

Option 2 - GPT-suggested bundles:
```
Choose bundle organization method:
1. Define your own bundle names
2. Let GPT suggest bundles
Enter choice (1 or 2): 2

GPT will analyze the content and suggest appropriate bundles
```

### Common Issues & Solutions

1. If Jina reader times out:
```bash
# Increase timeout (default 130s)
python scrape_all.py --max-urls 5 --timeout 180
```

2. For rate limiting:
```bash
# Increase delay between requests
python scrape_all.py --max-urls 5 --delay 10
```

3. For memory issues:
```bash
# Reduce batch size
python scrape_all.py --max-urls 3 --delay 5
```

Next steps:
1. Check current issues in CHANGELOG
2. Test with different websites
3. Focus on API and directory fixes
4. Add error handling improvements
5. Add more tests
6. Add CI/CD pipeline
7. Add documentation
