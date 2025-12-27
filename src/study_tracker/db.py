import sqlite3
from configparser import ConfigParser
from pathlib import Path

from .schema import SCHEMA_SQL


def load_settings(path="settings.ini"):
    config = ConfigParser()
    if not Path(path).exists():
        raise FileNotFoundError(
            "settings.ini not found. Create it based on settings.example.ini"
        )
    config.read(path)
    return {
        "db_path": config.get("app", "db_path")
    }


def get_connection(db_path):
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    return conn


def init_db(conn):
    conn.executescript(SCHEMA_SQL)
    conn.commit()
