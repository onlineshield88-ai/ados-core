import unittest
import urllib.request
from ados.core.runtime.llama_runtime import LlamaRuntime

def is_llama_up():
    try:
        urllib.request.urlopen("http://127.0.0.1:8080/health", timeout=1)
        return True
    except:
        return False

@unittest.skipUnless(is_llama_up(), "llama-server is not reachable at 127.0.0.1:8080")
class TestLlamaLive(unittest.TestCase):
    def test_live_health(self):
        runtime = LlamaRuntime()
        self.assertTrue(runtime.health())
        
    def test_live_generation(self):
        runtime = LlamaRuntime()
        res = runtime.generate("Hello integration test")
        self.assertIsNotNone(res)
