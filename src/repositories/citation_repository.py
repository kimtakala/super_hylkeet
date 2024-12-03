from sqlalchemy import text
from config import db

from entities.citation import Citation


def get_citations():
    sql = """   SELECT citations.*  FROM citations
                LEFT JOIN authors ON citations.id = authors.citation_id
                WHERE authors.main_author = true
                ORDER BY authors.last_name ASC
            """
    result = db.session.execute(text(sql))
    citations = result.fetchall()

    return [Citation(data) for data in citations]


def search_citations(search_key):
    key = "%"+search_key+"%"
    sql = text("""   SELECT c.*  FROM citations c
                LEFT JOIN authors a ON c.id = a.citation_id
                WHERE a.main_author = true AND (
                    c.title LIKE :search_key OR
                    LOWER(c.tags) LIKE LOWER(:search_key) OR
                    LOWER(c.key) LIKE LOWER(:search_key) OR
                    LOWER(a.first_name) LIKE LOWER(:search_key) OR
                    LOWER(a.last_name) LIKE LOWER(:search_key))
                ORDER BY a.last_name ASC
            """)
    result = db.session.execute(
        sql,
        {
            "search_key": key
        },
    )
    citations = result.fetchall()

    return [Citation(data) for data in citations]


def get_citation_by_title(title):
    sql = "SELECT * FROM citations WHERE title = :title"
    result = db.session.execute(text(sql), {"title": title})
    citation = Citation(result.fetchone())
    return citation

def get_citations_by_ids(ids):
    sql = "SELECT * FROM citations WHERE id = ANY(:ids)"
    result = db.session.execute(text(sql), {"ids": ids})
    citations = [Citation(row) for row in result.fetchall()]
    return citations

def get_citations_by_ids(ids):
    ids = [int(id) for id in ids]
    sql = "SELECT * FROM citations WHERE id = ANY(:ids)"
    result = db.session.execute(text(sql), {"ids": ids})
    citations = [Citation(row) for row in result.fetchall()]
    return citations


def check_if_exists(title):
    try:
        get_citation_by_title(title)
        return True
    except TypeError:
        return False


def add_citation(data):
    if check_if_exists(data["title"]):
        raise ValueError(
            "Entry already added. Can't have two citations with same names."
        )
    sql = text(
        """INSERT INTO citations 
            (title, key,  year, type, doi, pages, volume,
            publisher, tags, booktitle, citation_url, timestamp) 
            VALUES 
            (:title, :key, :year, :type, :doi, :pages, :volume,
            :publisher, :tags, :booktitle, :citation_url, CURRENT_TIMESTAMP)"""
    )
    db.session.execute(
        sql,
        {
            "title": data["title"],
            "key": data["key"],
            "year": data["year"],
            "type": data["type"],
            "doi": data["doi"],
            "pages": data["pages"],
            "volume": data["volume"],
            "publisher": data["publisher"],
            "tags": data["tags"],
            "booktitle": data["booktitle"],
            "citation_url": data["citation_url"],
        },
    )


def delete_by_id(id):
    sql = text("DELETE FROM citations WHERE id = :id")
    db.session.execute(
        sql,
        {"id": id}
    )
    db.session.commit()
