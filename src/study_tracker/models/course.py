from dataclasses import dataclass
from typing import Optional


@dataclass
class Course:
    id: Optional[int]
    name: str
    teacher: Optional[str] = None
    period: Optional[str] = None
