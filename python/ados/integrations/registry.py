import importlib

class IntegrationRegistry:

    MODULES = {
        "networkx": "networkx",
        "radon": "radon",
        "ruff": "ruff",
        "libcst": "libcst",
        "jedi": "jedi",
        "tree_sitter": "tree_sitter",
    }

    def status(self):

        result = {}

        for name,module in self.MODULES.items():

            try:
                importlib.import_module(module)
                result[name]="READY"

            except Exception:
                result[name]="MISSING"

        return result
