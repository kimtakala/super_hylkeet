from sqlalchemy import text
from config import db

from entities.citation import Citation


def get_citations():
    sql = """ SELECT citations.* FROM citations 
                LEFT JOIN authors ON citations.id = authors.citation_id 
                WHERE authors.main_author = true 
                ORDER BY authors.last_name ASC
            """
    result = db.session.execute(text(sql))
    citations = result.fetchall()

    return [Citation(data) for data in citations]


def get_citation_by_title(title):
    sql = "SELECT * FROM citations WHERE title = :title"
    result = db.session.execute(text(sql), {"title": title})
    citation = Citation(result.fetchone())
    return citation


def add_citation(data):
    sql = text(
        """INSERT INTO citations 
            (title, key,  year, type, doi, pages, volume, publisher, tags, booktitle, citation_url, timestamp) 
            VALUES 
            (:title, :key, :year, :type, :doi, :pages, :volume, :publisher, :tags, :booktitle, :citation_url, CURRENT_TIMESTAMP)"""
    )
    db.session.execute(
        sql,
        {
            "title": data["title"],
            "key": data["key"],
            "year": data["year"],
            "type": data["doi"],
            "doi": data["doi"],
            "pages": data["pages"],
            "volume": data["volume"],
            "publisher": data["publisher"],
            "tags": data["tags"],
            "booktitle": data["booktitle"],
            "citation_url": data["citation_url"],
        },
    )

    db.session.commit()
