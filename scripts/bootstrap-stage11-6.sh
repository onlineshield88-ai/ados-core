#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "======================================"
echo " ADOS STAGE 11.6"
echo " Knowledge Agent"
echo "======================================"

mkdir -p python/ados/agents

cat > python/ados/agents/knowledge.py <<'PY'
from ados.agent import Agent


class KnowledgeAgent(Agent):

    name = "knowledge"

    def run(self, context):

        tasks = context.get("tasks", [])

        context["knowledge"] = {
            "task_count": len(tasks),
            "titles": [
                t.title
                for t in tasks
            ]
        }

        return context


agent = KnowledgeAgent()
PY


python - <<'PY'
from pathlib import Path

init = Path("python/ados/agents/__init__.py")

text = init.read_text()

if "knowledge import agent" not in text:
    text += "\nfrom .knowledge import agent as knowledge\n"

init.write_text(text)
PY


cat > python/ados/agent/loader.py <<'PY'
import importlib

MODULES = (
    "ados.agents.planner",
    "ados.agents.knowledge",
)


class AgentLoader:

    def __init__(self, manager):
        self.manager = manager

    def load(self):

        for module_name in MODULES:

            module = importlib.import_module(module_name)

            self.manager.register(module.agent)
PY


echo
echo "[1] knowledge agent"
echo "[2] loader updated"

echo
echo DONE
