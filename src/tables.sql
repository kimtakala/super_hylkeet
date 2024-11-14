CREATE TABLE refrences (
    id SERIAL PRIMARY KEY,
    key TEXT NOT NULL,
    type TEXT NOT NULL,
    title TEXT NOT NULL,
    authors TEXT NOT NULL,
    year INT,
    pages TEXT,
    volume TEXT,
    publisher TEXT,
    link TEXT,
    doi TEXT,
    tag TEXT
)