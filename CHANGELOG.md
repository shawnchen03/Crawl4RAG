# Development Timeline

## v1.0.0 (Initial Version)
- Basic static bundle scraping
- Predefined URL bundles in `url_bundles.py`
- Simple article formatting
- Basic directory structure

## v1.1.0 (Content Processing)
- Added dynamic bundle detection
- Full page content processing with Jina reader
- GPT-4 content analysis
- Enhanced error handling
- Directory structure improvements
- Fixed OpenAI API v1.0 compatibility

## v1.2.0 (Search-Based Approach)
### Major Changes
- Split bundle detection into two approaches:
  1. Content-based (backed up as `bundle_detector_v1_content.py`)
  2. Search-based (new `bundle_detector.py`)
- Implemented Jina's search API for article discovery
- Added multiple search strategies

### Technical Improvements
- Better article validation
- Search query tracking
- Improved bundle organization
- Enhanced error handling
- Prevent silent fallbacks to predefined bundles

### Features Added
- Multiple search queries per topic
- Site-specific search capabilities
- Query result tracking
- Intermediate result storage
- Better content validation

### Documentation
- Updated README with new approaches
- Added clearer workflow documentation
- Improved command-line options description
- Better error messages and logging

## Future Plans
### v1.3.0 (Planned)
- Add rate limiting
- Implement authentication support
- Add more website-specific handlers
- Improve bundle categorization

### v1.4.0 (Planned)
- Add support for more content platforms
- Implement adaptive crawling
- Add content summarization
- Improve content deduplication 