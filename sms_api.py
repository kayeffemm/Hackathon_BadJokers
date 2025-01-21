import requests
import json


def sendsms(phone_number, sender="", message="no text available"):
    """
    Erster Versuch

    Arguments:
        phone_number (str): In dem Falle meine eigene
        message (str): Testnachricht
        sender (str, optional): SenderName Defaults to "".

    Returns:
        dict: Die Antwort der API.
    """

    url = "http://hackathons.masterschool.com:3030/sms/send"
    headers = {"Content-Type": "application/json"}
    payload = {
        "phoneNumber": phone_number,
        "message": message,
        "sender": sender
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            print("SMS sent successfully to Team 'BadJokers'!")
        else:
            print(f"Failed to send SMS. Status Code: {response.status_code}")
        return response.json()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def receivesms():
    url = f"http://hackathons.masterschool.com:3030/team/getMessages/BadJokers"
    headers = {"Content-Type": "application/json"}  # Header setze
    try:
        # GET-Request senden
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            print("Messages retrieved successfully!")
            return response.json()
        else:
            print(f"Failed to retrieve messages. Status Code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main():

    sendsms(phone_number, sender, sms_message)

    if __name__ == "__main__":
        main()