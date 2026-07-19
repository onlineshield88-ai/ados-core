#!/usr/bin/env python3

from pathlib import Path
import yaml

FEATURE_DIR = Path("knowledge/features")
OUT_DIR = Path("knowledge/architecture")

OUT_DIR.mkdir(parents=True, exist_ok=True)

for f in sorted(FEATURE_DIR.glob("*.yaml")):

    d = yaml.safe_load(f.read_text())

    result = {
        "repository": f.stem,

        "capabilities": {

            "plugin_system": d.get("plugin",0) > 0,
            "agent_system": d.get("agent",0) > 0,
            "command_system": d.get("commands",0) > 0,
            "hook_system": d.get("hooks",0) > 0,
            "skill_system": d.get("skills",0) > 0,
            "workflow_system": d.get("workflow",0) > 0,
            "runtime_system": d.get("runtime",0) > 0,
            "mcp_system": d.get("mcp",0) > 0,
            "template_system": d.get("template",0) > 0,
            "config_system": d.get("config",0) > 0

        }

    }

    with open(OUT_DIR/f.name,"w") as fp:
        yaml.dump(result,fp,sort_keys=False)

    print(f"{f.stem} architecture analyzed")
