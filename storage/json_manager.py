import json

def dict_store(filepath):
    my_dict = { }

    with open(filepath, 'w') as f:
        json.dump(my_dict, f)
        print("Dict wurde als JSON gespeichert.")

    with open(filepath, 'r') as f:
        loaded_dict = json.load(f)
        print("Geladenes Dictionary:", loaded_dict)

    for key, value in loaded_dict.items():
        print(f"{key}: {value}")



def content_json(filepath, key="number"):
    """
    Extrahiert den Wert eines bestimmten Schlüssels aus einer JSON-Datei.

    Args:
        filepath (str): Der Pfad zur JSON-Datei.
        key (str, optional): Der Schlüssel, dessen Wert extrahiert werden soll. Defaults to "joke".

    Returns:
        str: Der Wert des angegebenen Schlüssels oder None, wenn der Schlüssel nicht gefunden wurde.
    """

    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data.get(key)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Fehler beim Lesen der JSON-Datei: {e}")
        return None

# Beispielaufruf:
joke_content = content_json("jokes.json")
if joke_content:
    print(joke_content)
else:
    print("Witz konnte nicht gefunden werden.")



