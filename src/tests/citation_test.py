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


class TestCitation(unittest.TestCase):
    def setUp(self):
        self.stub = CitationStub()
        self.citation = Citation(self.stub.get_citation())

    def test_get_title(self):
        title = self.citation.get_title()
        print(title)
        self.assertEqual(title, "Test title")

    def test_get_entrys(self):
        self.assertListEqual(
            list(self.citation.get_entrys()), COLUMN_NAMES)

    def test_get_datalines(self):
        data = self.stub.get_citation()
        expected_datalines = [(COLUMN_NAMES[i], data[i])
                              for i in range(len(COLUMN_NAMES))]

        # Pop fields id, title and timestamp
        expected_datalines.pop(0)
        expected_datalines.pop(2)
        expected_datalines.pop(10)
        expected_dataline.pop(10)

        self.assertEqual(self.citation.get_datalines(), expected_datalines)
