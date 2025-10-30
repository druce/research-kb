# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A knowledge extraction pipeline that processes research documents (PDFs and HTML) using LangChain and Google Gemini 2.0/2.5 to create structured markdown notes for preparing presentations on AI adoption for buy-side Wall Street firms.

## Directory Structure

- `pdf/` - Source PDF files to process (65+ research documents)
- `html/` - Source HTML files to process (will be normalized)
- `kb/` - Output directory for generated markdown knowledge base files
- `extract_knowledge.py` - Main extraction pipeline script

## Environment Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Key dependencies:
   - `langchain` & `langchain-google-genai`: LLM orchestration
   - `pymupdf`: Fast, high-quality PDF text extraction
   - `trafilatura`: Clean HTML text extraction (removes scripts, ads, navigation)
   - `python-dotenv`: Environment variable management

2. Configure API key:
   ```bash
   cp .env.example .env
   # Edit .env and add: GOOGLE_API_KEY=your_actual_api_key_here
   ```

Get Gemini API key from: https://aistudio.google.com/app/apikey

## Running the Pipeline

Run the complete two-stage pipeline:
```bash
python extract_knowledge.py
```

The pipeline executes in two stages:
1. **Stage 1 (Normalization)**: Converts all PDFs and HTML files to plain text in `txt/`
2. **Stage 2 (Processing)**: Processes normalized text through Gemini to generate knowledge base in `kb/`

## Code Architecture

**Two-stage pipeline** (`extract_knowledge.py`):

### Stage 1: Normalization (lines 68-123)
- `extract_text_from_pdf()`: Uses **pymupdf** (fitz) for fast, high-quality PDF text extraction
- `extract_text_from_html()`: Uses **trafilatura** library to extract clean text from HTML files, removing JavaScript, navigation, ads, and other web artifacts
- `normalize_file()`: Dispatcher that handles both PDFs and HTML, saves to `txt/` directory
- `normalize_all_files()`: Main stage 1 function that discovers and processes all files from `pdf/` and `html/` directories

### Stage 2: Processing (lines 139-287)
- `setup_langchain_pipeline()`: Initializes Gemini model (temperature=0.3, max_output_tokens=8192), creates prompt template chain
- `process_text_file()`: Reads normalized text files and processes through Gemini
- `save_markdown()`: Formats output with metadata header and writes to `kb/` directory
- `process_all_texts()`: Main stage 2 function that processes all normalized texts with LLM

### Main Orchestration (lines 290-318)
- `main()`: Runs both stages sequentially, provides progress reporting and final summary

## Key Customization Points

- `GEMINI_MODEL` (line 22): Switch between Gemini models (currently `gemini-2.0-flash-exp`)
- Directory paths (lines 23-26): `PDF_DIR`, `HTML_DIR`, `TXT_DIR`, `KB_DIR`
- `RESEARCH_PROMPT` (lines 27-65): Modify extraction categories, output format, or analysis focus
- Temperature and token limits in `setup_langchain_pipeline()` (lines 147-148)
- File discovery patterns in `normalize_all_files()` (lines 217-220) and `process_all_texts()` (line 261)

## Output Format

Each document generates a markdown file with categorized insights:
- Key Findings - major themes, conclusions, trends
- Supporting Facts & Figures - data points, statistics
- Key Quotes (with Attribution) - direct quotes from source
- Critical Capabilities - dimensions buy-side firms must develop
- Best Practices - do's and don'ts
- AI Roadmap - adoption stages and milestones
- Measuring Success - KPIs and benchmarks

Notes are formatted as standalone index cards suitable for Notion, Obsidian, or RAG systems.

## Pipeline Benefits

**Two-stage approach advantages:**
1. **Separation of concerns**: Text extraction is independent from LLM processing
2. **Cost efficiency**: Can review/edit normalized text before incurring LLM costs
3. **Reprocessing**: Can rerun Stage 2 with different prompts without re-extracting text
4. **Debugging**: Easier to identify whether issues are in extraction or processing
5. **Incremental processing**: Can process subsets of normalized files

## Running Individual Stages

To run only Stage 1 (normalization):
```python
from extract_knowledge import normalize_all_files
normalize_all_files()
```

To run only Stage 2 (processing with Gemini):
```python
from extract_knowledge import process_all_texts
process_all_texts()
```
