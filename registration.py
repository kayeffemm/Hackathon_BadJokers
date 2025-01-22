import sms_api
from sms_api import registersms


def validate_phone_number(phone_number):
    """
    Validates the phone number.
    :param phone_number: phone number input from user
    :return: valid phone number
    """
    if phone_number[0] == "+":
        valid_phone_number = phone_number.replace(phone_number[0], "")
        return valid_phone_number
    elif phone_number[0] == "0":
        valid_phone_number = "49" + phone_number[1:]
        return valid_phone_number
    else:
        valid_phone_number = phone_number
        return valid_phone_number


def main():
    registration = False
    while not registration:
        phone_number = input("Please enter your phone number: ")
        user_check_phone_number = input(f"Your phone number is {phone_number}.\nPlease enter 'y' (yes) to continue or 'n' (no) to enter the correct phone number. Enter 'q' to quit. ")
        if user_check_phone_number == "y":
            valid_phone_number = validate_phone_number(phone_number)
            registersms(valid_phone_number)
            registration = True
        elif user_check_phone_number == "n":
            continue
        elif user_check_phone_number == "q":
            break


if __name__ == "__main__":
    main()
