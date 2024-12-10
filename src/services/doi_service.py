import requests


class DoiService:
    def __init__(self):
        self._base_url = "https://api.crossref.org/works/"

    def get_citation_data_from_doi(self, doi: str):
        request_url = self._base_url + doi
        print(request_url)
        response = requests.get(request_url, timeout=100).json()
        data = response["message"]
        # field are type (response field, our field)
        fields = [("publisher", "publisher"),
                  ("DOI", "doi"),
                  ("date.parts[0]", "year"),
                  ("page", "page"),
                  ("title", "title"),
                  ]

        citation_data = {
            "type": data["type"],
            "publisher": data["publisher"],
            "doi": data["DOI"],
            "year": data["created"]["date-parts"][0][0],
            "page": data["page"]
        }
        citation_data["authors"] = []
        for author in data["author"]:

            # "journal": data["journal-title"][0]}
        print(citation_data)
        return data


if __name__ == "__main__":
    d = DoiService()
    d.get_citation_data_from_doi("10.1016/j.jinf.2017.06.002")
    d.get_citation_data_from_doi("10.1007/978-3-319-46547-0_16")
