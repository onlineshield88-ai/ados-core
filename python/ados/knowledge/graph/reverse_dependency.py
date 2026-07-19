class ReverseDependencyGraph:

    def __init__(self, dependency_graph):

        self.forward = dependency_graph
        self.reverse = {}

    def build(self):

        self.reverse = {}

        for module in self.forward.modules():

            self.reverse.setdefault(module, [])

        for module in self.forward.modules():

            try:
                imports = self.forward.imports(module)
            except Exception:
                imports = []

            for dep in imports:

                dep_file = dep.replace(".", "/") + ".py"

                for target in self.forward.modules():

                    if target.endswith(dep_file):

                        self.reverse.setdefault(target, [])

                        if module not in self.reverse[target]:
                            self.reverse[target].append(module)

        return self

    def imported_by(self, module):

        return sorted(
            self.reverse.get(module, [])
        )

    def modules(self):

        return sorted(
            self.reverse.keys()
        )

    def size(self):

        return len(self.reverse)
