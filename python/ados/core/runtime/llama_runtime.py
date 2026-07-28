import json
import urllib.request
import urllib.error

class LlamaRuntime:

    name="llama-server"

    def __init__(self):

        self.url="http://127.0.0.1:8080/completion"

    def health(self):

        try:
            urllib.request.urlopen("http://127.0.0.1:8080/health",timeout=2)
            return True
        except:
            return False

    def generate(self, prompt):

        chat = f"""<|im_start|>system
You are ADOS AI Development Operating System.
Answer clearly and concisely.
<|im_end|>
<|im_start|>user
{prompt}
<|im_end|>
<|im_start|>assistant
"""

        payload = {

            "prompt": chat,

            "n_predict": 256,

            "temperature": 0.2,

            "top_p": 0.95,

            "repeat_penalty": 1.1,

            "stop": [
                "<|im_end|>",
                "</s>",
                "<|endoftext|>"
            ],

            "cache_prompt": True

        }

        req = urllib.request.Request(
            self.url,
            data=json.dumps(payload).encode(),
            headers={
                "Content-Type": "application/json"
            }
        )

        with urllib.request.urlopen(req, timeout=600) as r:
            result = json.loads(r.read().decode())

        return result["content"].strip()
