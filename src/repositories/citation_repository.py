from flask import request
from sqlalchemy import text
from config import db


def add_citation():
    data = request.form

    sql = text(
        """INSERT INTO citations 
            (title, authors, key,  year, type, doi, pages, volume, publisher, tags, citation_url) 
            VALUES 
            (:title, :authors, :key, :year, :type, :doi, :pages, :volume, :publisher, :tags, citation_url)"""
    )
    db.session.execute(
        sql,
        {
            "title": data["title"],
            "authors": data["authors"],
            "key": data["key"],
            "year": data["year"],
            "type": data["doi"],
            "doi": data["doi"],
            "pages": data["pages"],
            "volume": data["volume"],
            "publisher": data["publisher"],
            "tags": data["tags"],
            "citation_url": data["citation_url"]
        },
    )

    db.session.commit()
