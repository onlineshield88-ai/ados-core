class RepositoryReviewEngine:

    def __init__(self, kernel):
        self.kernel = kernel

    def review(self):

        repo = self.kernel.memory.get("repository")
        deps = self.kernel.memory.get("dependency_graph")
        refs = self.kernel.memory.get("reference_resolver")
        reverse = self.kernel.memory.get("reverse_dependency_graph")

        return {
            "files": repo["total_files"],
            "languages": repo["languages"],
            "modules": deps.size(),
            "symbols": len(self.kernel.memory.get("symbols")),
            "references": len(refs.symbols()),
            "reverse_modules": reverse.size()
        }

    def hotspots(self):

        deps = self.kernel.memory.get(
            "dependency_graph"
        )

        result = []

        for module in deps.modules():

            try:
                imports = deps.imports(module)
            except Exception:
                imports = []

            result.append(
                (len(imports), module)
            )

        return sorted(
            result,
            reverse=True
        )

    def orphan_modules(self):

        reverse = self.kernel.memory.get(
            "reverse_dependency_graph"
        )

        result = []

        for module in reverse.modules():

            if len(reverse.imported_by(module)) == 0:
                result.append(module)

        return sorted(result)

    def summary(self):

        data = self.review()

        data["hotspots"] = len(
            self.hotspots()
        )

        data["orphans"] = len(
            self.orphan_modules()
        )

        return data
