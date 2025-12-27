SCHEMA_SQL = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    teacher TEXT,
    period TEXT
);

CREATE TABLE IF NOT EXISTS study_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    minutes INTEGER NOT NULL,
    topic TEXT,
    rating INTEGER,
    FOREIGN KEY(course_id) REFERENCES courses(id)
);
"""
