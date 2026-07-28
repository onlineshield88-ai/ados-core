from ados.core.project import ProjectScanner


def main():

    scan=ProjectScanner(".")

    s=scan.summary()

    print()
    print("="*45)
    print("        ADOS PROJECT SCANNER")
    print("="*45)

    print()

    print("Project :",s["project"])
    print("Branch  :",s["branch"])
    print("Status  :",s["status"])

    print()

    print("Python   :",s["python"])
    print("Markdown :",s["markdown"])
    print("JSON     :",s["json"])
    print("YAML     :",s["yaml"])
    print("TOML     :",s["toml"])

    print()

    print("Modules")
    print("--------")

    for m in s["modules"]:
        print(" •",m)

    print()
    print("="*45)


if __name__=="__main__":
    main()
