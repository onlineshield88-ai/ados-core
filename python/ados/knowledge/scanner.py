import os
from pathlib import Path
from typing import List, Dict

class ProjectScanner:
    def __init__(self, root: str):
        self.root = Path(root)
        self.files: Dict[str, Dict] = {}
        self.python_files: List[str] = []
        self.doc_files: List[str] = []
        self.config_files: List[str] = []

    def scan(self) -> Dict[str, List[str]]:
        for root, dirs, files in os.walk(self.root):
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__', 'node_modules']]
            
            for file in files:
                path = Path(root) / file
                rel_path = str(path.relative_to(self.root))
                
                if file.endswith('.py'):
                    self.python_files.append(rel_path)
                elif file.endswith(('.md', '.rst', '.txt')):
                    self.doc_files.append(rel_path)
                elif file.endswith(('.yaml', '.yml', '.toml', '.json')):
                    self.config_files.append(rel_path)
                elif file in ['README', 'LICENSE', '.gitignore']:
                    self.doc_files.append(rel_path)
        
        return {
            'python': self.python_files,
            'docs': self.doc_files,
            'config': self.config_files
        }

    def read_file(self, rel_path: str) -> str:
        path = self.root / rel_path
        try:
            return path.read_text(encoding='utf-8')
        except:
            return ""
