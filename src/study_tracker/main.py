from .cli import run_cli
from .db import load_settings, get_connection, init_db


def main():
    settings = load_settings("settings.ini")
    conn = get_connection(settings["db_path"])
    init_db(conn)
    run_cli(conn)


if __name__ == "__main__":
    main()
