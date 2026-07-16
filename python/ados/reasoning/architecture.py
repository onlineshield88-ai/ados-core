class ArchitectureAnalyzer:

    def __init__(self, kernel):
        self.kernel = kernel

    def analyze(self):

        deps = self.kernel.memory.get(
            "dependency_graph"
        )

        report = []

        for module in sorted(deps.modules()):

            try:
                imports = deps.imports(module)
            except Exception:
                imports = []

            report.append({
                "module": module,
                "imports": len(imports),
                "dependencies": sorted(imports)
            })

        return report

    def hotspots(self):

        report = self.analyze()

        return sorted(
            report,
            key=lambda x: x["imports"],
            reverse=True
        )

    def summary(self):

        report = self.analyze()

        total_imports = sum(
            item["imports"]
            for item in report
        )

        return {
            "modules": len(report),
            "total_imports": total_imports,
            "average_imports":
                round(
                    total_imports / max(len(report),1),
                    2
                )
        }
