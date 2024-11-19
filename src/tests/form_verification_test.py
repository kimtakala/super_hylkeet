import unittest
import form_verification

class TestFormVerification(unittest.TestCase):

    # ------- Tests that deal with input text length -------

    def text_length_verification(self, function):
        test_text = ["Kissa", "X", "Koira" * 100]

        for i, text in enumerate(test_text):
            msg = function(text)

            if i == 0:
                self.assertIsNone(msg)
            else:
                self.assertIsNotNone(msg)


    def test_author(self):
        self.text_length_verification(form_verification.verify_author)


    def test_title(self):
        self.text_length_verification(form_verification.verify_title)

    
    def test_booktitle(self):
        self.text_length_verification(form_verification.verify_booktitle)


    def test_journal(self):
        self.text_length_verification(form_verification.verify_journal)


    def test_publisher(self):
        self.text_length_verification(form_verification.verify_publisher)


    def test_pages(self):
        self.text_length_verification(form_verification.verify_pages)


    # ------- Other tests -------


    def test_year(self):
        years = [2024, -1, 12345, "2024"]

        for i, year in enumerate(years):
            msg = form_verification.verify_year(year)

            if i == 0:
                self.assertIsNone(msg)
            else:
                self.assertIsNotNone(msg)


    def test_volume(self):
        volumes = [123, -5, "10"]

        for i, volume in enumerate(volumes):
            msg = form_verification.verify_volume(volume)

            if i == 0:
                self.assertIsNone(msg)
            else:
                self.assertIsNotNone(msg)
