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
    headers = {"Content-Type": "application/json"}
    try:
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


def registersms(phone_number):
    """
    Registers a phone number to the team BadJokers. Team name is fix.

    Arguments:
        phone_number (str): The phone number to register (with country code, without "+" sign).

    Returns:
        bool: True if registration is successful, False otherwise.
    """
    url = "http://hackathons.masterschool.com:3030/team/registerNumber"
    headers = {"Content-Type": "application/json"}
    team_name = "BadJokers"
    payload = {
        "phoneNumber": phone_number,
        "teamName": team_name
    }

    try:
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            print(f"Phone number {phone_number} successfully registered to team '{team_name}'!")
            return True
        else:
            print(f"Failed to register phone number. Status Code: {response.status_code}, Response: {response.text}")
            return False
    except Exception as e:
        print(f"An error occurred during registration: {e}")
        return False


def main():

    sendsms(phone_number, sender, sms_message)
    receivesms()
    registersms()

    if __name__ == "__main__":
        main()