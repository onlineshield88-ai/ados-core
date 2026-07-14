#!/usr/bin/env python3

from pathlib import Path
import yaml

base=Path("external/repositories")

print("="*60)
print("Tracked External Repositories")
print("="*60)

for f in sorted(base.glob("*.yaml")):
    data=yaml.safe_load(f.read_text())

    print(data["name"])
    print(" repo :",data["repository"])
    print()
