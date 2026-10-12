"""Validate public page structure and internal navigation without dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids=[]; self.refs=[]; self.headings=[]; self.lang=None; self.canonical=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if tag=='html': self.lang=a.get('lang')
        if tag=='h1': self.headings.append(tag)
        for key in ('href','src'):
            if key in a: self.refs.append(a[key])
        if tag=='link' and a.get('rel')=='canonical': self.canonical.append(a['href'])

pages={}
for file in ROOT.glob('*.html'):
    page=Page(); page.feed(file.read_text()); pages[file.name]=page
    assert page.lang in ('pl','en'), file
    assert len(page.headings)==1, file
    assert len(page.ids)==len(set(page.ids)), file
    assert len(page.canonical)==1, file
    assert 'main' in page.ids, file
for name,page in pages.items():
    for ref in page.refs:
        u=urlsplit(ref)
        if u.scheme or u.netloc: continue
        dest=unquote(u.path) or name
        assert (ROOT/dest).is_file(), (name,ref)
        if u.fragment:
            assert dest in pages and u.fragment in pages[dest].ids,(name,ref)
ET.parse(ROOT/'sitemap.xml')
assert set(pages)=={'index.html','index-pl.html','privacy.html','privacy-en.html','delete-account.html','delete-account-en.html'}
assert pages['privacy.html'].ids == pages['privacy-en.html'].ids
print(f'PASS: {len(pages)} pages, unique headings/IDs, bilingual legal sections, internal files/anchors and sitemap.')
