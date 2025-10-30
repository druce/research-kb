"""
Knowledge Base Extraction Pipeline
Two-stage pipeline:
1. Normalize PDFs and HTML files to plain text
2. Process normalized text with LangChain and Gemini 2.5 to extract insights
"""

import os
from pathlib import Path
from typing import List
from dotenv import load_dotenv
import fitz  # pymupdf
import trafilatura
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# Configuration
GEMINI_MODEL = "gemini-2.0-flash-exp"  # Using Gemini 2.0 Flash (Gemini 2.5 will be "gemini-2.5-pro" when available)
PDF_DIR = Path("./pdf")
HTML_DIR = Path("./html")
TXT_DIR = Path("./txt")
KB_DIR = Path("./kb")
RESEARCH_PROMPT = """You are an AI research assistant helping me prepare a presentation on how buy-side Wall Street firms can take advantage of AI.

Please read the attached document carefully and extract all relevant insights into concise, standalone notes (1–3 sentences each). These notes should be factually grounded, contextually rich, and formatted for use as index cards in a knowledge base (e.g., Notion or a RAG system).

Each note should focus on one clear idea or insight and fall into one or more of the following categories:
  - Key Findings — major themes, conclusions, or trends
  - Supporting Facts & Figures — data points, statistics, or concrete evidence
  - Key Quotes (with Attribution) — relevant direct quotes from the text
  - Critical Capabilities — what buy-side firms must improve or develop, which dimensions to consider and how to evaluate where you are or want to be
  - Decisions about what technology and workflows to implement, how to organize learning and implementation
  - Best practices - do's and don'ts
  - AI Roadmap — stages, milestones on the path to adoption
  - Measuring Success — criteria, KPIs, or benchmarks for evaluating AI initiatives

Output Format
  - Use Markdown
  - Begin each note with a bolded title or short summary
  - Include source attribution or context if available (e.g., "— [Author/Report Name]")
  - Separate each note with a horizontal rule (---)
  - Use bullet lists where appropriate for clarity

Example:
**AI Adoption Accelerating Among Asset Managers**
Over 60% of buy-side firms report active AI initiatives in trading and research. Adoption is driven by competitive pressure and data accessibility. — McKinsey 2024 Report
---

**Key Capability: Data Integration and Governance**
Effective AI use depends on unified, clean, and well-governed data pipelines across front and middle office systems.
---

**Measuring Success in AI Programs**
Success metrics include model accuracy, alpha generation improvement, and operational efficiency gains.
---

Document to analyze:
{document_text}

Source: {document_name}
"""


def extract_text_from_pdf(pdf_path: Path) -> str:
    """Extract text content from a PDF file using pymupdf."""
    try:
        doc = fitz.open(str(pdf_path))
        text = ""
        for page in doc:
            text += page.get_text() + "\n"
        doc.close()
        return text
    except Exception as e:
        print(f"Error extracting text from {pdf_path.name}: {e}")
        return ""


def extract_text_from_html(html_path: Path) -> str:
    """Extract text content from an HTML file using trafilatura."""
    try:
        html_content = html_path.read_text(encoding='utf-8')
        # Use trafilatura to extract main content, removing scripts, ads, navigation, etc.
        text = trafilatura.extract(html_content, include_comments=False, include_tables=True)
        if text:
            return text
        else:
            print(f"  ⚠ Trafilatura returned no content, trying fallback")
            # Fallback: use trafilatura's bare extraction
            text = trafilatura.extract(html_content, include_comments=False, include_tables=True, output_format='txt', favor_recall=True)
            return text if text else ""
    except Exception as e:
        print(f"Error extracting text from {html_path.name}: {e}")
        return ""


def normalize_file(file_path: Path, output_dir: Path) -> bool:
    """Normalize a PDF or HTML file to plain text and save to output directory."""
    print(f"Normalizing: {file_path.name}")

    # Determine file type and extract text
    if file_path.suffix.lower() == '.pdf':
        text = extract_text_from_pdf(file_path)
    elif file_path.suffix.lower() in ['.html', '.htm']:
        text = extract_text_from_html(file_path)
    else:
        print(f"  ⚠ Unsupported file type: {file_path.suffix}")
        return False

    if not text.strip():
        print(f"  ⚠ No text extracted from {file_path.name}")
        return False

    print(f"  Extracted {len(text)} characters")

    # Create output directory if needed
    output_dir.mkdir(exist_ok=True)

    # Save as .txt file
    output_path = output_dir / f"{file_path.stem}.txt"
    output_path.write_text(text, encoding='utf-8')
    print(f"  ✓ Saved to {output_path}")

    return True


def setup_langchain_pipeline():
    """Set up the LangChain pipeline with Gemini."""
    # Initialize Gemini model
    llm = ChatGoogleGenerativeAI(
        model=GEMINI_MODEL,
        temperature=0.3,  # Lower temperature for more factual outputs
        max_output_tokens=8192,
    )

    # Create prompt template
    prompt = ChatPromptTemplate.from_template(RESEARCH_PROMPT)

    # Create chain
    chain = prompt | llm | StrOutputParser()

    return chain


def process_text_file(txt_path: Path, chain) -> str:
    """Process a normalized text file and return extracted insights."""
    print(f"Processing: {txt_path.name}")

    # Read normalized text
    try:
        document_text = txt_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"  ✗ Error reading {txt_path.name}: {e}")
        return None

    if not document_text.strip():
        print(f"  ⚠ Empty file: {txt_path.name}")
        return None

    print(f"  Read {len(document_text)} characters")

    # Run through LangChain pipeline
    try:
        insights = chain.invoke({
            "document_text": document_text,
            "document_name": txt_path.stem  # Use stem to remove .txt extension
        })
        print(f"  ✓ Generated insights")
        return insights
    except Exception as e:
        print(f"  ✗ Error processing with Gemini: {e}")
        return None


def save_markdown(content: str, source_name: str, output_dir: Path):
    """Save extracted insights to a markdown file."""
    # Create output directory if it doesn't exist
    output_dir.mkdir(exist_ok=True)

    # Generate output filename
    output_filename = source_name + ".md"
    output_path = output_dir / output_filename

    # Add header with source information
    header = f"# Research Notes: {source_name}\n\n"
    header += f"**Source:** `{source_name}`  \n"
    header += f"**Processed:** {Path.cwd().name}\n\n"
    header += "---\n\n"

    full_content = header + content

    # Write to file
    output_path.write_text(full_content, encoding='utf-8')
    print(f"  ✓ Saved to {output_path}")


def normalize_all_files():
    """Stage 1: Normalize all PDF and HTML files to plain text."""
    print("=" * 60)
    print("STAGE 1: NORMALIZING FILES TO PLAIN TEXT")
    print("=" * 60)
    print()

    # Find all PDFs and HTML files
    pdf_files = list(PDF_DIR.glob("*.pdf")) if PDF_DIR.exists() else []
    html_files = []
    if HTML_DIR.exists():
        html_files = list(HTML_DIR.glob("*.html")) + list(HTML_DIR.glob("*.htm"))

    all_files = pdf_files + html_files

    if not all_files:
        print("No PDF or HTML files found to normalize.")
        return 0

    print(f"Found {len(pdf_files)} PDF files and {len(html_files)} HTML files\n")

    # Normalize each file
    success_count = 0
    for file_path in all_files:
        if normalize_file(file_path, TXT_DIR):
            success_count += 1
        print()  # Blank line between files

    print(f"✓ Normalized: {success_count}/{len(all_files)} files")
    print(f"✓ Text files saved to: {TXT_DIR.absolute()}\n")

    return success_count


def process_all_texts():
    """Stage 2: Process all normalized text files with Gemini."""
    print("=" * 60)
    print("STAGE 2: PROCESSING TEXTS WITH GEMINI")
    print("=" * 60)
    print()

    # Verify API key is set
    if not os.getenv("GOOGLE_API_KEY"):
        print("Error: GOOGLE_API_KEY not found in environment variables.")
        print("Please create a .env file with your API key (see .env.example)")
        return 0

    # Find all normalized text files
    if not TXT_DIR.exists():
        print(f"Error: {TXT_DIR} directory not found. Run normalization first.")
        return 0

    txt_files = list(TXT_DIR.glob("*.txt"))

    if not txt_files:
        print(f"No text files found in {TXT_DIR}")
        return 0

    print(f"Found {len(txt_files)} text files\n")

    # Set up LangChain pipeline
    print("Setting up LangChain pipeline with Gemini...\n")
    chain = setup_langchain_pipeline()

    # Process each text file
    success_count = 0
    for txt_path in txt_files:
        insights = process_text_file(txt_path, chain)

        if insights:
            save_markdown(insights, txt_path.stem, KB_DIR)
            success_count += 1

        print()  # Blank line between files

    print(f"✓ Processed: {success_count}/{len(txt_files)} files")
    print(f"✓ Knowledge base saved to: {KB_DIR.absolute()}\n")

    return success_count


def main():
    """Main execution function - runs both stages of the pipeline."""
    print("\n")
    print("=" * 60)
    print("KNOWLEDGE BASE EXTRACTION PIPELINE")
    print("=" * 60)
    print()

    # Stage 1: Normalize files
    normalized = normalize_all_files()

    if normalized == 0:
        print("\nNo files were normalized. Exiting.")
        return

    # Stage 2: Process with Gemini
    processed = process_all_texts()

    # Final summary
    print("=" * 60)
    print("PIPELINE COMPLETE")
    print("=" * 60)
    print(f"Files normalized: {normalized}")
    print(f"Files processed: {processed}")
    print()


if __name__ == "__main__":
    main()
