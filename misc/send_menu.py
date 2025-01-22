from api import sms_api


def send_menu(phonenumber):

    menu_message = """Welcome to BadJokers! Please choose an option:\n
         1. Random Joke\n
         2. Joke from category\n
            a = Misc
            b = Programming
            c = Dark
            d = Pun
            example: 2a (for 'Misc')\n"""

    print(menu_message)


    sms_api.sendsms(phonenumber, message=menu_message)


if __name__ == "__main__":
    send_menu()