from repositories.citation_repository import add_citation, get_citations, get_citation_by_title
from repositories.authors_repository import add_author_by_citation_id, get_authors_by_citation_id


class CitationService:
    def __init__(self):
        pass

    def add_citation(self, data):
        authors = data["authors"].split(",")
        add_citation(data)
        citations_id = get_citation_by_title(data["title"]).id

        for author in authors:
            add_author_by_citation_id(citations_id, author)

    def get_citations(self):
        citations = get_citations()
        for citation in citations:
            authors = get_authors_by_citation_id(citation.id)
            author_string = ", ".join(authors)
            citation.add_authors(author_string)
        return citations


citation_service = CitationService()
