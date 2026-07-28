from pathlib import Path
import subprocess


class ProjectScanner:

    def __init__(self, root="."):
        self.root = Path(root).resolve()

    def project_name(self):
        return self.root.name

    def count_files(self, ext):
        return len(list(self.root.rglob(f"*{ext}")))

    def git_branch(self):
        try:
            return subprocess.check_output(
                ["git", "branch", "--show-current"],
                cwd=self.root,
                text=True
            ).strip()
        except Exception:
            return "-"

    def git_status(self):
        try:
            out = subprocess.check_output(
                ["git", "status", "--porcelain"],
                cwd=self.root,
                text=True
            ).strip()

            return "clean" if out == "" else "modified"

        except Exception:
            return "-"

    def modules(self):

        modules=[]

        base=self.root/"python"

        if not base.exists():
            return modules

        for f in base.rglob("__init__.py"):

            module=str(
                f.parent.relative_to(base)
            ).replace("/", ".")

            modules.append(module)

        return sorted(modules)

    def summary(self):

        return {

            "project":self.project_name(),

            "branch":self.git_branch(),

            "status":self.git_status(),

            "python":self.count_files(".py"),

            "markdown":self.count_files(".md"),

            "json":self.count_files(".json"),

            "yaml":self.count_files(".yaml")+self.count_files(".yml"),

            "toml":self.count_files(".toml"),

            "modules":self.modules()

        }
