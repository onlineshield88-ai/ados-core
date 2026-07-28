import sys
from pathlib import Path

def main():
    root = Path.cwd()
    index_dir = root / '.ados' / 'index'
    
    sys.path.insert(0, str(root / 'python'))
    
    from ados.knowledge import IndexBuilder
    
    builder = IndexBuilder(str(root), str(index_dir))
    summary = builder.build()
    
    print("\n=== Index Summary ===")
    for key, value in summary.items():
        print(f"{key}: {value}")
    print(f"\nIndex saved to: {index_dir}")

if __name__ == '__main__':
    main()
