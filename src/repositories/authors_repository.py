from sqlalchemy import text
from config import db


def get_authors_by_citation_id(citation_id):
    sql = text("SELECT first_name, last_name FROM authors WHERE citation_id = :id")
    result = db.session.execute(sql, {"id": citation_id})
    authors = result.fetchall()

    return authors


def add_author_by_citation_id(citation_id, author, is_main):
    first_name, last_name = author.split(" ", 1)
    sql = text(
        "INSERT INTO authors (citation_id, first_name, last_name, main_author)"
        " VALUES (:id, :first_name, :last_name, :main_author)"
    )
    db.session.execute(
        sql,
        {
            "id": citation_id,
            "first_name": first_name,
            "last_name": last_name,
            "main_author": is_main
        },
    )
