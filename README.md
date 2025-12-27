\# Study Tracker (CLI)



\## Purpose

Command-line application to track courses and study sessions.



\## Functionalities

\- Add and list courses

\- Add and list study sessions

\- Update study sessions

\- Report: total study minutes per course

\- Export report to CSV or Excel



\## Project structure

\- `main.py` (root): application entrypoint

\- `src/study\_tracker/`: main package

&nbsp; - `cli.py`: user interface layer

&nbsp; - `models/`: domain layer

&nbsp; - `services/`: service layer

&nbsp; - `db.py` + `schema.py`: data access layer



\## Setup

1\. Create and activate virtual environment:

&nbsp;  ```bash

&nbsp;  python -m venv .venv

&nbsp;  .venv\\Scripts\\activate



