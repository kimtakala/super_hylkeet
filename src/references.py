from flask import request
from sqlalchemy import text
from config import db


def add_reference():
    title = request.form["title"]
    author = request.form["author"]
    year = request.form["year"]
    type = request.form["type"]
    doi = request.form["doi"]
    pages = request.form["pages"]
    volume = request.form["volume"]
    publisher = request.form["publisher"]
    tags = request.form["tags"]

    sql = text(
        "INSERT INTO references (title, author, year, type, doi, pages, volume, publisher, tags) VALUES (:title, :author, :year, :type, :doi, :pages, :volume, :publisher, :tags)"
    )
    db.session.execute(
        sql,
        {
            "title": title,
            "author": author,
            "year": year,
            "type": type,
            "doi": doi,
            "pages": pages,
            "volume": volume,
            "publisher": publisher,
            "tags": tags,
        },
    )

    db.session.commit()
