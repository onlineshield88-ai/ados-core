class ToolExecutor:

    def __init__(self, registry):
        self.registry = registry

    def execute(self, tool_name, *args, **kwargs):

        tool = self.registry.get(tool_name)

        if tool is None:
            raise ValueError(f"Tool '{tool_name}' not registered")

        if callable(tool):
            return tool(*args, **kwargs)

        if hasattr(tool, "run"):
            return tool.run(*args, **kwargs)

        raise TypeError(f"Tool '{tool_name}' is not executable")
