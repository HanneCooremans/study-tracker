# Study Tracker (CLI)

## Purpose
Command-line application to track courses and study sessions using a simple SQLite database.

## Functionalities
- Add and list courses
- Add and list study sessions
- Update study sessions
- Report total study minutes per course
- Export report to CSV
- Export report to Excel

## Project structure
- main.py (root): application entrypoint
- src/study_tracker/: main package
  - cli.py: user interface layer (CLI)
  - models/: domain layer (Course, StudySession)
  - services/: service layer (business logic)
  - db.py: database connection and initialization
- data/: databases
- output/: generated reports

## Requirements
- Python 3.10 or higher
- Virtual environment (venv)

## Setup
Create a virtual environment in the project root:
python -m venv .venv

Activate the virtual environment (Windows cmd):
.venv\Scripts\activate.bat

Install dependencies:
pip install -r requirements.txt

## Configuration
Create a settings.ini file based on settings.example.ini.

Example content:
[app]
db_path = data/study_tracker.db

This file is not included in the git repository.

## Sample database
A sample SQLite database with sample data is provided:
data/study_tracker_sample.db

To run the application with sample data:
1. Copy the sample database:
   copy data\study_tracker_sample.db data\study_tracker.db
2. Ensure settings.ini points to data/study_tracker.db.

## Run the application
From the project root:
python main.py

## Reports and export
The application can generate a report with total study minutes per course.
Exports are written to:
- output/report.csv
- output/report.xlsx
