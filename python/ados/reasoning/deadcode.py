class DeadCodeDetector:

    def __init__(self, kernel):
        self.kernel = kernel

    def detect(self):

        refs = self.kernel.memory.get(
            "reference_resolver"
        )

        symbols = self.kernel.memory.get(
            "symbols"
        )

        result = []

        for symbol in symbols:

            if symbol["type"] not in (
                "class",
                "function"
            ):
                continue

            callers = refs.callers(
                symbol["name"]
            )

            callers = [
                c for c in callers
                if c != symbol["file"]
            ]

            if not callers:
                result.append({
                    "name": symbol["name"],
                    "type": symbol["type"],
                    "file": symbol["file"],
                    "line": symbol["line"]
                })

        return sorted(
            result,
            key=lambda x: (
                x["file"],
                x["line"]
            )
        )

    def summary(self):

        dead = self.detect()

        return {
            "dead_symbols": len(dead),
            "symbols": dead
        }
