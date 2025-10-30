
## Task

The user will provide a filename from the `kb/` directory. You need to:

1. Read the specified file from the `kb/` directory
2. Extract the source name from the header (the line that starts with `**Source:**`)
3. Remove the entire header section (everything before the first `---` separator after the header)
4. Split the remaining content into individual notes (separated by `---`)
5. Create the `kb2/` directory if it doesn't exist
6. For each note, create a separate file in `kb2/` with:
   - Filename format: `{source-name}_{sequential-id}.md`
     - `{source-name}` = sanitized version of the original filename (remove .md extension, replace spaces with hyphens)
     - `{sequential-id}` = sequential number starting from 1
   - File content:
     - Source attribution (from original header)
     - The individual note content

## Instructions for Claude

1. **If user hasn't specified a file, list available files:**
   ```bash
   ls -1 kb/*.md | head -20
   ```
   Ask the user which file they want to process.

2. **Run the helper script:**
   ```bash
   python scripts/split_kb_notes.py "filename.md"
   ```

   The script will automatically:
   - Read the file from `kb/` directory
   - Extract source and parse notes
   - Create `kb2/` directory
   - Generate individual note files
   - Report results

3. **Show the script output to the user**

## Example

Input file: `kb/what-every-ceo-should-know-about-generative-ai.md`

Output files in `kb2/`:
- `what-every-ceo-should-know-about-generative-ai_1.md`
- `what-every-ceo-should-know-about-generative-ai_2.md`
- `what-every-ceo-should-know-about-generative-ai_3.md`
- ... etc

Each file contains:
```markdown
**Source:** `what-every-ceo-should-know-about-generative-ai`

**Key Finding: AI Boosts Productivity**
Companies using AI see 40% productivity gains in key workflows.
---
```

## Important Notes

- Sequential IDs are global and start from 1 for each run
- Sanitize filenames by replacing spaces and special characters with hyphens or underscores
- Strip leading/trailing whitespace from notes
- Skip empty notes (notes that are just whitespace)
