from repositories.citation_repository import add_citation, get_citations, get_citation_by_title
from repositories.authors_repository import add_author_by_citation_id, get_authors_by_citation_id

from hprint import hprint


class CitationService:
    def __init__(self):
        pass

    def add_citation(self, data):
        # data[authors] is in string format as ¨firstname lastname, firstname lastname¨
        authors = data["authors"].split(", ")

        # Adding the citation to the db so that it can generate id for the authors table reference.
        add_citation(data)
        citations_id = get_citation_by_title(data["title"]).id

        for i, author in enumerate(authors):
            add_author_by_citation_id(citations_id, author, i == 0)

    def get_citations(self):
        citations = get_citations()
        for citation in citations:
            authors = get_authors_by_citation_id(citation.id)
            # parsin the author data to firstname lastname, firstname lastname format
            author_string = ", ".join([f"{a[0]} {a[1]}" for a in authors])
            citation.add_authors(author_string)
        return citations


citation_service = CitationService()
