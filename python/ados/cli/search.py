import sys
import json
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m ados.cli.search <query>")
        sys.exit(1)
    
    query = sys.argv[1]
    root = Path.cwd()
    index_dir = root / '.ados' / 'index'
    
    sys.path.insert(0, str(root / 'python'))
    
    from ados.knowledge import IndexLoader, SymbolSearcher
    
    loader = IndexLoader(str(index_dir))
    searcher = SymbolSearcher(loader)
    results = searcher.search_symbol(query)
    
    print(f"\n=== Search Results for '{query}' ===")
    print(json.dumps(results, indent=2))

if __name__ == '__main__':
    main()
