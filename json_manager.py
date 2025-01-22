import json

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

# Beispiel:
data1 = {'id': 1, 'name': 'Alice', 'age': 30}  # Duplikat der ID 1

store_json('data.json', data1, 'id')
store_json('data.json', data2, 'id')
try:
    store_json('data.json', data2, 'id')
except ValueError as e:
    print(e)

all_data = load_json('data.json')
duplicates = find_duplicates(all_data, 'id')
print("Duplikate:", duplicates)
