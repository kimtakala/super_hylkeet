import requests


class DoiService:
    def __init__(self):
        self._base_url = "https://api.crossref.org/works/"
        self.data = {}

    def get_citation_data_from_doi(self, doi: str):

        self._load_data_from_api(doi)

        citation_data = self.parse_data_to_dict()

        return citation_data

    def parse_data_to_dict(self):
        # field are type (response field, our field)
        direct_keys = {"type": "type",
                       "publisher": "publisher",
                       "pages": "page",
                       "doi": "DOI",
                       "volume": "volume"}

        citation_data = {}

        for k, v in direct_keys.items():
            citation_data[k] = self._if_exisists_return(v)

        citation_data["year"] = self.data["created"]["date-parts"][0][0]
        citation_data["title"] = self.data["title"][0]

        if "journal" in self.data:
            citation_data["journal"]: self.data["journal-title"][0]

        citation_data["authors"] = self._author_parser()

        return citation_data

    def _load_data_from_api(self, doi):
        request_url = self._base_url + doi
        response = requests.get(request_url, timeout=100).json()
        self.data = response["message"]

    def _author_parser(self):
        author_string = ""

        for author in self.data["author"]:
            first_name = author["given"].split(" ")[0]
            last_name = author["family"]
            author_string += first_name + " " + last_name + ", "

        return author_string[:-2]

    def _if_exisists_return(self, key):
        if key in self.data.keys():
            return self.data[key]
        return ""


doi_service = DoiService()
