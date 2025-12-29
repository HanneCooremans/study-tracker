import sqlite3

from .models.course import Course
from .models.session import StudySession
from .services.course_service import CourseService
from .services.session_service import SessionService
from .services.report_service import ReportService


def prompt(text: str) -> str:
    return input(text).strip()


def prompt_int(text: str) -> int:
    while True:
        value = input(text).strip()
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid number.")


def prompt_optional_int(text: str):
    value = input(text).strip()
    if value == "":
        return None
    try:
        return int(value)
    except ValueError:
        print("Invalid number, leaving empty.")
        return None


def show_courses(courses):
    if not courses:
        print("No courses found.")
        return
    for c in courses:
        print(f"{c.id}: {c.name} | teacher={c.teacher} | period={c.period}")


def show_sessions(sessions):
    if not sessions:
        print("No sessions found.")
        return
    for s in sessions:
        print(f"{s.id}: course_id={s.course_id} | {s.date} | {s.minutes} min | topic={s.topic} | rating={s.rating}")


def add_course_flow(course_service: CourseService):
    name = prompt("Course name: ")
    teacher = prompt("Teacher (optional): ")
    period = prompt("Period (optional): ")

    teacher_val = teacher if teacher != "" else None
    period_val = period if period != "" else None

    new_id = course_service.add_course(Course(id=None, name=name, teacher=teacher_val, period=period_val))
    print(f"Course added with id {new_id}")


def list_courses_flow(course_service: CourseService):
    courses = course_service.list_courses()
    show_courses(courses)


def search_courses_flow(course_service: CourseService):
    term = prompt("Search term: ")
    courses = course_service.find_courses_by_name(term)
    show_courses(courses)


def add_session_flow(session_service: SessionService):
    course_id = prompt_int("Course id: ")
    date = prompt("Date (YYYY-MM-DD): ")
    minutes = prompt_int("Minutes: ")
    topic = prompt("Topic (optional): ")
    rating = prompt_optional_int("Rating (optional number): ")

    topic_val = topic if topic != "" else None

    new_id = session_service.add_session(
        StudySession(
            id=None,
            course_id=course_id,
            date=date,
            minutes=minutes,
            topic=topic_val,
            rating=rating,
        )
    )
    print(f"Session added with id {new_id}")


def list_sessions_flow(session_service: SessionService):
    raw = prompt("Course id (optional, enter for all): ")
    if raw == "":
        sessions = session_service.list_sessions()
    else:
        try:
            cid = int(raw)
        except ValueError:
            print("Invalid course id.")
            return
        sessions = session_service.list_sessions(cid)
    show_sessions(sessions)


def update_session_flow(session_service: SessionService):
    session_id = prompt_int("Session id to update: ")
    minutes = prompt_int("New minutes: ")
    topic = prompt("New topic (optional): ")
    rating = prompt_optional_int("New rating (optional number): ")

    topic_val = topic if topic != "" else None

    ok = session_service.update_session(session_id=session_id, minutes=minutes, topic=topic_val, rating=rating)
    print("Updated." if ok else "Session not found.")


def run_cli(conn: sqlite3.Connection):
    course_service = CourseService(conn)
    session_service = SessionService(conn)
    report_service = ReportService(conn)


    while True:
        print()
        print("Study Tracker")
        print("1) Add course")
        print("2) List courses")
        print("3) Search courses")
        print("4) Add study session")
        print("5) List study sessions")
        print("6) Update study session")
        print("7) Report: total minutes per course")
        print("8) Export report to CSV")
        print("9) Export report to Excel")
        print("0) Exit")

        choice = prompt("Choose: ")

        if choice == "1":
            add_course_flow(course_service)
        elif choice == "2":
            list_courses_flow(course_service)
        elif choice == "3":
            search_courses_flow(course_service)
        elif choice == "4":
            add_session_flow(session_service)
        elif choice == "5":
            list_sessions_flow(session_service)
        elif choice == "6":
            update_session_flow(session_service)
        elif choice == "7":
            report_minutes_per_course_flow(report_service)
        elif choice == "8":
            report_service.export_csv("output/report.csv")
            print("CSV exported to output/report.csv")
        elif choice == "9":
            report_service.export_excel("output/report.xlsx")
            print("Excel exported to output/report.xlsx")
        elif choice == "0":
            break
        else:
            print("Unknown option.")
            
def report_minutes_per_course_flow(report_service: ReportService):
    rows = report_service.total_minutes_per_course()
    if not rows:
        print("No data found.")
        return
    for name, minutes in rows:
        print(f"{name}: {minutes} minutes")

