import sqlite3
from typing import List, Optional

from ..models.session import StudySession


class SessionService:
    def __init__(self, connection: sqlite3.Connection):
        self.conn = connection

    def add_session(self, session: StudySession) -> int:
        cursor = self.conn.execute(
            """
            INSERT INTO study_sessions (course_id, date, minutes, topic, rating)
            VALUES (?, ?, ?, ?, ?)
            """,
            (session.course_id, session.date, session.minutes, session.topic, session.rating),
        )
        self.conn.commit()
        return cursor.lastrowid

    def list_sessions(self, course_id: Optional[int] = None) -> List[StudySession]:
        if course_id is None:
            cursor = self.conn.execute(
                """
                SELECT id, course_id, date, minutes, topic, rating
                FROM study_sessions
                ORDER BY date DESC, id DESC
                """
            )
        else:
            cursor = self.conn.execute(
                """
                SELECT id, course_id, date, minutes, topic, rating
                FROM study_sessions
                WHERE course_id = ?
                ORDER BY date DESC, id DESC
                """,
                (course_id,),
            )

        rows = cursor.fetchall()
        return [
            StudySession(
                id=row[0],
                course_id=row[1],
                date=row[2],
                minutes=row[3],
                topic=row[4],
                rating=row[5],
            )
            for row in rows
        ]

    def update_session(self, session_id: int, minutes: int, topic: Optional[str], rating: Optional[int]) -> bool:
        cursor = self.conn.execute(
            """
            UPDATE study_sessions
            SET minutes = ?, topic = ?, rating = ?
            WHERE id = ?
            """,
            (minutes, topic, rating, session_id),
        )
        self.conn.commit()
        return cursor.rowcount == 1
