from ados.knowledge.search.search import SearchEngine


def run(args):

    if not args:
        print("Usage:")
        print("  ados search <keyword>")
        return

    engine = SearchEngine(".")

    results = engine.search(args[0])

    if not results:
        print("No matches.")
        return

    print()

    print("=" * 70)

    print(f"Found {len(results)} matches")

    print("=" * 70)

    for r in results:

        print(
            f"{r['file']}:{r['line']}"
        )

        print(
            f"    {r['text']}"
        )

        print()
