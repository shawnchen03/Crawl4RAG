# Finance Article Tools

This project consists of two main components:

1. **Finance Article Scraper & Formatter**: Scrapes financial articles and formats them into structured content
2. **Link Pipeline**: Crawls websites and organizes links using GPT

## Part 1: Finance Article Scraper & Formatter

A Python tool that scrapes financial articles from Mergers & Inquisitions, combines them into a single document, and uses GPT to format them into clean, structured content.

### Overview

The scraper works in two phases:
1. Scrapes articles and creates a combined markdown file
2. Uses GPT to format the combined content into a clean, structured document

### Usage

#### 1. Scraping Articles
```bash
python scrape_all.py
```
This script:
- Creates a `mdforfinance` directory
- Scrapes articles from predefined URL bundles
- Saves individual markdown files
- Creates a combined markdown file

#### 2. Formatting Content
```bash
python format_combined.py
```
This script:
- Takes the combined markdown file
- Processes it through GPT
- Saves a formatted version

### Output Files

The scraper generates:
- `mdforfinance/*.md` - Individual article files
- `mdforfinance/finance_articles_combined.md` - Combined raw content
- `mdforfinance/finance_articles_formatted.md` - GPT-formatted content

## Part 2: Link Pipeline

A tool that crawls websites to collect article links and organizes them into topic bundles using GPT.

### Overview

The pipeline works in two phases:
1. Crawls website to collect article links
2. Uses GPT to organize links into topic bundles

### Usage

#### Running the Full Pipeline
```bash
python pipeline/run_pipeline.py "https://example.com" --output-dir ./output
```
This script:
- Crawls the website to collect article links
- Organizes links into topic bundles using GPT
- Saves results to specified output directory

#### Individual Components

1. Link Crawler
```python
from pipeline.link_crawler import LinkCrawler

crawler = LinkCrawler("https://example.com")
crawler.crawl(max_depth=2)
```

2. Link Organizer
```python
from pipeline.link_organizer import LinkOrganizer

organizer = LinkOrganizer(api_key)
bundles = organizer.organize_links("crawled_links.json")
```

### Pipeline Output

The pipeline generates:
- `output/crawled_links.json` - Raw crawled links with metadata
- `output/organized_bundles.json` - GPT-organized topic bundles

## Installation (Common)

1. Clone the repository:
```bash
git clone <repository-url>
cd finance-tools
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with your OpenAI API key:
```bash
OPENAI_API_KEY=your_api_key_here
```

## Requirements

- Python 3.7+
- OpenAI API key
- Required packages:
  - requests
  - beautifulsoup4
  - openai
  - python-dotenv
  - tiktoken

## Project Structure
```
finance_tools/
├── pipeline/                    # Link Pipeline
│   ├── link_crawler.py         # Website crawling logic
│   ├── link_organizer.py       # GPT-based link organization
│   └── run_pipeline.py         # Pipeline script
├── mdforfinance/               # Scraper output directory
├── article_formatter.py        # Content formatting logic
├── finance_crawler.py          # Article scraping logic
├── finance_scraper.py          # URL management
├── scrape_all.py              # Main scraping script
├── format_combined.py          # Formatting script
└── requirements.txt            # Project dependencies
```
