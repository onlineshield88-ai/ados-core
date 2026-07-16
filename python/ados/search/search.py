class SemanticSearch:

    def __init__(self, kernel):
        self.kernel = kernel

    def symbols(self, keyword):

        keyword = keyword.lower()

        results = []

        for s in self.kernel.memory.get("symbols"):

            if keyword in s["name"].lower():
                results.append(s)

        return results

    def modules(self, keyword):

        deps = self.kernel.memory.get(
            "dependency_graph"
        )

        keyword = keyword.lower()

        return [
            m
            for m in deps.modules()
            if keyword in m.lower()
        ]

    def callers(self, symbol):

        refs = self.kernel.memory.get(
            "reference_resolver"
        )

        return refs.callers(symbol)
