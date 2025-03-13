from dataclasses import dataclass
from enum import Enum
from uuid import UUID


class TaskStatus(str, Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"


@dataclass
class Task:
    id: UUID
    title: str
    status: TaskStatus
    owner: str

    @classmethod
    def create(cls, id, title, owner):
        if not title:
            raise ValueError("Title cannot be empty")
        if type(id) is not UUID:
            raise ValueError("ID cannot be empty")
        return cls(id=id, title=title, status=TaskStatus.OPEN, owner=owner)
