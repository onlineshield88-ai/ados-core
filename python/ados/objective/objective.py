from dataclasses import dataclass


@dataclass
class Objective:

    goal: str

    priority: int = 1

    metadata: dict = None

    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}
