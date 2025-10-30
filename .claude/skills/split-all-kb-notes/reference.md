# Split All KB Notes - Reference for Claude

## Task

Process all markdown files in the `kb/` directory and split each one into individual note files in the `kb2/` directory.

## Instructions for Claude

When this skill is invoked, follow these steps:

### Step 1: Discover all markdown files

Use the Bash tool to list all `.md` files in the `kb/` directory:

```bash
ls -1 kb/*.md
```

This will output a list of files like:
```
kb/file1.md
kb/file2.md
kb/securing-ai.md
```

### Step 2: Process each file

For each file discovered in Step 1, run the split-kb-note script using the Bash tool:

```bash
python .claude/skills/split-kb-note/scripts/split_kb_notes.py "basename-of-file.md"
```

**Important:** Extract just the basename (filename without path) from each full path before passing to the script.

For example:
- If you found `kb/securing-ai.md`, run: `python .claude/skills/split-kb-note/scripts/split_kb_notes.py "securing-ai.md"`
- If you found `kb/another-file.md`, run: `python .claude/skills/split-kb-note/scripts/split_kb_notes.py "another-file.md"`

### Step 3: Report results

After processing all files, provide a summary to the user:
- Total number of files processed
- Total number of individual notes created
- Location of output files (`kb2/` directory)

## Example Execution

If the `kb/` directory contains 3 files:
- `kb/securing-ai.md` (50 notes)
- `kb/research-report.md` (30 notes)
- `kb/best-practices.md` (25 notes)

You would:
1. Run the split script for each file (3 times total)
2. Report: "Processed 3 files, created 105 individual notes in kb2/ directory"

## Important Notes

- The script expects just the filename (e.g., `"securing-ai.md"`), not the full path
- The script automatically reads from `kb/` directory and writes to `kb2/` directory
- If `kb2/` directory doesn't exist, the script will create it
- Each file's notes are numbered sequentially (e.g., `securing-ai_1.md`, `securing-ai_2.md`, etc.)
- If there are no `.md` files in `kb/`, inform the user that no files were found to process
