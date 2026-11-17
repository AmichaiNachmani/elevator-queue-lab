"""Build index.html for GitHub Pages from the Queue Lab page in the FaceRecognition project.

The source page has no <!doctype>/<html>/<head> wrapper (claude.ai adds one when it is published there);
GitHub Pages serves files as they are, so this adds the wrapper.

    python build.py [path/to/elevator-queue-lab.html]
"""

from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_SOURCE = HERE.parent / "FaceRecognition" / "web" / "elevator-queue-lab.html"

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<style>body { margin: 0; }</style>
</head>
<body>
"""
TAIL = "\n</body>\n</html>\n"


def main() -> None:
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SOURCE
    page = source.read_text(encoding="utf-8").strip()
    if page.lower().startswith("<!doctype"):
        raise SystemExit(f"{source} already has a document wrapper; copy it as index.html instead")
    (HERE / "index.html").write_text(HEAD + page + TAIL, encoding="utf-8", newline="\n")
    print(f"index.html built from {source}")


if __name__ == "__main__":
    main()
