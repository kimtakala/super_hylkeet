import unittest
from entities.citation import Citation

COLUMN_NAMES = [
    "id",
    "key",
    "type",
    "title",
    "authors",
    "year",
    "pages",
    "volume",
    "publisher",
    "doi",
    "tags",
    "citation_url",
    "timestamp",
]


class CitationStub:
    def get_citation(self):
        return [
            1,
            "Testkey",
            "article",
            "Test title",
            "Test author",
            2024,
            12,
            22,
            "Test publisher",
            "Test doi",
            "Test tags",
            "Test url",
            "2024-11-19",
        ]


class TestCitation(unittest.TestCase):
    def setUp(self):
        self.stub = CitationStub()
        self.citation = Citation(self.stub.get_citation())

    def test_get_title(self):
        title = self.citation.get_title()
        print(title)
        self.assertEqual(title, "Test title")

    def test_get_entrys(self):
        expected_keys = {
            "id",
            "key",
            "type",
            "title",
            "authors",
            "year",
            "pages",
            "volume",
            "publisher",
            "doi",
            "tags",
            "citation_url",
            "timestamp",
        }
        self.assertSetEqual(set(self.citation.get_entrys()), expected_keys)

    def test_get_datalines(self):
        expected_datalines = [
            ("key", "Testkey"),
            ("type", "article"),
            ("authors", "Test author"),
            ("year", 2024),
            ("pages", 12),
            ("volume", 22),
            ("publisher", "Test publisher"),
            ("doi", "Test doi"),
            ("tags", "Test tags"),
            ("citation_url", "Test url"),
        ]
        self.assertEqual(self.citation.get_datalines(), expected_datalines)
