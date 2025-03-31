"""
Default Algorithm Module
This module provides a default algorithm implementation that returns a standard response.
"""
import json
import logging
import sys
from pathlib import Path

# Use the centralized logging system
sys.path.append(str(Path(__file__).parent.parent.parent.parent))
try:
    from logger_config import get_logger
    logger = get_logger(__name__)
except ImportError:
    # Fallback if logger_config isn't available
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

def run(data):
    """
    Process the input data and return a standard JSON response.
    
    Args:
        data (dict): Input data to process
        
    Returns:
        dict: Processing results
    """
    logger.info(f"Processing input data with Default Algorithm")
    
    # Log information about the input
    try:
        input_type = data.get("input_type", "unknown")
        input_data = data.get("input", {})
        
        if isinstance(input_data, (dict, list)):
            input_size = len(json.dumps(input_data))
            logger.info(f"Input is {type(input_data).__name__} with size {input_size} bytes")
        elif isinstance(input_data, str):
            logger.info(f"Input is string with length {len(input_data)}")
        else:
            logger.info(f"Input is of type {type(input_data).__name__}")
    except Exception as e:
        logger.warning(f"Couldn't analyze input data: {str(e)}")
    
    # Return standard response in the required format
    return {
        "status": "success",
        "message": "Default algorithm execution completed successfully",
        "results": {
            "received_input": input_data if not isinstance(input_data, str) or len(str(input_data)) < 1000 
                            else f"{str(input_data)[:100]}... (truncated)",
            "default_output": {
                "value": 42,
                "description": "This is a default response"
            }
        }
    }

# For direct script execution
if __name__ == "__main__":
    # Example test with sample input
    test_data = {
        "input_type": "data",
        "input": {"test": "data"},
        "metadata": {"source": "test"}
    }
    result = run(test_data)
    print(json.dumps(result, indent=2))
