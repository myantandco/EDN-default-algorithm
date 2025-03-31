"""
Unit tests for the default algorithm
"""
import unittest
import json
import sys
from pathlib import Path

# Add the src directory to the path so we can import the algorithm
sys.path.append(str(Path(__file__).parent.parent / "src" / "release" / "latest"))
from algorithm import run

class TestDefaultAlgorithm(unittest.TestCase):
    """Tests for the algorithm."""
    
    def test_run_with_dict_input(self):
        """Test algorithm execution with dictionary input."""
        test_input = {
            "input_type": "data",
            "input": {"test": "data"}
        }
        result = run(test_input)
        
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["results"]["received_input"], test_input["input"])
    
    def test_run_with_string_input(self):
        """Test algorithm execution with string input."""
        test_input = {
            "input_type": "data",
            "input": "test string data"
        }
        result = run(test_input)
        
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["results"]["received_input"], test_input["input"])
    
    def test_run_with_large_string_input(self):
        """Test algorithm execution with large string input."""
        test_input = {
            "input_type": "data",
            "input": "x" * 2000  # String longer than 1000 chars
        }
        result = run(test_input)
        
        self.assertEqual(result["status"], "success")
        self.assertTrue(len(result["results"]["received_input"]) < len(test_input["input"]))
        self.assertTrue("truncated" in result["results"]["received_input"])

if __name__ == "__main__":
    unittest.main()
