class CrossReference:

    def __init__(self, kernel):
        self.kernel = kernel

    def definition(self, name):

        result = []

        for s in self.kernel.memory.get("symbols"):

            if s["name"] == name:
                result.append(s)

        return result

    def implementations(self, keyword):

        result = []

        keyword = keyword.lower()

        for s in self.kernel.memory.get("symbols"):

            if s["type"] in ("class", "function"):

                if keyword in s["name"].lower():
                    result.append(s)

        return result

    def usages(self, symbol):

        refs = self.kernel.memory.get(
            "reference_resolver"
        )

        return refs.callers(symbol)

    def imports(self, module):

        deps = self.kernel.memory.get(
            "dependency_graph"
        )

        return deps.imports(module)
