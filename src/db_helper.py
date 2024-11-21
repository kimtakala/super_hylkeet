from config import db, app
from sqlalchemy import text

table_name = "citations"

COLUMN_NAMES = ["id", "key", "type", "title", "authors", "year",
                "pages", "volume", "publisher", "doi", "tags", "citation_url", "timestamp"]


def table_exists(name):
    sql_table_existence = text(
        "SELECT EXISTS ("
        "  SELECT 1"
        "  FROM information_schema.tables"
        f" WHERE table_name = '{name}'"
        ")"
    )

    print(f"Checking if table {name} exists")
    print(sql_table_existence)

    result = db.session.execute(sql_table_existence)
    return result.fetchall()[0][0]


def reset_db():
    print(f"Clearing contents from table {table_name}")
    sql = text(f"DELETE FROM {table_name}")
    db.session.execute(sql)
    sql = text(f"DELETE FROM authors")
    db.session.execute(sql)
    db.session.commit()


def setup_db():
    print(f"Creating table {table_name}")
    sql = text(
        f"""CREATE TABLE {table_name}(
    id SERIAL PRIMARY KEY,
    key TEXT NOT NULL,
    type TEXT NOT NULL,
    title TEXT NOT NULL,
    authors TEXT,
    year INT,
    pages TEXT,
    volume TEXT,
    publisher TEXT,
    doi TEXT,
    tags TEXT,
    citation_url TEXT,
    timestamp TEXT
    )"""
    )

    db.session.execute(sql)

    sql = text(
        f"""CREATE TABLE authors(
    id SERIAL PRIMARY KEY,
    citation_id INT NOT NULL,
    first_name TEXT,
    last_name TEXT,
    FOREIGN KEY (citation_id) REFERENCES citations(id)
    )"""
    )

    db.session.execute(sql)
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        setup_db()
