class CircularDependencyDetector:

    def __init__(self, kernel):
        self.kernel = kernel

    def detect(self):

        deps = self.kernel.memory.get(
            "dependency_graph"
        )

        modules = deps.modules()

        graph = {}

        for module in modules:

            edges = []

            try:
                imports = deps.imports(module)
            except Exception:
                imports = []

            for imp in imports:

                target = imp.replace(".", "/") + ".py"

                for m in modules:
                    if m.endswith(target):
                        edges.append(m)

            graph[module] = edges

        visited = set()
        stack = []
        cycles = []

        def dfs(node):

            if node in stack:
                i = stack.index(node)
                cycles.append(stack[i:] + [node])
                return

            if node in visited:
                return

            visited.add(node)
            stack.append(node)

            for nxt in graph.get(node, []):
                dfs(nxt)

            stack.pop()

        for module in modules:
            dfs(module)

        unique = []

        seen = set()

        for cycle in cycles:

            key = tuple(sorted(cycle))

            if key not in seen:
                seen.add(key)
                unique.append(cycle)

        return unique

    def summary(self):

        cycles = self.detect()

        return {
            "cycle_count": len(cycles),
            "cycles": cycles
        }
