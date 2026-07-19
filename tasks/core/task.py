from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class Task:

    type: str
    action: str

    payload: dict = field(default_factory=dict)

    priority: str = "normal"

    workspace: str | None = None

    id: str = field(
        default_factory=lambda: uuid4().hex
    )

    status: str = "pending"

    result: dict | None = None

    error: str | None = None
