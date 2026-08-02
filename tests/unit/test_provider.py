import unittest
from unittest.mock import patch
from ados.core.providers.router import ProviderRouter
from ados.core.providers.local.qwen import QwenProvider

class TestProvider(unittest.TestCase):
    @patch.object(QwenProvider, 'available', return_value=True)
    def test_router_healthy(self, mock_available):
        provider = ProviderRouter().select()
        self.assertIsInstance(provider, QwenProvider)

    @patch.object(QwenProvider, 'available', return_value=False)
    def test_router_unhealthy(self, mock_available):
        with self.assertRaises(RuntimeError):
            ProviderRouter().select()
