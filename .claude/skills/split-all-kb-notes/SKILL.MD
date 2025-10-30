---
name: split-all-kb-notes
description: splits all knowledge base markdown files in the kb directory into individual note files
---
# Split All KB Notes Skill

Process all knowledge base markdown files in the `kb/` directory and split each one into individual note files.

This skill automatically discovers all `.md` files in the `kb/` directory and applies the splitting logic to each file, creating individual notes in the `kb2/` directory.

## Usage

Simply invoke the skill:
```
/split-all-kb-notes
```

Claude will:
1. Find all `.md` files in the `kb/` directory
2. Process each file using the split-kb-note logic
3. Create individual note files in the `kb2/` directory
4. Provide a summary of files processed

## Output

- Individual note files are created in `kb2/` directory
- Each file is named with the pattern: `{source-name}_{number}.md`
- Progress is reported for each file processed

For detailed instructions, see [reference.md](reference.md).
