import unittest
from ados.core.kernel.kernel import Kernel

class TestKernel(unittest.TestCase):
    def test_kernel_initialization(self):
        kernel = Kernel()
        self.assertTrue(hasattr(kernel, 'register'))
        self.assertIsNotNone(kernel)
