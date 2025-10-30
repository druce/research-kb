# Research Knowledge Base Extraction

A two-stage pipeline that extracts structured insights from research documents (PDFs and HTML) using LangChain and Google Gemini 2.0/2.5 to create a knowledge base for preparing presentations on AI adoption for buy-side Wall Street firms.

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

Each PDF generates a markdown file with:
- Key Findings
- Supporting Facts & Figures
- Key Quotes (with Attribution)
- Critical Capabilities
- Best Practices (do's and don'ts)
- AI Roadmap milestones
- Success Metrics and KPIs

Notes are formatted as standalone index cards, suitable for importing into Notion, Obsidian, or a RAG system.

## Customization

Edit `extract_knowledge.py` to modify:
- `GEMINI_MODEL`: Change the model (currently using gemini-2.0-flash-exp)
- `PDF_DIR`, `HTML_DIR`, `TXT_DIR`, `KB_DIR`: Change directory locations
- `RESEARCH_PROMPT`: Adjust the extraction prompt and categories
- Temperature and token settings in `setup_langchain_pipeline()`

## Benefits of Two-Stage Pipeline

1. **Cost Efficiency**: Review normalized text before incurring LLM processing costs
2. **Reprocessing**: Rerun Stage 2 with different prompts without re-extracting text
3. **Debugging**: Easier to identify issues in extraction vs. processing
4. **Incremental Processing**: Process subsets of files as needed
5. **Format Flexibility**: Supports both PDF and HTML input formats
6. **High-Quality Extraction**: Uses pymupdf for PDFs and trafilatura for HTML, both industry-standard tools
