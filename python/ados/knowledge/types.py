from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any

@dataclass
class FunctionRecord:
    key: str
    name: str
    module: str
    file: str
    line: int
    args: List[str] = field(default_factory=list)
    return_annotation: Optional[str] = None
    docstring: Optional[str] = None
    decorators: List[str] = field(default_factory=list)
    is_async: bool = False
    parent_class: Optional[str] = None

@dataclass
class ClassRecord:
    key: str
    name: str
    module: str
    file: str
    line: int
    bases: List[str] = field(default_factory=list)
    methods: List[str] = field(default_factory=list)
    docstring: Optional[str] = None
    decorators: List[str] = field(default_factory=list)

@dataclass
class ModuleRecord:
    name: str
    file: str
    imports: List[Dict[str, Any]] = field(default_factory=list)
    classes: List[str] = field(default_factory=list)
    functions: List[str] = field(default_factory=list)
    docstring: Optional[str] = None

@dataclass
class ImportRecord:
    type: str
    module: str
    name: Optional[str] = None
    alias: Optional[str] = None
    file: str = ""
