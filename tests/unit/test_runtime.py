import unittest
from unittest.mock import patch, MagicMock
from ados.core.runtime.llama_runtime import LlamaRuntime

class TestRuntime(unittest.TestCase):
    @patch('urllib.request.urlopen')
    def test_health_success(self, mock_urlopen):
        mock_resp = MagicMock()
        mock_resp.status = 200
        mock_urlopen.return_value.__enter__.return_value = mock_resp
        self.assertTrue(LlamaRuntime().health())

    @patch('urllib.request.urlopen')
    def test_health_failure(self, mock_urlopen):
        mock_urlopen.side_effect = Exception("Connection refused")
        self.assertFalse(LlamaRuntime().health())

    @patch('urllib.request.urlopen')
    @patch.object(LlamaRuntime, 'health', return_value=True)
    def test_generate(self, mock_health, mock_urlopen):
        mock_resp = MagicMock()
        mock_resp.status = 200
        mock_resp.read.return_value = b'{"content": "mock response"}'
        mock_urlopen.return_value.__enter__.return_value = mock_resp
        
        res = LlamaRuntime().generate("hello")
        self.assertEqual(res, "mock response")
