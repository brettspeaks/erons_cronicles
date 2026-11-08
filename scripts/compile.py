import os
from pathlib import Path

# Define the root of your notes/scenes
DOCS_DIR = Path(".")
OUTPUT_FILE = Path("master-chronicles.md")

# Exclude non-scene folders like .git, scripts, etc.
EXCLUDES = {".git", "scripts", ".github"}

def compile_docs():
    markdown_content = []
    
    # Recursively find all markdown files, sorted alphabetically/chronologically
    for path in sorted(DOCS_DIR.rglob("*.md")):
        if any(exc in path.parts for exc in EXCLUDES):
            continue
        if path == OUTPUT_FILE:
            continue
            
        markdown_content.append(f"\n\n--- \n*Source: {path}*\n\n")
        markdown_content.append(path.read_text(encoding="utf-8"))
        
    OUTPUT_FILE.write_text("".join(markdown_content), encoding="utf-8")
    print(f"Successfully compiled {OUTPUT_FILE}!")

if __name__ == "__main__":
    compile_docs()
    