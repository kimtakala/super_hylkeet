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

    def test_get_title_empty(self):
        title = self.misc.get_title()
        self.assertEqual(title, "No Title")

    def test_datalines_empty_misc(self):

    def test_get_datalines(self):
        data = self.stub.get_citation()
        expected_datalines = [(COLUMN_NAMES[i], data[i])
                              for i in range(len(COLUMN_NAMES))]

        # Pop fields id, title and timestamp
        expected_datalines.pop(0)
        expected_datalines.pop(11)

        self.assertEqual(self.citation.get_datalines(), expected_datalines)
