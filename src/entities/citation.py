from db_helper import COLUMN_NAMES


class Citation:
    def __init__(self, data):
        # the code below filter the data from the db.
        # it deletes all the key that have no value assosiated with them
        self._data = {}
        for i, value in enumerate(data):
            if value:
                self._data[COLUMN_NAMES[i]] = value

    def __str__(self):
        return str(self._data)

    def get_entrys(self):
        return self._data.keys()

    def get_title(self):
        return self._data["title"]

    def get_datalines(self):
        # This funktion returns all relevant datafields. Not including the title.
        new_dict = self._data
        new_dict.pop("title", None)
        new_dict.pop("id", None)
        new_dict.pop("timestamp", None)
        return list((k, v) for k, v in new_dict.items())
