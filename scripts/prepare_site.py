"""Prepare DITA HTML5 links for a GitHub Pages project site."""

import argparse
from html import escape
from html.parser import HTMLParser
import os
from pathlib import Path
from urllib.parse import unquote, urlsplit


class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.items = []

    def handle_starttag(self, tag, attrs):
        attr_name = {"a": "href", "link": "href", "img": "src", "script": "src"}.get(tag)
        value = dict(attrs).get(attr_name)
        if value:
            self.items.append((tag, attr_name, value, self.get_starttag_text()))


def prepare(root):
    for page in root.rglob("*.html"):
        content = page.read_text(encoding="utf-8")
        parser = References()
        parser.feed(content)
        for tag, attr, value, raw in parser.items:
            parsed = urlsplit(value)
            if parsed.scheme or parsed.netloc:
                continue
            target = None
            if page == root / "index.html" and value.startswith("../topics/"):
                target = value[3:]
            elif tag == "link" and Path(parsed.path).name in ("commonltr.css", "commonrtl.css"):
                target = os.path.relpath(root / Path(parsed.path).name, page.parent).replace(os.sep, "/")
            if target and target != value:
                updated = raw.replace(f'{attr}="{escape(value, quote=True)}"', f'{attr}="{escape(target, quote=True)}"')
                content = content.replace(raw, updated)
        if page == root / "index.html" and 'href="pdf/zhiya-guochuan-agent.pdf"' not in content:
            link = '<p class="shortdesc"><a href="pdf/zhiya-guochuan-agent.pdf">查看 PDF 版本</a></p>'
            content = content.replace("</h1>", "</h1>\n" + link, 1)
        page.write_text(content, encoding="utf-8")


def check(root, require_pdf):
    missing = []
    count = 0
    for page in root.rglob("*.html"):
        count += 1
        parser = References()
        parser.feed(page.read_text(encoding="utf-8"))
        for _, _, value, _ in parser.items:
            parsed = urlsplit(value)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            if not require_pdf and value == "pdf/zhiya-guochuan-agent.pdf":
                continue
            target = (page.parent / unquote(parsed.path)).resolve()
            if not target.is_relative_to(root) or not target.exists():
                missing.append(f"{page.relative_to(root)}: {value}")
    if not count:
        raise SystemExit("No HTML files found.")
    if missing:
        raise SystemExit("Invalid local links:\n" + "\n".join(missing))
    print(f"Checked local links in {count} HTML files.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", type=Path)
    parser.add_argument("--check", action="store_true", help="Check existing output, including the PDF link.")
    args = parser.parse_args()
    root = args.site.resolve()
    if not args.check:
        prepare(root)
    check(root, require_pdf=args.check)


if __name__ == "__main__":
    main()
