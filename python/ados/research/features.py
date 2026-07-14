from pathlib import Path
import yaml

GRAPH = Path("knowledge/graphs")
OUT = Path("knowledge/features")

OUT.mkdir(exist_ok=True)

FEATURE_RULES = {
    "Plugin System": ("plugin", 1),
    "Agent Framework": ("agent", 1),
    "Runtime Engine": ("runtime", 1),
    "Memory System": ("memory", 1),
    "MCP Support": ("mcp", 1),
}

for file in sorted(GRAPH.glob("*.yaml")):

    graph = yaml.safe_load(file.read_text())

    features = {}

    for feature, (section, minimum) in FEATURE_RULES.items():
        enabled = graph.get(section, {}).get("total", 0) >= minimum
        features[feature] = enabled

    with open(OUT / file.name, "w") as fp:
        yaml.dump(features, fp, sort_keys=False)

print("Feature detection complete.")
