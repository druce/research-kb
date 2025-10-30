#!/usr/bin/env python3
"""
Split KB Notes Helper Script

Splits a knowledge base markdown file from kb/ directory into individual note files
in the kb2/ directory. Each note is saved as a separate file with source attribution.

Usage:
    python split_kb_notes.py <filename>

Example:
    python split_kb_notes.py "McKinsey - what is generative ai.md"
    python split_kb_notes.py JaggedFrontier.md
"""

import sys
import re
from pathlib import Path


def split_kb_notes(filename):
    """
    Split a KB markdown file into individual note files.

    Args:
        filename: Name of the file in kb/ directory (e.g., "McKinsey - what is generative ai.md")

    Returns:
        List of created filenames
    """

    # Validate input
    kb_path = Path('kb') / filename
    if not kb_path.exists():
        print(f"Error: File not found: {kb_path}")
        print(f"\nAvailable files in kb/:")
        for f in sorted(Path('kb').glob('*.md')):
            print(f"  - {f.name}")
        return []

    # Read the file
    print(f"Reading: {filename}")
    content = kb_path.read_text(encoding='utf-8')

    # Extract source from header
    source_match = re.search(r'\*\*Source:\*\*\s*`([^`]+)`', content)
    if not source_match:
        print(f"Error: Could not find source in {filename}")
        print("Expected format: **Source:** `source_name`")
        return []

    source = source_match.group(1)
    print(f"Source: {source}")

    # Find where header ends (first --- after the metadata section)
    lines = content.split('\n')
    header_end_idx = 0
    found_first_separator = False

    for i, line in enumerate(lines):
        if line.strip() == '---':
            if found_first_separator:
                header_end_idx = i + 1
                break
            found_first_separator = True

    # Get content after header
    remaining_content = '\n'.join(lines[header_end_idx:])

    # Split by --- to get individual notes
    notes = [note.strip() for note in remaining_content.split('---')]
    notes = [note for note in notes if note]  # Remove empty notes

    print(f"Found {len(notes)} notes")

    # Create kb2 directory
    kb2_dir = Path('kb2')
    kb2_dir.mkdir(exist_ok=True)

    # Generate base filename (remove .md extension)
    base_name = kb_path.stem

    # Create individual note files
    created_files = []
    for i, note in enumerate(notes, start=1):
        output_filename = f"{base_name}_{i}.md"
        output_path = kb2_dir / output_filename

        # Create file content with source attribution
        file_content = f"**Source:** `{source}`\n\n{note}\n"

        output_path.write_text(file_content, encoding='utf-8')
        created_files.append(output_filename)

    # Report results
    print(f"\n✓ Successfully split {filename} into {len(notes)} individual notes")
    print(f"✓ Created files in kb2/ directory")
    print(f"\nFirst 5 files:")
    for i, fname in enumerate(created_files[:5], 1):
        print(f"  {i}. {fname}")
    if len(created_files) > 5:
        print(f"  ... and {len(created_files) - 5} more")

    return created_files


def main():
    """Main entry point for the script."""

    if len(sys.argv) < 2:
        print("Usage: python split_kb_notes.py <filename>")
        print("\nExample:")
        print('  python split_kb_notes.py "McKinsey - what is generative ai.md"')
        print('  python split_kb_notes.py JaggedFrontier.md')
        print("\nAvailable files in kb/:")
        kb_dir = Path('kb')
        if kb_dir.exists():
            for f in sorted(kb_dir.glob('*.md')):
                print(f"  - {f.name}")
        else:
            print("  (kb/ directory not found)")
        sys.exit(1)

    filename = sys.argv[1]

    # Add .md extension if not provided
    if not filename.endswith('.md'):
        filename = filename + '.md'

    split_kb_notes(filename)


if __name__ == "__main__":
    main()
