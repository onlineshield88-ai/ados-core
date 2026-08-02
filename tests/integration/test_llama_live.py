import unittest, urllib.request
from ados.core.runtime.llama_runtime import LlamaRuntime

def is_up():
    try:
        urllib.request.urlopen("http://127.0.0.1:8080/health", timeout=1)
        return True
    except:
        return False

@unittest.skipUnless(is_up(), "llama-server offline, skipping live test")
class TestLlamaLive(unittest.TestCase):
    def test_live_health(self):
        self.assertTrue(LlamaRuntime().health())
