# Research Knowledge Base Extraction

An experiment using Claude Code to accelerate research for a presentation on AI adoption in hedge funds. This project demonstrates how to build a two-stage knowledge extraction pipeline that transforms research documents into a queryable knowledge base using LangChain and Google Gemini.

## Project Overview

This project explores two complementary approaches to research:

**Traditional Approach:** Tools like Google Gemini search on Google Drive folders and NotebookLM enable direct querying across research documents. For example, asking "What are important facts and figures about improving developer productivity using AI coding assistants?" across a collection of PDFs returns relevant insights quickly and effectively.

**Enhanced Pipeline Approach:** This project takes research a step further by:
1. Converting documents (PDFs, HTML) to normalized text
2. Applying structured prompts to extract key insights for AI strategy presentations
3. Organizing extracted knowledge into a queryable database
4. Using Claude Code skills to split and manage individual notes

The result is a curated knowledge base optimized for presentation preparation, where insights are pre-extracted, categorized, and ready for rapid retrieval.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API key:**
   - Copy `.env.example` to `.env`
   - Add your Google Gemini API key:
     ```
     GOOGLE_API_KEY=your_actual_api_key_here
     ```

3. **Get a Gemini API key:**
   - Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Create a new API key
   - Copy it to your `.env` file

## Usage

Run the complete two-stage pipeline:
```bash
python extract_knowledge.py
```

The pipeline operates in two stages:

**Stage 1: Normalization**
- Finds all PDF files in `pdf/` directory
- Finds all HTML files in `html/` directory
- Extracts and normalizes text from each file
- Saves plain text files to `txt/` directory

**Stage 2: Processing**
- Reads all normalized text files from `txt/` directory
- Processes each through Gemini with the research prompt
- Saves structured markdown notes to `kb/` directory

## Output Format

Each document generates a structured markdown file in the `kb/` directory with:
- **Key Findings** - Major themes, conclusions, and trends
- **Supporting Facts & Figures** - Data points and statistics
- **Key Quotes (with Attribution)** - Direct quotes from sources
- **Critical Capabilities** - Dimensions firms must develop
- **Best Practices** - Do's and don'ts for AI adoption
- **AI Roadmap** - Adoption stages and milestones
- **Success Metrics** - KPIs and benchmarks

Notes are formatted as standalone index cards, suitable for importing into Notion, Obsidian, or a RAG system.

## Claude Code Skills

This project includes custom Claude Code skills for knowledge base management:

### split-kb-note
Splits a single knowledge base markdown file containing multiple notes into individual note files.

Usage:
```bash
/split-kb-note
```

### split-all-kb-notes
Processes all markdown files in the `kb/` directory and splits each into individual notes in `kb2/`.

Usage:
```bash
/split-all-kb-notes
```

These skills enable granular organization of extracted knowledge, with each insight as a separate file for easier querying and management.

## Knowledge Base Structure

- `pdf/` - Source PDF research documents (not tracked in git)
- `html/` - Source HTML documents (not tracked in git)
- `txt/` - Normalized text files (not tracked in git)
- `kb/` - Structured markdown notes per document (68 files)
- `kb2/` - Individual note files split from kb/ (1,843 files)
- `notes.md` - All notes concatenated into a single file with `---` separators

## Extraction Prompt

The research extraction prompt is defined in `prompt.txt`. It instructs the AI to extract insights organized into these categories:
- **Key Findings** — Major themes, conclusions, or trends
- **Supporting Facts & Figures** — Data points, statistics, or concrete evidence
- **Key Quotes (with Attribution)** — Relevant direct quotes from sources
- **Critical Capabilities** — What buy-side firms must improve or develop
- **Decisions** — Technology and workflow implementation choices
- **Best Practices** — Do's and don'ts
- **AI Roadmap** — Stages and milestones on the path to adoption
- **Measuring Success** — Criteria, KPIs or benchmarks for evaluating AI initiatives

The prompt produces standalone notes (1-3 sentences each) formatted as index cards with source attribution.

## Customization

Edit `extract_knowledge.py` to modify:
- `GEMINI_MODEL`: Change the model (currently using gemini-2.0-flash-exp)
- `PDF_DIR`, `HTML_DIR`, `TXT_DIR`, `KB_DIR`: Change directory locations
- `RESEARCH_PROMPT`: Adjust the extraction prompt and categories (or reference `prompt.txt`)
- Temperature and token settings in `setup_langchain_pipeline()`

## Benefits of Two-Stage Pipeline

1. **Cost Efficiency**: Review normalized text before incurring LLM processing costs
2. **Reprocessing**: Rerun Stage 2 with different prompts without re-extracting text
3. **Debugging**: Easier to identify issues in extraction vs. processing
4. **Incremental Processing**: Process subsets of files as needed
5. **Format Flexibility**: Supports both PDF and HTML input formats
6. **High-Quality Extraction**: Uses pymupdf for PDFs and trafilatura for HTML, both industry-standard tools

## Research Sources

Source research documents are available in [this Google Drive folder](https://drive.google.com/drive/folders/1DgX9XaLe6ZhH0IxEyszf930dc7mbgjj8) (68+ PDFs and HTML files on AI adoption, strategy, and implementation for financial services).

## Results

- **68 research documents** processed
- **1,843 individual notes** extracted and organized
- **Consolidated knowledge base** in `notes.md` (532 KB)
- **Custom Claude Code skills** for knowledge management
- **Complete automation** from source documents to queryable knowledge base

## Custom GPT

A [custom GPT for AI Strategy Research](https://chatgpt.com/g/g-6900e2b7897481919e462a13c5678ad3-dv-strategy-research) has been created with:
- Raw article files from the research collection
- Summarized notes from `notes.md`
- Optimized for querying insights on AI adoption in financial services

This provides an interactive way to explore the research and get answers tailored to specific questions about AI strategy for hedge funds and asset managers.
