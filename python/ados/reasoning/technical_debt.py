class TechnicalDebtAnalyzer:

    def __init__(self, kernel):
        self.kernel = kernel

    def analyze(self):

        complexity = self.kernel.memory.get("complexity_summary")
        maintainability = self.kernel.memory.get("maintainability_summary")
        deadcode = self.kernel.memory.get("deadcode_summary")
        unused = self.kernel.memory.get("unused_imports_summary")
        cycles = self.kernel.memory.get("cycle_summary")

        debt = []

        if complexity["high_risk"] > 0:
            debt.append({
                "category": "Complexity",
                "count": complexity["high_risk"],
                "severity": "High"
            })

        if deadcode["dead_symbols"] > 0:
            debt.append({
                "category": "Dead Code",
                "count": deadcode["dead_symbols"],
                "severity": "Medium"
            })

        if unused["unused_imports"] > 0:
            debt.append({
                "category": "Unused Imports",
                "count": unused["unused_imports"],
                "severity": "Low"
            })

        if cycles["cycle_count"] > 0:
            debt.append({
                "category": "Circular Dependencies",
                "count": cycles["cycle_count"],
                "severity": "Critical"
            })

        avg = maintainability["average_mi"]

        if avg < 50:
            severity = "Critical"
        elif avg < 60:
            severity = "High"
        elif avg < 70:
            severity = "Medium"
        else:
            severity = "Low"

        debt.append({
            "category": "Maintainability",
            "count": round(avg,2),
            "severity": severity
        })

        return debt

    def summary(self):

        debt = self.analyze()

        score = 0

        for item in debt:

            if item["severity"] == "Critical":
                score += 5
            elif item["severity"] == "High":
                score += 3
            elif item["severity"] == "Medium":
                score += 2
            else:
                score += 1

        if score <= 5:
            level = "Excellent"
        elif score <= 10:
            level = "Good"
        elif score <= 15:
            level = "Moderate"
        elif score <= 20:
            level = "High Debt"
        else:
            level = "Critical Debt"

        return {
            "technical_debt_score": score,
            "technical_debt_level": level,
            "items": debt
        }
