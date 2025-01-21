import json
from datetime import datetime


def correct_content():


    # Erstelle ein Dictionary für die neue SMS
    new_sms = {
            'from': from_number,
            'body': body,
            'timestamp': datetime.now().isoformat()
    }

    def store_json(new_sms):
        """Speichert die neue SMS in einer JSON-Datei und führt einen Vergleich durch."""

        try:
            with open('store.json', 'r') as f:
                store = json.load(f)
        except FileNotFoundError:
            # Wenn die Datei noch nicht existiert, erstelle eine leere Liste
            store = []

        # Prüfe, ob die SMS bereits existiert (basierend auf 'from' und 'body')
        exists = False
        for sms in store:
            if sms['from'] == from_number and sms['body'] == body:
                exists = True
                break

        if not exists:
            # Füge die neue SMS nur hinzu, wenn sie noch nicht vorhanden ist
            store.append(new_sms)

            # Speichere die aktualisierten Daten in der JSON-Datei
            with open('store.json', 'w') as f:
                json.dump(store, f, indent=4)
            return True  # Gibt zurück, ob die SMS hinzugefügt wurde
        else:
            return False  # Gibt zurück, dass die SMS bereits vorhanden ist




