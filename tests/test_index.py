import unittest
from html.parser import HTMLParser
from pathlib import Path


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.fragments = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("href", "").startswith("#"):
            self.fragments.append(attrs["href"][1:])


class TestIndex(unittest.TestCase):
    def test_contact_link_has_destination(self):
        page = Path(__file__).resolve().parents[1] / "index.html"
        parser = PageParser()
        parser.feed(page.read_text(encoding="utf-8"))
        parser.close()
        self.assertIn("lien-he", parser.fragments)
        for fragment in parser.fragments:
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, parser.ids)


if __name__ == "__main__":
    unittest.main()
