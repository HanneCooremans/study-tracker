from dataclasses import dataclass
from typing import Optional


@dataclass
class StudySession:
    id: Optional[int]
    course_id: int
    date: str          
    minutes: int
    topic: Optional[str] = None
    rating: Optional[int] = None
