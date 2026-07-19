from pathlib import Path
from datetime import datetime

from ados.kernel.bootstrap import kernel


class ContextEngine:

    def __init__(self):
        self.k = kernel()

    def build(self):

        mem = self.k.memory

        workspace = mem.get("workspace") or {}
        repository = mem.get("repository") or {}

        dep = mem.get("dependency_graph")
        rev = mem.get("reverse_dependency_graph")

        ctx = {

            "timestamp": datetime.utcnow().isoformat(),

            "workspace_root": workspace.get("root"),

            "workspace_name": (
                Path(workspace.get("root")).name
                if workspace.get("root")
                else None
            ),

            "directories": workspace.get(
                "directory_count",
                0,
            ),

            "files": workspace.get(
                "file_count",
                0,
            ),

            "languages": repository.get(
                "languages",
                {},
            ),

            "symbols": len(
                mem.get("symbols") or {}
            ),

            "deps": dep.size() if dep else 0,

            "reverse": rev.size() if rev else 0,

            "cwd": str(Path.cwd()),
        }

        return ctx

    def summary(self):

        c = self.build()

        langs = "\n".join(
            f"{k:<12}: {v}"
            for k, v in sorted(
                c["languages"].items()
            )
        )

        return f"""
Workspace
---------

Name        : {c["workspace_name"]}
Root        : {c["workspace_root"]}

Directories : {c["directories"]}
Files       : {c["files"]}

Repository
----------

{langs}

Symbols     : {c["symbols"]}
Dependencies: {c["deps"]}
Reverse     : {c["reverse"]}

Directory   : {c["cwd"]}
""".strip()
