from misc.send_menu import send_menu
from storage.json_manager import save_json, read_json
from api.sms_api import sendsms, receivesms
from storage.compare import process_jsons
from time import sleep
from api.joke_api import get_joke, get_category


JSON_FILEPATH = "data/badjokers.json"


def analyze_message(message):
    valid_messages = ["1", "2a", "2b", "2c", "3"]
    return message in valid_messages


def choose_joke_method(prompt: str):
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
    while True:
        old_json = read_json(JSON_FILEPATH)
        print(old_json)
        new_json = receivesms()

        if old_json and old_json == new_json:
            sleep(30)
            continue

        message_text, phone_number, new_json_to_save = process_jsons(old_json, new_json)

        print(message_text, phone_number)
        save_json(JSON_FILEPATH, new_json_to_save)

        if analyze_message(message_text):
            new_text = choose_joke_method(message_text)
            sendsms(phone_number, "", new_text)
        else:
            send_menu(phone_number)

        sleep(30)


if __name__ == "__main__":
    main()