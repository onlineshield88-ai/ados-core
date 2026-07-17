import importlib
import importlib.metadata
import shutil
import subprocess


class IntegrationRegistry:

    PYTHON_MODULES = {
        "networkx": "networkx",
        "radon": "radon",
        "libcst": "libcst",
        "jedi": "jedi",
        "tree_sitter": "tree_sitter",
    }

    EXECUTABLES = {
        "ruff": "ruff",
    }

    def status(self):

        result = {}

        for package, module in self.PYTHON_MODULES.items():

            try:
                importlib.import_module(module)
                result[package] = "READY"

            except Exception:
                result[package] = "MISSING"

        for package, exe in self.EXECUTABLES.items():

            result[package] = (
                "READY"
                if shutil.which(exe)
                else "MISSING"
            )

        return result

    def versions(self):

        versions = {}

        for package in self.PYTHON_MODULES:

            try:
                versions[package] = importlib.metadata.version(package)

            except Exception:
                versions[package] = None

        for package, exe in self.EXECUTABLES.items():

            if shutil.which(exe):

                try:

                    versions[package] = subprocess.check_output(
                        [exe, "--version"],
                        text=True,
                    ).strip()

                except Exception:

                    versions[package] = None

        return versions
