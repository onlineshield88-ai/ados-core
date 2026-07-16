from dataclasses import dataclass, field


@dataclass
class RuntimeContext:

    objective = None

    tasks: list = field(default_factory=list)

    knowledge: dict = field(default_factory=dict)

    memory: dict = field(default_factory=dict)

    reflection: dict = field(default_factory=dict)

    state: dict = field(default_factory=dict)
