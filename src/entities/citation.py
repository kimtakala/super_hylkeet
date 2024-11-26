from db_helper import COLUMN_NAMES
from repositories import authors_repository


class Citation:
    def __init__(self, data):
        # the code below filter the data from the db.
        # it deletes all the key that have no value assosiated with them
        self._data = {}
        for i, value in enumerate(data):
            if value:
                self._data[COLUMN_NAMES[i]] = value

    @property
    def id(self):
        return self._data["id"]

    @property
    def authors(self):
        return self._data["authors"]

    def __str__(self):
        return str(self._data)

    def get_entrys(self):
        return self._data.keys()

    def get_title(self):
        return self._data["title"]

    def get_year(self):
        return self._data["year"]

    def add_authors(self, authors):
        self._data["authors"] = authors

    def get_datalines(self):
        # This funktion returns all relevant datafields. Not including the title.
        new_dict = self._data
        # Removing not essential field form the dictinary
        new_dict.pop("title", None)
        new_dict.pop("id", None)
        new_dict.pop("timestamp", None)

        # Returning a list of keys and values
        return list((k, v) for k, v in new_dict.items())

    def get_authors_for_listing(self):
        authors = authors_repository.get_authors_for_citation_listing(self._data["id"])
        return authors
