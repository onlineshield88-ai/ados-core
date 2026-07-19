from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class RuntimeSession:

    id: str = field(default_factory=lambda: str(uuid4()))

    user: str = "local"

    project: str = ""

    state: dict = field(default_factory=dict)
