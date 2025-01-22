import requests
from time import sleep


def fetch_sms_api():
    # Simuliere Anfrage an SMS-API
    response = requests.get("https://sms-api.example.com/get")
    return response.json()


def compare_jsons(old_json, new_json):
    return old_json == new_json


def process_jsons(old_json, new_json):
    # Simuliere Verarbeitung der JSON-Daten
    message_text = "Neuer Inhalt erkannt"
    phone_number = "1234567890"
    return message_text, phone_number, new_json


def analyze_message(message_text):
    # Simuliere Analyse des Nachrichtentexts
    return "richtig" in message_text.lower()


def communicate_with_jokes_api():
    # Simuliere Kommunikation mit der Jokes-API
    response = requests.get("https://jokes.api/example")
    return response.json().get("joke")


def send_sms(phone_number, message_text=None):
    # Simuliere das Senden einer SMS
    if message_text:
        print(f"SMS an {phone_number}: {message_text}")
    else:
        print(f"SMS an {phone_number}: Standardnachricht")


def main():
    filepath = ""
    old_json = read_json(filepath) #returns python dict

    while True:
        new_json = fetch_sms_api()

        if old_json and compare_jsons(old_json, new_json):
            sleep(5)  # Wartezeit vor der nächsten Anfrage
            continue

        message_text, phone_number, new_json_to_save = process_jsons(old_json, new_json) #my part
        save_json(filepath, new_json_to_save)

        if analyze_message(message_text):
            new_text = communicate_with_jokes_api(message_text)
            send_sms(phone_number, new_text)
        else:
            send_sms(phone_number, rules)

        sleep(5)  # Wartezeit vor der nächsten Anfrage


if __name__ == "__main__":
    main()
