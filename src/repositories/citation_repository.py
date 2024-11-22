from sqlalchemy import text
from config import db

from entities.citation import Citation


def get_citations():
    sql = """ SELECT c.*
                FROM citations c
                LEFT JOIN authors a ON c.id = a.citation_id
                WHERE a.id IS NULL
                ORDER BY c.id
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
            (title, key,  year, type, doi, pages, volume, publisher, tags, citation_url, timestamp) 
            VALUES 
            (:title, :key, :year, :type, :doi, :pages, :volume, :publisher, :tags, :citation_url, CURRENT_TIMESTAMP)"""
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
            "citation_url": data["citation_url"],
        },
    )

    db.session.commit()
