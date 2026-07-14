from pathlib import Path

required=[
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
"external"
]

missing=[]

for r in required:
    if not Path(r).exists():
        missing.append(r)

print("="*60)

if missing:
    print("Missing:")
    for i in missing:
        print("-",i)
else:
    print("Repository Healthy")

print("="*60)
