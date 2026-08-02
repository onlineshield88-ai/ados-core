import unittest
from ados.knowledge.context.context_engine import ContextEngine

class TestContext(unittest.TestCase):
    def test_context_engine_initialization(self):
        engine = ContextEngine()
        self.assertIsNotNone(engine)
