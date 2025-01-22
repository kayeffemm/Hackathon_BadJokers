import json
import os


def save_json(file_path, new_json: dict):
    """
    Saves a dictionary as a JSON file to the specified file path.
    """

    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_dir, '..', file_path)  # Navigate to the project root

    try:
        # Ensure the target directory exists
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        # Save the dictionary as JSON
        with open(full_path, 'w') as f:
            json.dump(new_json, f, indent=4)
    except Exception as e:
        raise OSError(f"Failed to save JSON to {full_path}: {e}")

def read_json(file_path):
    """
    Reads and returns the contents of a JSON file.
    """

    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_dir, '..', file_path)  # Navigate to the project root

    try:
        # Open and load the JSON file
        with open(full_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"JSON file not found: {full_path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format in file {full_path}: {e}")