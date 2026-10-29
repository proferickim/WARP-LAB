"""Export the built site with relative file links for a server-free preview."""
from pathlib import Path
from urllib.parse import urlsplit, unquote
import os
import re
import shutil
import sys
import json

root = Path(__file__).resolve().parents[1]
site = root / "_site"
baseurl = json.loads(re.search(r'^baseurl:\s*(.+)$', (root / '_config.yml').read_text(), re.M)[1]).rstrip('/')
destination = Path(sys.argv[1]).resolve()
if not (site / "index.html").exists():
    raise SystemExit("Build the site first.")
if destination.exists():
    raise SystemExit("Choose a new output directory; existing previews are preserved.")
shutil.copytree(site, destination)

def local_file(url, current):
    parsed = urlsplit(url)
    if not parsed.path.startswith("/") or parsed.netloc:
        return url
    path = unquote(parsed.path)
    if baseurl and (path == baseurl or path.startswith(baseurl + '/')):
        path = path[len(baseurl):] or '/'
    target = destination / path.lstrip("/")
    if target.is_dir():
        target = target / "index.html"
    elif not target.exists() and Path(str(target) + ".html").exists():
        target = Path(str(target) + ".html")
    relative = os.path.relpath(target, current.parent)
    return relative + ("?" + parsed.query if parsed.query else "") + ("#" + parsed.fragment if parsed.fragment else "")

for file in destination.rglob("*.html"):
    source = file.read_text()
    source = re.sub(r'(\b(?:href|src)=")(/[^"\s]*)"', lambda m: m[1] + local_file(m[2], file) + '"', source)
    file.write_text(source)
print(destination / "index.html")
