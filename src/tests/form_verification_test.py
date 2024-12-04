import unittest
import form_verification


class TestFormVerification(unittest.TestCase):
    def assert_first_is_none_others_is_not_none(self, test_cases, function):
        for i, case in enumerate(test_cases):
            msg = function(case)

            if i == 0:
                self.assertIsNone(msg)
            else:
                self.assertIsNotNone(msg)

    def test_author(self):
        authors = ["Make Mukava, Maijja Junnila",
                   "Porkkana, Porkkana  p"]

        self.assert_first_is_none_others_is_not_none(
            authors, form_verification.verify_author)

    def test_long_author(self):
        authors = ["Make Mukava, Maijja Junnila",
                   "Porkkana" * 100]

        self.assert_first_is_none_others_is_not_none(
            authors, form_verification.verify_author)

    def test_title(self):
        titles = ["Satsuma", "Omena" * 100]

        self.assert_first_is_none_others_is_not_none(
            titles, form_verification.verify_title)

    def test_booktitle(self):
        titles = ["Konkeli", "Mankeli" * 100]

        self.assert_first_is_none_others_is_not_none(
            titles, form_verification.verify_booktitle)

    def test_journal(self):
        journals = ["Kakku", "Kukka" * 100]

        self.assert_first_is_none_others_is_not_none(
            journals, form_verification.verify_journal)

    def test_publisher(self):
        publishers = ["Verna", "Gabriel" * 100]

        self.assert_first_is_none_others_is_not_none(
            publishers, form_verification.verify_publisher)

    def test_pages(self):
        pages = ["1", "9" * 100]

        self.assert_first_is_none_others_is_not_none(
            pages, form_verification.verify_pages)

    def test_year(self):
        years = ["2024", "-3", "12345"]

        self.assert_first_is_none_others_is_not_none(
            years, form_verification.verify_year)

    def test_volume(self):
        volumes = ["101", "blaablaa" * 100]

        self.assert_first_is_none_others_is_not_none(
            volumes, form_verification.verify_volume)

    def test_validate_citations_all_ok(self):
        citation = {
            "title": "Test title",
            "type": "misc",
            "authors": "Make Mukava, Maijja Junnila",
            "year": "2024",
            "publisher": "Test publisher",
            "doi": "Test doi",
            "tags": "Test tags",
            "booktitle": "test booktitle",
            "url": "Test url",
            "timestamp": "2024-11-19"
        }
        self.assertDictEqual(
            {}, form_verification.validate_citations(citation))

    def test_validate_citations_authors_broken(self):
        citation = {
            "title": "Test title",
            "type": "misc",
            "authors": "Make Mukava, Maijja Junnila" * 100,
            "year": "2024",
            "publisher": "Test publisher",
            "doi": "Test doi",
            "tags": "Test tags",
            "booktitle": "test booktitle",
            "url": "Test url",
            "timestamp": "2024-11-19"
        }
        self.assertDictEqual(
            {'authors': 'Authors field must include less than 200 characters'}, form_verification.validate_citations(citation))

    def test_validate_citations_missing_required_fields_book(self):
        citation = {
            "title": "",
            "type": "book",
            "authors": "",
            "year": "",
            "publisher": "",
            "doi": "Test doi",
            "tags": "Test tags",
            "booktitle": "test booktitle",
        }
        self.assertDictEqual(
            {'authors': 'Authors is a required field', 'title': 'Title is a required field', "publisher": 'Publisher is a required field', "year": 'Year is a required field'}, form_verification.validate_citations(citation))

    def test_validate_citations_missing_required_fields_book(self):
        citation = {
            "title": "",
            "type": "inproceedings",
            "authors": "",
            "year": "",
            "publisher": "",
            "doi": "Test doi",
            "tags": "Test tags",
            "booktitle": "",
        }
        self.assertDictEqual(
            {'booktitle': 'Booktitle is a required field', 'authors': 'Authors is a required field', 'title': 'Title is a required field', "year": 'Year is a required field'}, form_verification.validate_citations(citation))
