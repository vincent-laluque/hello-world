
import html, subprocess, pathlib

src = pathlib.Path("related_lst.php")          # à adapter
code = src.read_text(encoding="utf-8")

# Police identique à celle de Sublime Text (adapter le nom exact)
font = "Fira Code"   # ou "Menlo", "Consolas"…
font = "Anonymous Pro"

page = f"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8">
<style>
  body {{ margin: 2cm; }}
  pre {{
    font-family: "{font}", monospace;
    font-size: 11pt;
    white-space: pre-wrap;
    word-wrap: break-word;
  }}
</style></head><body>
<pre>{html.escape(code)}</pre>
</body></html>"""

out = pathlib.Path("impression.html")
out.write_text(page, encoding="utf-8")
subprocess.run(["open", str(out)])   # ouvre dans le navigateur par défaut