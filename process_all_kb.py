#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path

kb_dir = Path("kb")
script_path = ".claude/skills/split-kb-note/scripts/split_kb_notes.py"

# Get all markdown files
md_files = sorted(kb_dir.glob("*.md"))

print(f"Found {len(md_files)} markdown files to process\n")

total_notes = 0
processed_files = 0

for md_file in md_files:
    filename = md_file.name
    print(f"Processing: {filename}")

    try:
        result = subprocess.run(
            ["python", script_path, filename],
            capture_output=True,
            text=True,
            timeout=60
        )

        # Extract note count from output
        for line in result.stdout.split("\n"):
            if "Found" in line and "notes" in line:
                try:
                    count = int(line.split("Found")[1].split("notes")[0].strip())
                    total_notes += count
                    print(f"  → Created {count} notes")
                except:
                    pass

        if "Successfully split" in result.stdout:
            processed_files += 1
        elif result.stderr:
            print(f"  ERROR: {result.stderr}")

    except Exception as e:
        print(f"  ERROR: {e}")

    print()

print(f"\n{'='*60}")
print(f"SUMMARY")
print(f"{'='*60}")
print(f"Total files processed: {processed_files}/{len(md_files)}")
print(f"Total individual notes created: {total_notes}")
print(f"Output directory: kb2/")
print(f"{'='*60}")
