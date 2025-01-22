TEAM = "BadJokers"


def validate_phone_number(phone_number):
    """
    Validates the phone number.
    :param phone_number: phone number input from user
    :return: valid phone number
    """
    if phone_number[0] == "+":
        valid_phone_number = phone_number.replace("+", "")
        return valid_phone_number
    elif phone_number[0] == "0":
        valid_phone_number = phone_number.replace("0", "49")
        return valid_phone_number
    else:
        valid_phone_number = phone_number
        return valid_phone_number


def phone_number_registration(valid_phone_number):
    """
    Register the validated phone number in the TEAM and sends
    an SMS to the phone number if registration was successful.
    :param valid_phone_number: the validated phone number from func validate_phone_number
    :return:
    """
    pass


def main():
    phone_number = input("Please enter your phone number: ")
    print(f"TEST validate_phone_number: {validate_phone_number(phone_number)}")


if __name__ == "__main__":
    main()
