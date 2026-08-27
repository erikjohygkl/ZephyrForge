# test_zephyrforge.py
"""
Tests for ZephyrForge module.
"""

import unittest
from zephyrforge import ZephyrForge

class TestZephyrForge(unittest.TestCase):
    """Test cases for ZephyrForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZephyrForge()
        self.assertIsInstance(instance, ZephyrForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZephyrForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
