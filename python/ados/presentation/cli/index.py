from ados.knowledge.indexer import SourceIndexer


def run(args):

    idx = SourceIndexer(".")

    files = idx.build()

    print()

    print("=" * 70)
    print("ADOS INDEX")
    print("=" * 70)

    for f in files:
        print(f)

    print()
    print(f"Total : {len(files)} files")
