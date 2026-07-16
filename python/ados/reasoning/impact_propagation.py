class ImpactPropagationEngine:

    def __init__(self, kernel):
        self.kernel = kernel

    def analyze(self, module):

        reverse = self.kernel.memory.get(
            "reverse_dependency_graph"
        )

        deps = self.kernel.memory.get(
            "dependency_graph"
        )

        visited = set()
        queue = [module]

        while queue:

            current = queue.pop(0)

            if current in visited:
                continue

            visited.add(current)

            try:
                parents = reverse.imported_by(current)
            except Exception:
                parents = []

            for parent in parents:
                if parent not in visited:
                    queue.append(parent)

        visited.discard(module)

        score = len(visited)

        if score == 0:
            risk = "Very Low"
        elif score < 5:
            risk = "Low"
        elif score < 10:
            risk = "Medium"
        elif score < 20:
            risk = "High"
        else:
            risk = "Critical"

        try:
            imports = deps.imports(module)
        except Exception:
            imports = []

        return {
            "module": module,
            "imports": imports,
            "affected": sorted(visited),
            "affected_count": len(visited),
            "risk": risk
        }
