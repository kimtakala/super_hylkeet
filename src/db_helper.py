from sqlalchemy import text
from config import db, app

COLUMN_NAMES = [
    "id",
    "key",
    "type",
    "title",
    "year",
    "pages",
    "volume",
    "publisher",
    "doi",
    "tags",
    "booktitle",
    "citation_url",
    "timestamp"
]

TABLE_CITATIONS = """
                    id SERIAL PRIMARY KEY,
                    key TEXT,
                    type TEXT,
                    title TEXT,
                    year TEXT,
                    pages TEXT,
                    volume TEXT,
                    publisher TEXT,
                    doi TEXT,
                    tags TEXT,
                    booktitle TEXT,
                    citation_url TEXT,
                    timestamp TEXT
                """

TABLE_AUTHORS = """
                    id SERIAL PRIMARY KEY,
                    citation_id INT NOT NULL,
                    first_name TEXT,
                    last_name TEXT,
                    main_author BOOLEAN,
                    FOREIGN KEY (citation_id) 
                        REFERENCES citations(id)
                        ON DELETE CASCADE
                """


def table_exists(name):
    sql_table_existence = text(
        "SELECT EXISTS ("
        "  SELECT 1"
        "  FROM information_schema.tables"
        f" WHERE table_name = '{name}'"
        ")"
    )

    print(f"Checking if table {name} exists")

    result = db.session.execute(sql_table_existence)
    return result.fetchall()[0][0]


def reset_table(table_name):
    print(f"Clearing contents from table {table_name}")
    sql = text(f"DELETE FROM {table_name}")
    db.session.execute(sql)
    db.session.commit()


def setup_table(table_name):
    tables = {"citations": TABLE_CITATIONS, "authors": TABLE_AUTHORS}

    if table_name not in tables:
        raise ValueError(f"Table name {table_name} not regognized.")

    if table_exists(table_name):
        print(f"Dropping table {table_name}.")
        sql = text(f"DROP TABLE {table_name} CASCADE")
        db.session.execute(sql)
        db.session.commit()

    print(f"Creating table {table_name}")
    sql = text(f"CREATE TABLE {table_name} ({tables[table_name]})")
    db.session.execute(sql)
    db.session.commit()


def reset_db():
    reset_table("authors")
    reset_table("citations")


def setup_db():
    setup_table("citations")
    setup_table("authors")


if __name__ == "__main__":
    with app.app_context():
        setup_db()
