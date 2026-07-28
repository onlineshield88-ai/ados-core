import os
import sys
import ast
from pathlib import Path
from collections import defaultdict

def audit_package(package_path):
    print("\n" + "="*50)
    print("KNOWLEDGE ENGINE AUDIT REPORT")
    print("="*50)
    
    issues = {
        'modules': [],
        'duplicates': [],
        'circular': [],
        'missing_apis': [],
        'dead_files': [],
        'import_issues': []
    }
    
    py_files = list(Path(package_path).glob('*.py'))
    print(f"\nTotal Python files: {len(py_files)}")
    print("Modules:")
    for f in sorted(py_files):
        print(f"  - {f.name}")
        issues['modules'].append(f.name)
    
    imports_graph = defaultdict(set)
    defined_names = defaultdict(set)
    
    for py_file in py_files:
        try:
            with open(py_file) as f:
                tree = ast.parse(f.read())
            
            module_name = py_file.stem
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imports_graph[module_name].add(alias.name.split('.')[0])
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        imports_graph[module_name].add(node.module.split('.')[0])
                elif isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                    defined_names[module_name].add(node.name)
        except Exception as e:
            issues['import_issues'].append(f"{py_file.name}: {str(e)}")
    
    # Check for circular imports
    def has_circular(graph, start, visited, rec_stack):
        visited.add(start)
        rec_stack.add(start)
        
        for neighbor in graph.get(start, set()):
            if neighbor not in graph or neighbor.startswith('_'):
                continue
            if neighbor not in visited:
                if has_circular(graph, neighbor, visited, rec_stack):
                    return True
            elif neighbor in rec_stack:
                issues['circular'].append(f"{start} -> {neighbor}")
        
        rec_stack.remove(start)
        return False
    
    visited = set()
    for module in imports_graph:
        if module not in visited:
            has_circular(imports_graph, module, visited, set())
    
    print(f"\nCircular imports found: {len(issues['circular'])}")
    for circular in issues['circular']:
        print(f"  - {circular}")
    
    print(f"\nImport issues: {len(issues['import_issues'])}")
    for issue in issues['import_issues']:
        print(f"  - {issue}")
    
    return issues

if __name__ == '__main__':
    audit_package('python/ados/knowledge')
