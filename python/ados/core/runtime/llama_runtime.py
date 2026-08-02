import urllib.request
import json
import logging

class LlamaRuntime:
    def __init__(self, host="127.0.0.1", port=8080):
        self.base_url = f"http://{host}:{port}"

    def health(self) -> bool:
        """Check if the local llama-server is responding."""
        try:
            req = urllib.request.Request(f"{self.base_url}/health")
            with urllib.request.urlopen(req, timeout=2) as response:
                return response.status == 200
        except Exception:
            return False

    def generate(self, prompt: str) -> str:
        """Generate a response using the local llama.cpp server API."""
        if not self.health():
            return "Error: Local Qwen model at 127.0.0.1:8080 is not reachable."
            
        try:
            data = json.dumps({
                "prompt": prompt,
                "n_predict": 512,
                "temperature": 0.2,
                "stop": ["</s>", "<|im_end|>", "<|im_start|>"]
            }).encode('utf-8')
            
            req = urllib.request.Request(
                f"{self.base_url}/completion",
                data=data,
                headers={'Content-Type': 'application/json'}
            )
            
            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read().decode('utf-8'))
                return result.get('content', '').strip()
        except Exception as e:
            logging.error(f"Generation failed: {e}")
            return f"Error during generation: {e}"
