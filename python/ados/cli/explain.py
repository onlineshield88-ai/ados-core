import sys
import json
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m ados.cli.explain <symbol>")
        sys.exit(1)
    
    symbol = sys.argv[1]
    root = Path.cwd()
    index_dir = root / '.ados' / 'index'
    
    sys.path.insert(0, str(root / 'python'))
    
    from ados.knowledge import IndexLoader, SymbolExplainer
    
    loader = IndexLoader(str(index_dir))
    explainer = SymbolExplainer(loader)
    
    result = None
    for method_name in ['explain_module', 'explain_class', 'explain_function']:
        method = getattr(explainer, method_name)
        result = method(symbol)
        if result:
            break
    
    if result:
        print(f"\n=== Explanation for '{symbol}' ===")
        print(json.dumps(result, indent=2))
    else:
        print(f"Symbol '{symbol}' not found in index")

if __name__ == '__main__':
    main()
