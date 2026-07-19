class TaskGraph:

    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_task(self, task):
        self.nodes[task.id] = task
        self.edges.setdefault(task.id, [])

    def connect(self, parent, child):
        self.edges.setdefault(parent, [])
        self.edges[parent].append(child)

    def children(self, task_id):
        return self.edges.get(task_id, [])

    def tasks(self):
        return list(self.nodes.values())
