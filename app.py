from misc.send_menu import send_menu
from storage.json_manager import save_json, read_json
from api.sms_api import sendsms, receivesms
from storage.compare import process_jsons
from time import sleep
from api.joke_api import get_joke, get_category


JSON_FILEPATH = "data/badjokers.json"


def analyze_message(message):
    valid_messages = ["1", "2a", "2b", "2c", "2d"]
    return message in valid_messages


def choose_joke_method(prompt: str):
    match prompt:
        case "1":
            return get_joke()
        case "2a":
            return get_category("misc")
        case "2b":
            return get_category("Programming")
        case "2c":
            return get_category("Dark")
        case "2d":
            return get_category("Pun")


def main():
    while True:
        old_json = read_json(JSON_FILEPATH)
        #print(old_json)
        new_json = receivesms()

        phone_number, message_text, new_json_to_save = process_jsons(old_json, new_json)

        print(message_text, phone_number)
        save_json(JSON_FILEPATH, new_json_to_save)

        if analyze_message(message_text):
            new_text = choose_joke_method(message_text)
            print(new_text)
            sendsms(phone_number, "", new_text)
        elif message_text is not None:
            send_menu(phone_number)
        else:
            print("sleeping...")
            sleep(30)


if __name__ == "__main__":
    main()