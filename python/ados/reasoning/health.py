class RepositoryHealthAnalyzer:

    def __init__(self, kernel):
        self.kernel = kernel

    def analyze(self):

        complexity = self.kernel.memory.get("complexity_summary")
        maintainability = self.kernel.memory.get("maintainability_summary")
        deadcode = self.kernel.memory.get("deadcode_summary")
        unused = self.kernel.memory.get("unused_imports_summary")
        cycles = self.kernel.memory.get("cycle_summary")

        high_risk = complexity["high_risk"]
        avg_mi = maintainability["average_mi"]
        dead = deadcode["dead_symbols"]
        unused_imports = unused["unused_imports"]
        cycle_count = cycles["cycle_count"]

        score = 100

        score -= high_risk * 2
        score -= dead * 0.10
        score -= unused_imports * 0.20
        score -= cycle_count * 5
        score += (avg_mi - 70) * 0.5

        score = max(0, min(100, round(score,2)))

        if score >= 90:
            grade = "A+"
        elif score >= 80:
            grade = "A"
        elif score >= 70:
            grade = "B"
        elif score >= 60:
            grade = "C"
        elif score >= 50:
            grade = "D"
        else:
            grade = "E"

        return {
            "score": score,
            "grade": grade,
            "high_risk_functions": high_risk,
            "dead_symbols": dead,
            "unused_imports": unused_imports,
            "cycles": cycle_count,
            "maintainability": avg_mi,
        }
