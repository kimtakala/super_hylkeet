from db_helper import COLUMN_NAMES


class Citation:
    def __init__(self, data):
        # the code below filter the data from the db.
        # it deletes all the key that have no value assosiated with them
        self._data = {}
        for i, value in enumerate(data):
            if value:
                self._data[COLUMN_NAMES[i]] = value

    @property
    def all_data(self):
        return self._data

    @property
    def id(self):
        return self._data["id"]

    def get_title(self):
        if "title" not in self._data:
            return "No Title"
        return self._data["title"]

    def get_year(self):
        if "year" not in self._data:
            return "No Year"
        return self._data["year"]

    def add_authors(self, authors):
        self._data["authors"] = authors

    def get_datalines(self):
        # This function returns all relevant datafields. Not including the title.
        new_dict = self._data
        # Removing not essential field form the dictinary
        # Basicly these field are not shown in the fronend dropdown.
        new_dict.pop("id", None)
        new_dict.pop("timestamp", None)

        # Returning a list of keys and values
        return list((k, v) for k, v in new_dict.items())

    def get_authors_for_listing(self):
        firts_name, last_name = self._data["authors"].split(", ")[0].split(" ")
        return f"{firts_name[0]}. {last_name}"
