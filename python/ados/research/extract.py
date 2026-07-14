from pathlib import Path
import yaml

ROOT=Path("external/cache")

KEYWORDS={

"plugins":"plugins",

"agents":"agents",

"commands":"commands",

"hooks":"hooks",

"skills":"skills",

"runtime":"runtime",

"prompt":"prompt",

"memory":"memory",

"workflow":"workflow",

"template":"template",

"mcp":"mcp",

"config":"config"

}

for repo in ROOT.iterdir():

    if not repo.is_dir():
        continue

    result={}

    for k in KEYWORDS:

        result[k]=[]

    for f in repo.rglob("*"):

        p=str(f)

        lower=p.lower()

        for k,v in KEYWORDS.items():

            if v in lower:

                result[k].append(p)

    out=Path("knowledge/extracted")

    out.mkdir(exist_ok=True)

    with open(out/f"{repo.name}.yaml","w") as fp:

        yaml.dump(result,fp,sort_keys=False)

    print(repo.name,"done")
