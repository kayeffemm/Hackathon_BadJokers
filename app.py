from storage.json_manager import save_json
from api.sms_api import sendsms, receivesms
from storage.compare import compare_jsons, process_jsons
from time import sleep
from api.joke_api import get_joke, get_category, get_keyword


def analyze_message(message):
    valid_messages = ["1", "2a", "2b", "2c", "3"]
    return message in valid_messages


def choose_joke_method(prompt: str)
    match prompt:
        case "1":
            return get_joke()
        case "2b":
            return get_category("misc")
        case "2b":
            return get_category("Programming")
        case "2c":
            return get_category("Dark")
        case "2d":
            return get_category("Pun")
        case "2e":
            return get_category("Spooky")
        case "2f":
            return get_category("Christmas")
        case "3":
            return get_keyword("")


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