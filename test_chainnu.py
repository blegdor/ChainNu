# test_chainnu.py
"""
Tests for ChainNu module.
"""

import unittest
from chainnu import ChainNu

class TestChainNu(unittest.TestCase):
    """Test cases for ChainNu class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChainNu()
        self.assertIsInstance(instance, ChainNu)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChainNu()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
