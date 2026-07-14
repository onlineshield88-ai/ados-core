from pathlib import Path

folders=[
"constitution",
"genome",
"world",
"contracts",
"knowledge",
"decision",
"execution",
"engine",
"runtime",
"handover",
"memory",
"state",
"docs",
"external/repositories"
]

print("="*60)

for f in folders:
    print(f,"OK" if Path(f).exists() else "MISSING")
