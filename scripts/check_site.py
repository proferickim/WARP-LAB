"""Check the actual Jekyll output for broken local links and migration loss."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import sys
import re

ROOT = Path(__file__).resolve().parents[1]
SITE = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / "_site"
BASEURL = json.loads(re.search(r'^baseurl:\s*(.+)$', (ROOT / '_config.yml').read_text(), re.M)[1]).rstrip('/')

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
        self.ids = set()
        self.headings = 0
        self.missing_alt = 0
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "h1":
            self.headings += 1
        if tag == "img" and "alt" not in attrs:
            self.missing_alt += 1
        for attribute in ("href", "src"):
            if attrs.get(attribute) and not (tag == "link" and attrs.get("rel") == "canonical"):
                self.urls.append(attrs[attribute])

def resolve(path):
    path = Path(path)
    for candidate in (path, path / "index.html", Path(str(path) + ".html")):
        if candidate.is_file():
            return candidate
    return None

pages = {}
errors = []
for file in SITE.rglob("*.html"):
    page = Page()
    page.feed(file.read_text())
    pages[file] = page
    if page.missing_alt:
        errors.append(f"Image without alt text: {file.relative_to(SITE)}")
    if page.headings != 1 and "http-equiv=\"refresh\"" not in file.read_text():
        errors.append(f"Expected one H1: {file.relative_to(SITE)}")

checked = 0
for file, page in pages.items():
    for url in page.urls:
        parsed = urlsplit(url)
        if parsed.scheme or parsed.netloc:
            continue
        local_path = unquote(parsed.path)
        if BASEURL and (local_path == BASEURL or local_path.startswith(BASEURL + '/')):
            local_path = local_path[len(BASEURL):] or '/'
        target = resolve(SITE / local_path.lstrip("/")) if local_path.startswith("/") else resolve(file.parent / local_path) if local_path else file
        if not target:
            errors.append(f"Missing target {url} in {file.relative_to(SITE)}")
        elif parsed.fragment and target in pages and unquote(parsed.fragment) not in pages[target].ids:
            errors.append(f"Missing anchor {url} in {file.relative_to(SITE)}")
        checked += 1

expected = ("commag25", "globecom23", "iotj25", "pieee24", "RIS_TVT", "twc25", "wcl26", "wcm25")
for slug in expected:
    if not resolve(SITE / "publication" / slug):
        errors.append(f"Missing migrated publication: {slug}")
for token in ("Room 411", "Room 303", "eric_kim@dankook.ac.kr"):
    if token not in (SITE / "join/index.html").read_text():
        errors.append(f"Missing contact detail: {token}")

print(json.dumps({"html_pages": len(pages), "local_links_and_assets": checked, "migrated_publications": len(expected), "errors": errors}, indent=2))
raise SystemExit(bool(errors))

