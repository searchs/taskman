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
        return cls(id=id, title=title, status=TaskStatus.OPEN, owner=owner)
