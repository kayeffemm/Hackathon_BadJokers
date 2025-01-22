import time
import json


def load_json():
    try:
        with open('store.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"latest_request": None}

def save_json(data):
    with open('store.json', 'w') as file:
        json.dump(data, file)

def receivesms():
    return {"number": "+491234567890", "text": "1"}

def send_sms(number, text):
    print(f"Sending SMS to {number}: {text}")

def main():
    print("Starting program...")

    while True:
        new_request = receivesms()
        data = load_json()

        if data["latest_request"] == new_request:
            print("No new request. Waiting...")
            time.sleep(30)
            continue

        data["latest_request"] = new_request
        save_json(data)

        user_choice = new_request["text"]
        user_number = new_request["number"]

        if user_choice == "1":
            send_sms(user_number, "Random joke: Why did the chicken go to the barber?")
        elif user_choice.startswith("2="):
            category = user_choice.split("=")[1]
            send_sms(user_number, f"Joke from category {category}")
        elif user_choice.startswith("3="):
            keyword = user_choice.split("=")[1]
            send_sms(user_number, f"Joke with keyword '{keyword}'")
        else:
            send_sms(user_number, "Invalid input. Try again.")

if __name__ == "__main__":
    main()
