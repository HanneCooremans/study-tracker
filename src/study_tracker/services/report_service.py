import sqlite3
import pandas as pd
from pathlib import Path


class ReportService:
    def __init__(self, connection: sqlite3.Connection):
        self.conn = connection

    def total_minutes_per_course(self):
        cursor = self.conn.execute(
            """
            SELECT c.name AS course, SUM(s.minutes) AS minutes
            FROM courses c
            JOIN study_sessions s ON s.course_id = c.id
            GROUP BY c.id, c.name
            ORDER BY c.name
            """
        )
        return cursor.fetchall()

    def export_csv(self, path: str):
        rows = self.total_minutes_per_course()
        df = pd.DataFrame(rows, columns=["course", "minutes"])
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(path, index=False)

    def export_excel(self, path: str):
        rows = self.total_minutes_per_course()
        df = pd.DataFrame(rows, columns=["course", "minutes"])
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        df.to_excel(path, index=False)
