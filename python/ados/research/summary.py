from pathlib import Path
import yaml

base=Path("knowledge/extracted")

for f in sorted(base.glob("*.yaml")):

    d=yaml.safe_load(f.read_text())

    print("="*60)

    print(f.stem)

    for k,v in d.items():

        print(f"{k:12}",len(v))
