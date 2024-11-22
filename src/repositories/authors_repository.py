from sqlalchemy import text
from config import db


def get_authors_by_citation_id(id):
    sql = text(
        "SELECT first_name, last_name FROM authors WHERE citation_id = :id")
    result = db.session.execute(
        sql,
        {"id": id}
    )
    authors = result.fetchall()

    return authors


def add_author_by_citation_id(id, author):
    first_name, last_name = author.split(" ")
    sql = text(
        "INSERT INTO authors (citation_id, first_name, last_name) VALUES (:id, :first_name, :last_name)")
    db.session.execute(
        sql,
        {
            "id": id,
            "first_name": first_name,
            "last_name": last_name,
        }
    )

    db.session.commit()
