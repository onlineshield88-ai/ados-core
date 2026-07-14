#!/usr/bin/env python3

from pathlib import Path

required = [
"constitution",
"genome",
"knowledge",
"engine",
"decision",
"runtime",
"contracts",
"docs",
"specs",
"python",
"install"
]

missing=[]

for i in required:
    if not Path(i).exists():
        missing.append(i)

print("="*60)

if missing:
    print("Missing")
    for m in missing:
        print("-",m)
else:
    print("Repository Healthy")

print("="*60)
