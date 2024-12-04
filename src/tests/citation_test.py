import unittest
from entities.citation import Citation
from db_helper import COLUMN_NAMES


class CitationStub:
    def get_citation(self):
        return [
            1,
            "Testkey",
            "article",
            "Test title",
            2024,
            12,
            22,
            "Test publisher",
            "Test doi",
            "Test tags",
            "test booktitle",
            "Test url",
            "2024-11-19",
        ]

    def get_misc(self):
        return [
            1,
            "",
            "misc",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "2024-11-19",
        ]


class TestCitation(unittest.TestCase):
    def setUp(self):
        self.stub = CitationStub()
        self.citation = Citation(self.stub.get_citation())
        self.misc = Citation(self.stub.get_misc())

    def test_get_title(self):
        title = self.citation.get_title()
        self.assertEqual(title, "Test title")

    def test_return_data(self):
        data = self.stub.get_citation()
        expected_data = dict([(COLUMN_NAMES[i], data[i])
                              for i in range(len(COLUMN_NAMES))])
        self.assertDictEqual(expected_data, self.citation.all_data)

    def test_correct_id(self):
        self.assertEqual(1, self.citation.id)

    def test_get_title_empty(self):
        title = self.misc.get_title()
        self.assertEqual(title, "No Title")

    def test_get_year(self):
        year = self.citation.get_year()
        self.assertEqual(year, 2024)

    def test_get_year_empty(self):
        year = self.misc.get_year()
        self.assertEqual(year, "No Year")

    def test_add_authors(self):
        authors = ["Author1", "Author2"]
        self.citation.add_authors(authors)
        self.assertEqual(self.citation.all_data["authors"], authors)

    def test_get_authors_for_listing(self):
        authors = ["Author1 Author", "Author2 Author"]
        self.citation.add_authors(", ".join(authors))
        self.assertEqual(self.citation.get_authors_for_listing(), "A. Author")

    def test_datalines_empty_misc(self):
        expected_datalines = [("type", "misc")]
        self.assertEqual(self.misc.get_datalines(), expected_datalines)

    def test_get_datalines(self):
        data = self.stub.get_citation()
        expected_datalines = [(COLUMN_NAMES[i], data[i])
                              for i in range(len(COLUMN_NAMES))]

        # Pop fields id, title and timestamp
        expected_datalines.pop(0)
        expected_datalines.pop(11)

        self.assertEqual(self.citation.get_datalines(), expected_datalines)
