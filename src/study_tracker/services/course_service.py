import sqlite3
from typing import List

from ..models.course import Course


class CourseService:
    def __init__(self, connection: sqlite3.Connection):
        self.conn = connection

    def add_course(self, course: Course) -> int:
        cursor = self.conn.execute(
            """
            INSERT INTO courses (name, teacher, period)
            VALUES (?, ?, ?)
            """,
            (course.name, course.teacher, course.period),
        )
        self.conn.commit()
        return cursor.lastrowid

    def list_courses(self) -> List[Course]:
        cursor = self.conn.execute(
            """
            SELECT id, name, teacher, period
            FROM courses
            ORDER BY name
            """
        )
        rows = cursor.fetchall()

        return [
            Course(
                id=row[0],
                name=row[1],
                teacher=row[2],
                period=row[3],
            )
            for row in rows
        ]

    def find_courses_by_name(self, search: str) -> List[Course]:
        cursor = self.conn.execute(
            """
            SELECT id, name, teacher, period
            FROM courses
            WHERE name LIKE ?
            ORDER BY name
            """,
            (f"%{search}%",),
        )
        rows = cursor.fetchall()

        return [
            Course(
                id=row[0],
                name=row[1],
                teacher=row[2],
                period=row[3],
            )
            for row in rows
        ]
