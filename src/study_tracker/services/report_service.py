import sqlite3
from typing import List, Tuple


class ReportService:
    def __init__(self, connection: sqlite3.Connection):
        self.conn = connection

    def total_minutes_per_course(self) -> List[Tuple[str, int]]:
        cursor = self.conn.execute(
            """
            SELECT c.name, SUM(s.minutes)
            FROM courses c
            JOIN study_sessions s ON s.course_id = c.id
            GROUP BY c.id, c.name
            ORDER BY c.name
            """
        )
        return cursor.fetchall()
