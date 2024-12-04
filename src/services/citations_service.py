from repositories.citation_repository import (
    add_citation,
    get_citations,
    search_citations,
    get_citation_by_title,
    delete_by_id,
    get_citations_by_ids
)
from repositories.authors_repository import (
    add_author_by_citation_id,
    get_authors_by_citation_id,
)
from config import db
from db_helper import COLUMN_NAMES

from hprint import hprint


class CitationService:
    def __init__(self):
        pass

    def add_citation(self, data):
        # data[authors] is in string format as ¨firstname lastname, firstname lastname¨
        if data["authors"] != "":
            authors = data["authors"].split(", ")
        else:
            authors = ["No author"]

        # Adding the citation to the db so that
        # it can generate id for the authors table reference.
        add_citation(data)
        citations_id = get_citation_by_title(data["title"]).id

        for i, author in enumerate(authors):
            add_author_by_citation_id(citations_id, author, i == 0)

        # DB commit here so that if one of the add functions throws error,
        # the others wont be commited.
        db.session.commit()

    def fetch_citations(self, search_key=""):  # changed name to be unique
        if search_key == "":
            citations = get_citations()
        else:
            citations = search_citations(search_key)

        for citation in citations:
            authors = get_authors_by_citation_id(citation.id)
            # parsin the author data to firstname lastname, firstname lastname format
            author_string = ", ".join([f"{a[0]} {a[1]}" for a in authors])
            citation.add_authors(author_string)
        return citations

    def delete_citation_by_id(self, id):
        delete_by_id(id)

    def fill_data_with_nones(self, data):
        data = data.to_dict()
        required_fields = list(COLUMN_NAMES)
        required_fields.remove("id")
        required_fields.remove("timestamp")
        hprint(required_fields)
        for field in required_fields:
            if field not in data:
                data[field] = ""
        return data

    def get_citations_for_bibtex(self, citation_ids):
        citations = get_citations_by_ids(citation_ids)
        for citation in citations:
            authors = get_authors_by_citation_id(citation.id)
            # parsin the author data to firstname lastname, firstname lastname format
            author_string = ", ".join([f"{a[0]} {a[1]}" for a in authors])
            citation.add_authors(author_string)
        return citations


citation_service = CitationService()
