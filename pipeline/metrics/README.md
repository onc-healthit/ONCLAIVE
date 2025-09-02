# LLM-Based Metrics

The Python scripts in this folder are to aid in the automated analysis of FHIR test kit development. These scrips should provide comprehensive coverage analysis, question extraction, and test kit comparison capabilities.

## Overview

There are five main analysis scripts designed to work with the artifacts that are generated during automated Test Kit development:

1. **IG Questions Extractor** - Extracts questions and issues from implementation guide markdown files
2. **Test Plan Coverage Analyzer** - Analyzes test coverage against detailed test plans
3. **Requirements Coverage Checker** - Evaluates requirements coverage in test plans
4. **Test Kit Comparator** - Compares different versions of test implementations for consistency
5. **Question Summary Generator** - Aggregates question counts across documents

## Prerequisites

- Required dependencies (install via pip):
  ```bash
  pip install python-dotenv
  ```
- LLM API access (Claude, GPT, or other supported models)
- `.env` file with API credentials

## Configuration

All scripts use a common configuration pattern at the top of each file. Key settings include:

- **LLM_UTILS_PATH**: Path to the LLM utilities module
- **API_TYPE**: Which LLM to use (`claude`, `gpt`, etc.)
- **MAX_TOKENS**: Token limit for LLM responses
- **MAX_WORKERS**: Concurrency level for parallel processing
- **Batching parameters**: Control batch sizes and processing limits

### Environment Setup

Be sure to have a `.env` file in the project root:
```
ANTHROPIC_API_KEY=your_claude_key_here
OPENAI_API_KEY=your_openai_key_here
```

## Scripts

### 1. IG Questions Extractor (`ig_questions_llm.py`)

Extracts implementation questions from markdown files at scale with intelligent batching.

**Features:**
- Batches multiple markdown files per LLM call to reduce API costs
- Handles large files by splitting into sections
- Exponential backoff for rate limiting
- Per-file JSON and Markdown output

**Usage:**
```bash
python3 pipeline/metrics/ig_questions_llm.py
```

**Configuration:**
- `IG_MD_DIR`: Directory containing markdown files
- `PROMPT_PATH`: Path to question extraction prompt `prompts/ig_questions.txt`
- `MAX_CHARS_PER_CALL`: Character limit per API call
- `MAX_FILES_PER_CALL`: File limit per batch

**Output:**
- `reports/<filename>_ig_questions.json`
- `reports/<filename>_ig_questions.md`

### 2. Test Plan Coverage Analyzer (`test_plan_coverage_llm.py`)

Analyzes test coverage against detailed test plans with exact requirement matching.

**Features:**
- Anchor-based plan excerpt extraction
- REQ range selection (`--req "1-123,1000-1228,77"`)
- Per-batch checkpointing for resumability
- Concurrent processing with worker pools
- Selective redo capability

**Usage:**
```bash
python3 pipeline/metrics/test_plan_coverage_llm.py [--req "1-100"] [--redo]
```

**Configuration:**
- `TEST_PLAN_PATH`: Path to test plan markdown
- `TEST_KIT_ROOT`: Root directory of Ruby test files
- `REQ range selection`: Filter specific requirements

**Output:**
- `reports_plannet_test_plan/test_plan_coverage.json`
- `reports_plannet_test_plan/test_plan_coverage.md`
- Checkpoints in `.chk/` directory

### 3. Requirements Coverage Checker (`requirements_coverage_llm.py`)

Evaluates how well test plans cover specified requirements with preprocessing optimization.

**Features:**
- Table of contents parsing for grouping
- Relevant test content extraction
- Concurrent batch processing
- Coverage percentage calculation

**Usage:**
```bash
python3 pipeline/metrics/requirements_coverage_llm.py
```

**Configuration:**
- `REQ_PATH`: Requirements markdown file
- `TEST_PLAN_PATH`: Test plan markdown file
- `ENABLE_PREPROCESSING`: Toggle optimization features

**Output:**
- `reports/requirements_coverage.json`
- `reports/requirements_coverage.md`

### 4. Test Kit Comparator (`compare_test_kits_llm.py`)

Compares two versions of test implementations for repeatability analysis.

**Features:**
- Semantic similarity scoring (0.0-1.0)
- Heuristic + LLM-based analysis
- Best-match pairing of test files
- Risk assessment for coverage gaps
- Per-requirement checkpointing

**Usage:**
```bash
python3 pipeline/metrics/compare_test_kits_llm.py
```

**Configuration:**
- `V1_ROOT`: First version directory
- `V2_ROOT`: Second version directory
- `REQ_FILTER`: Optional requirement range filter

**Output:**
- `reports_compare_kits_*/compare_report.json`
- `reports_compare_kits_*/compare_report.md`

### 5. Question Summary Generator (`summary_questions.py`)

Aggregates question counts across all analysis reports.

**Usage:**
```bash
python summary_questions.py
```

**Output:**
- `reports/question_count_summary.json`

## LLM Integration

All scripts use a common `llm_utils` module pattern:

```python
from llm_utils import LLMApiClient, API_CONFIGS

# Configure for deterministic output
if API_TYPE in API_CONFIGS:
    cfg = dict(API_CONFIGS[API_TYPE])
    cfg["temperature"] = 0.0  # or 0.1 for slight variation
    API_CONFIGS[API_TYPE] = cfg

client = LLMApiClient(config=API_CONFIGS)
```
Temperature can be configured here or within the LLM utils file. 

### Error Handling

All scripts include error handling:
- Exponential backoff with jitter for rate limits
- Checkpoint-based resumability
- Graceful handling of malformed responses
- Automatic JSON parsing with fallback strategies

## Output Formats

### JSON Reports
Machine-readable structured data with:
- Summary statistics
- Per-item details
- Scoring metrics
- Evidence references

### Markdown Reports
Human-readable summaries with:
- Coverage percentages
- Requirement breakdowns
- Issue lists with checkboxes
- Evidence links

## Directory Structure

```
project/
├── pipeline/
│   ├── llm_utils.py
│   └── checkpoints/
│       ├── markdown2_site/     # Cleaned IG markdown files
│       ├── gemini_8_13/        # Example Test kit version 1
│       └── gemini_7_30/        # Example Test kit version 2
├── prompts/
│   ├── ig_questions_new.txt
│   ├── test_plan_coverage.txt
│   └── requirements_coverage.txt
├── reports/                    # Output directory
├── .env                       # API credentials
└── dsl-guidance.md            # DSL reference
```

## Performance Optimization

- **Batching**: Multiple files processed per API call
- **Concurrency**: ThreadPoolExecutor for parallel processing
- **Caching**: Checkpoints prevent re-processing
- **Rate Limiting**: Intelligent backoff strategies
- **Memory Management**: Content truncation for large files

## Best Practices

1. **Start Small**: Test with a subset of requirements first
2. **Monitor Costs**: LLM API calls can be expensive at scale. Monitor costs using the API console dashboards. 
3. **Review Outputs**: LLM analysis should be validated by domain experts
4. **Checkpoint Management**: Use `--redo` selectively to avoid unnecessary re-processing
5. **Batch Sizing**: Adjust `MAX_CHARS_PER_CALL` based on your LLM's context limits

## Troubleshooting

### Common Issues

1. **Empty LLM responses**: Check API credentials and rate limits
2. **JSON parsing errors**: Review prompt engineering and response format
3. **File not found**: Verify path configurations at top of scripts
4. **Rate limiting**: Increase backoff delays or reduce concurrency

### Debug Mode

Most scripts include preview output:
```python
RAW_PREVIEW = 800  # Characters to preview from LLM responses
```

Set this higher for debugging response format issues.