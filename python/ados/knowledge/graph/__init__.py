try:
    from .task_graph import TaskGraph
except ImportError:
    pass

try:
    from .dependency_graph import DependencyGraph
except ImportError:
    pass

try:
    from .reverse_dependency import ReverseDependencyGraph
except ImportError:
    pass
