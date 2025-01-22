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


def store_json(filepath, new_data, key='id'):
    """Speichert ein Dictionary als JSON-Datei und verhindert Duplikate anhand des angegebenen Schlüssels.

    Args:
        filepath (str): Der Pfad zur Datei.
        new_data (dict): Das neue Dictionary, das hinzugefügt werden soll.
        key (str, optional): Der Schlüssel, der zur Identifizierung von Duplikaten verwendet wird.
    """
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    if key not in new_data:
        raise ValueError(f"Das neue Datenelement muss den Schlüssel '{key}' enthalten.")


    if new_data[key] not in data:
        data[new_data[key]] = new_data
    else:
        print(f"Duplikat gefunden für Schlüssel '{key}': {new_data[key]}")

    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def load_json(filepath, key=None):
    """Lädt eine JSON-Datei und gibt entweder das gesamte Dictionary oder einen bestimmten Eintrag zurück.

    Args:
        filepath (str): Der Pfad zur Datei.
        key (str, optional): Der Schlüssel des zu ladenden Eintrags.
    """
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Datei '{filepath}' nicht gefunden.")
        return None

def find_duplicates(data, key):
    """Findet Duplikate in einem Dictionary basierend auf einem bestimmten Schlüssel.

    Args:
        data (dict): Das Dictionary, in dem nach Duplikaten gesucht werden soll.
        key (str): Der Schlüssel, der zur Identifizierung von Duplikaten verwendet wird.

    Returns:
        list: Eine Liste von Duplikaten.
    """
    seen = set()
    duplicates = []
    for item in data.values():
        if item[key] in seen:
            duplicates.append(item)
        else:
            seen.add(item[key])
    return duplicates
