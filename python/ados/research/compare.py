import yaml
from pathlib import Path

base=Path("knowledge/repositories")

for f in sorted(base.glob("*.yaml")):
    d=yaml.safe_load(f.read_text())

    print("="*60)
    print(d.get("name"))
    print(d.get("repository"))
    print("Category :",d.get("category",""))
    print()
