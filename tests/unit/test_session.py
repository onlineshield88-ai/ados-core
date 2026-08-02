import unittest, tempfile
from pathlib import Path
from unittest.mock import patch
import ados.core.session.session as session_module
from ados.core.session.session import Session

class TestSession(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.patcher = patch.object(session_module, 'ROOT', Path(self.temp_dir.name))
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()
        self.temp_dir.cleanup()

    def test_session_creation_and_append(self):
        session = Session()
        self.assertTrue((Path(self.temp_dir.name) / session.id).exists())
        
        session.append("user", "test_message")
        history = session.load()
        
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0]["role"], "user")
        self.assertEqual(history[0]["text"], "test_message")
