from pathlib import Path
import subprocess

class ContextBuilder:

    def build(self,user_prompt:str)->str:

        cwd=Path.cwd()

        try:
            branch=subprocess.check_output(
                ["git","branch","--show-current"],
                text=True
            ).strip()
        except:
            branch="unknown"

        try:
            commit=subprocess.check_output(
                ["git","rev-parse","--short","HEAD"],
                text=True
            ).strip()
        except:
            commit="-"

        text=f"""
Workspace:
{cwd}

Branch:
{branch}

Commit:
{commit}

Instruction:
{user_prompt}
"""

        return text.strip()
