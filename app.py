from json_manager import read_json, save_json
from sms_api import sendsms, receivesms
from storage.compare import compare_jsons, process_jsons
from time import sleep
from joke_api import get_joke


def analyze_message(message):
    valid_messages = ["1", "2a", "2b", "2c", "3"]
    return message in valid_messages


def choose_joke_method(prompt: str)
    match prompt:
        case "1":
            return get_joke()
        case "2b":
            pass
        case "2b":
            pass
        case "2c":
            pass
        case "3":
            pass


def main():
    filepath = ""
    old_json = json_manager.read_json(filepath) #returns python dict

    while True:
        new_json = receivesms()

        if old_json and compare_jsons(old_json, new_json):
            sleep(30)  # Wartezeit vor der nächsten Anfrage
            continue

        message_text, phone_number, new_json_to_save = process_jsons(old_json, new_json) #my part

        save_json(filepath, new_json_to_save)

        if analyze_message(message_text):
            new_text = choose_joke_method(message_text)
            sendsms(phone_number, "", new_text)
        else:
            sendsms(phone_number, menu)

        sleep(30)  # Wartezeit vor der nächsten Anfrage


if __name__ == "__main__":
    main()