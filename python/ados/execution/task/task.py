from dataclasses import dataclass, field


@dataclass
class Task:

    id: str
    title: str

    description: str = ""

    status: str = "pending"

    priority: int = 0

    depends_on: list = field(default_factory=list)

    metadata: dict = field(default_factory=dict)
