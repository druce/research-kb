#!/usr/bin/env python3
from pathlib import Path

kb2_dir = Path("kb2")
output_file = Path("notes.md")

# Get all markdown files sorted
md_files = sorted(kb2_dir.glob("*.md"))

print(f"Found {len(md_files)} note files to concatenate")

with open(output_file, 'w', encoding='utf-8') as outfile:
    for i, md_file in enumerate(md_files):
        print(f"Processing: {md_file.name}")

        # Read and write the content
        with open(md_file, 'r', encoding='utf-8') as infile:
            content = infile.read()
            outfile.write(content)

        # Add separator between files (but not after the last one)
        if i < len(md_files) - 1:
            outfile.write("\n\n---\n\n")

print(f"\nSuccessfully concatenated {len(md_files)} files into notes.md")
