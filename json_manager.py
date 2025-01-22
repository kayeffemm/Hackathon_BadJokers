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

def content_json

dict_store()

