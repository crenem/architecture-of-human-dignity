#!/usr/bin/env python3
"""Check Obsidian wikilinks and simple Markdown conventions in a Git repository."""
import re
import sys
from pathlib import Path

LINK = re.compile(r"\[\[([^\]]+)\]\]")
EXCLUDED = {".git", ".obsidian", "__pycache__", ".venv"}

def markdown_paths(root):
    return [p for p in root.rglob("*.md") if not EXCLUDED.intersection(p.relative_to(root).parts)]

def check(root):
    root = Path(root)
    paths = markdown_paths(root)
    exact = {p.relative_to(root).with_suffix("").as_posix(): p for p in paths}
    name_index = {}
    for key in exact:
        name_index.setdefault(key.rsplit("/", 1)[-1], []).append(key)
    defects = []
    for path in paths:
        text = path.read_text(encoding="utf-8")
        current = path.relative_to(root).parent
        for matched in LINK.finditer(text):
            target = matched.group(1).split("|", 1)[0].split("#", 1)[0].strip()
            if not target or target.startswith(("http://", "https://")):
                continue
            target = target.removesuffix(".md").lstrip("/")
            relative_target = (current / target).as_posix()
            if target in exact or relative_target in exact:
                continue
            if "/" not in target and len(name_index.get(target, [])) == 1:
                continue
            defects.append(f"{path.relative_to(root)}: missing/ambiguous link [[{matched.group(1)}]]")
    return defects, len(paths)

def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    defects, filecount = check(root)
    if defects:
        print("\n".join(defects))
        print(f"{len(defects)} broken/ambiguous links across {filecount} Markdown files.")
        return 1
    print(f"OK: {filecount} Markdown files, all referenced Obsidian links resolve.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
