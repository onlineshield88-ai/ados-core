from pathlib import Path
from datetime import datetime

from ados.kernel.bootstrap import kernel


class ContextEngine:

    def __init__(self):
        self.k = kernel()

    def build(self):
        mem = self.k.memory

        ctx = {
            "timestamp": datetime.utcnow().isoformat(),
            "workspace": mem.get("workspace"),
            "repository": mem.get("repository"),
            "symbols": len(mem.get("symbols") or {}),
            "dependency_graph": len(mem.get("dependency_graph") or {}),
            "reverse_dependency_graph": len(
                mem.get("reverse_dependency_graph") or {}
            ),
            "cwd": str(Path.cwd()),
        }

        return ctx

    def summary(self):

        c = self.build()

        return f"""
Workspace : {c['workspace']}
Repository: {c['repository']}
Symbols   : {c['symbols']}
Deps      : {c['dependency_graph']}
Reverse   : {c['reverse_dependency_graph']}
Directory : {c['cwd']}
""".strip()
