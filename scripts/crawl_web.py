"""Quét website letsdoitvietnam.org và lưu dữ liệu SEO + bài viết ra CSV.

Chạy: python scripts/crawl_web.py
Đầu ra: data/web/pages.csv, data/web/posts.csv
Chỉ dùng thư viện chuẩn của Python.
"""
import csv
import html as htmllib
import json
import re
import time
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse

SITE = "https://letsdoitvietnam.org"
OUT = Path(__file__).resolve().parent.parent / "data" / "web"
UA = {"User-Agent": "letdivn-ai-agent/1.0 (student project)"}


def fetch(url):
    start = time.time()
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        body = r.read().decode("utf-8", "replace")
        return r.status, body, round((time.time() - start) * 1000)


def sitemap_urls():
    _, index, _ = fetch(SITE + "/wp-sitemap.xml")
    urls = []
    for sm in re.findall(r"<loc>(.*?)</loc>", index):
        if "taxonomies" in sm:
            continue
        _, xml, _ = fetch(sm)
        urls += re.findall(r"<loc>(.*?)</loc>", xml)
    return urls


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.meta = {}
        self.canonical = ""
        self.lang = ""
        self.h1 = []
        self.h2 = 0
        self.images = 0
        self.images_no_alt = 0
        self.links = []
        self.jsonld = []
        self.text = []
        self._in = None
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.lang = a.get("lang", "")
        elif tag == "title":
            self._in = "title"
        elif tag == "meta":
            key = a.get("name") or a.get("property")
            if key:
                self.meta[key.lower()] = a.get("content", "")
        elif tag == "link" and a.get("rel") == "canonical":
            self.canonical = a.get("href", "")
        elif tag == "h1":
            self._in = "h1"
            self.h1.append("")
        elif tag == "h2":
            self.h2 += 1
        elif tag == "img":
            self.images += 1
            if not (a.get("alt") or "").strip():
                self.images_no_alt += 1
        elif tag == "a" and a.get("href"):
            self.links.append(a["href"])
        elif tag == "script" and a.get("type") == "application/ld+json":
            self._in = "jsonld"
            self.jsonld.append("")
        elif tag in ("script", "style", "noscript"):
            self._skip += 1

    def handle_endtag(self, tag):
        if tag in ("title", "h1") or (tag == "script" and self._in == "jsonld"):
            self._in = None
        elif tag in ("script", "style", "noscript") and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if self._in == "title":
            self.title += data
        elif self._in == "h1":
            self.h1[-1] += data
        elif self._in == "jsonld":
            self.jsonld[-1] += data
        elif not self._skip:
            self.text.append(data)


def schema_types(blocks):
    types = set()
    for b in blocks:
        try:
            data = json.loads(b)
        except ValueError:
            continue
        items = data.get("@graph", [data]) if isinstance(data, dict) else data
        for it in items:
            t = it.get("@type") if isinstance(it, dict) else None
            if t:
                types.update(t if isinstance(t, list) else [t])
    return "|".join(sorted(types))


def crawl_pages():
    host = urlparse(SITE).netloc
    rows = []
    for url in sitemap_urls():
        try:
            status, html, ms = fetch(url)
        except Exception as e:  # trang lỗi vẫn ghi lại để audit
            rows.append({"url": url, "status": str(e)[:60]})
            continue
        p = PageParser()
        p.feed(html)
        internal = {urljoin(url, l).split("#")[0] for l in p.links
                    if urlparse(urljoin(url, l)).netloc == host}
        words = len(" ".join(p.text).split())
        desc = p.meta.get("description", "")
        rows.append({
            "url": url,
            "status": status,
            "load_ms": ms,
            "lang": p.lang,
            "title": p.title.strip(),
            "title_len": len(p.title.strip()),
            "meta_description": desc,
            "desc_len": len(desc),
            "h1_count": len(p.h1),
            "h1": " | ".join(h.strip() for h in p.h1),
            "h2_count": p.h2,
            "word_count": words,
            "images": p.images,
            "images_no_alt": p.images_no_alt,
            "internal_links": len(internal),
            "canonical": p.canonical,
            "og_image": "yes" if p.meta.get("og:image") else "no",
            "schema_types": schema_types(p.jsonld),
        })
        time.sleep(0.5)
    return rows


def fetch_posts():
    rows, page = [], 1
    while True:
        url = f"{SITE}/wp-json/wp/v2/posts?per_page=100&page={page}&_embed=wp:term"
        try:
            _, body, _ = fetch(url)
        except Exception:
            break
        posts = json.loads(body)
        if not posts:
            break
        for p in posts:
            terms = p.get("_embedded", {}).get("wp:term", [])
            cats = [t["name"] for group in terms for t in group if t.get("taxonomy") == "category"]
            text = re.sub(r"<[^>]+>", " ", p["content"]["rendered"])
            rows.append({
                "date": p["date"][:10],
                "title": htmllib.unescape(re.sub(r"<[^>]+>", "", p["title"]["rendered"])),
                "url": p["link"],
                "slug": p["slug"],
                "categories": "|".join(cats),
                "word_count": len(text.split()),
            })
        if len(posts) < 100:
            break
        page += 1
    return rows


def save(name, rows):
    if not rows:
        print(f"{name}: không có dữ liệu")
        return
    keys = list(dict.fromkeys(k for r in rows for k in r))
    with open(OUT / name, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        w.writerows(rows)
    print(f"{name}: {len(rows)} dòng")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    save("pages.csv", crawl_pages())
    save("posts.csv", fetch_posts())
