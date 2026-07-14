from pathlib import Path
import yaml

BASE = Path("knowledge/features")

print("=" * 72)

header = (
    f"{'Repository':18}"
    f"{'Plugin':>9}"
    f"{'Agent':>9}"
    f"{'Runtime':>10}"
    f"{'Memory':>9}"
    f"{'MCP':>7}"
)

print(header)
print("=" * 72)

for f in sorted(BASE.glob("*.yaml")):

    d = yaml.safe_load(f.read_text())

    print(
        f"{f.stem:18}"
        f"{'YES' if d['Plugin System'] else '-':>9}"
        f"{'YES' if d['Agent Framework'] else '-':>9}"
        f"{'YES' if d['Runtime Engine'] else '-':>10}"
        f"{'YES' if d['Memory System'] else '-':>9}"
        f"{'YES' if d['MCP Support'] else '-':>7}"
    )
