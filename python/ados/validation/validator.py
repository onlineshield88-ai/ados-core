#!/usr/bin/env python3

from pathlib import Path
import yaml

ROOT=Path("knowledge")

required=[

    "analysis",
    "features",
    "architecture",
    "graphs"

]

print("="*70)
print("ADOS Repository Validation")
print("="*70)

ok=True

for folder in required:

    p=ROOT/folder

    if not p.exists():

        print(f"[FAIL] {folder} missing")

        ok=False

        continue

    files=list(p.glob("*.yaml"))

    print(f"{folder:15} {len(files):4} yaml")

if ok:
    print()
    print("STATUS : OK")
else:
    print()
    print("STATUS : FAILED")
