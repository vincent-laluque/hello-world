#!/usr/bin/env python3
import html
import pathlib
import subprocess
import sys

# ---- réglages ----
FONT = "Fira Code"   # <-- mets ici le nom exact de ton font_face
SIZE = "11pt"
# ------------------

def main():
    if len(sys.argv) < 2:
        print("Usage: sublime_print.py <fichier>")
        sys.exit(1)

    src = pathlib.Path(sys.argv[1])
    if not src.exists():
        print(f"Fichier introuvable : {src}")
        sys.exit(1)

    code = src.read_text(encoding="utf-8", errors="replace")

    page = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>{html.escape(src.name)}</title>
<style>
  @page {{ margin: 1.8cm; }}
  body {{ margin: 0; }}
  pre {{
    font-family: "{FONT}", "Menlo", monospace;
    font-size: {SIZE};
    line-height: 1.35;
    white-space: pre-wrap;
    word-wrap: break-word;
  }}
</style>
</head>
<body>
<pre>{html.escape(code)}</pre>
</body>
</html>
"""

    out = pathlib.Path.home() / "impression_sublime.html"
    out.write_text(page, encoding="utf-8")
    subprocess.run(["open", str(out)])

if __name__ == "__main__":
    main()