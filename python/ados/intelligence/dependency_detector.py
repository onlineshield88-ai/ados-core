from pathlib import Path
import yaml

ROOT=Path("external/cache")
OUT=Path("knowledge/dependencies")

OUT.mkdir(exist_ok=True)

FILES=[

"requirements.txt",
"pyproject.toml",
"package.json",
"go.mod",
"Cargo.toml",
"composer.json",
"pom.xml",
"build.gradle",
"Gemfile"

]

for repo in ROOT.iterdir():

    if not repo.is_dir():
        continue

    deps=[]

    for f in repo.rglob("*"):

        if f.name in FILES:

            deps.append(str(f.relative_to(repo)))

    with open(OUT/f"{repo.name}.yaml","w") as fp:

        yaml.dump({

            "repository":repo.name,

            "dependency_files":deps,

            "count":len(deps)

        },fp,sort_keys=False)

    print(repo.name,len(deps))
