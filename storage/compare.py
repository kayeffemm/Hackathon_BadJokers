from datetime import datetime

def compare_json(old_json, new_json):
    oldest_message = None
    oldest_timestamp = None
    oldest_number = None

    for number, messages in new_json.items():
        old_messages = old_json.get(number, [])
        old_timestamps = {msg['receivedAt'] for msg in old_messages}

        for msg in messages:
            if msg['receivedAt'] not in old_timestamps:
                msg_timestamp = datetime.fromisoformat(msg['receivedAt'].replace('Z', '+00:00'))
                if oldest_timestamp is None or msg_timestamp < oldest_timestamp:
                    oldest_timestamp = msg_timestamp
                    oldest_message = msg
                    oldest_number = number

    if oldest_message:
        # Return the text and the phone number of the oldest new message
        return oldest_message['text'], oldest_number, oldest_timestamp

def update_json(old_json, new_entry, phone_number):
    new_json = old_json
    if phone_number not in new_json:
        new_json[phone_number] = []
    new_json[phone_number].append(new_entry)
    return new_json

# Example usage
old_json2 = {
    # Your old JSON structure here
    "491781844175": [
        {
            "text": "Test",
            "receivedAt": "2025-01-20T13:11:43.306+0000"
        }
    ]
}

new_json2 = {
    # Your new JSON structure here
    "491781844175": [
        {
            "text": "Test",
            "receivedAt": "2025-01-20T13:11:43.306+0000"
        },
        {
            "text": "GitHub ist ...",
            "receivedAt": "2025-01-20T13:17:44.148+0000"
        },
        {
            "text": "Kurznachricht",
            "receivedAt": "2025-01-21T08:27:50.460+0000"
        },
        {
            "text": "Es ist 11:56",
            "receivedAt": "2023-01-21T10:55:35.538+0000"
        }
    ]
}


def main():
    # Find the oldest new message
    message_text, phone_number, oldest_timestamp = compare_json(old_json2, new_json2)

    new_entry = {
        "text": message_text,
        "receivedAt": oldest_timestamp.isoformat()
    }
    # Update the old JSON with the oldest new message
    print(old_json2)
    updated_json = update_json(old_json2, new_entry, phone_number)

    # check variables
    print(f"Message Text = {message_text} \nphone_number = {phone_number} \noldest_timestamp = {oldest_timestamp}")
    print(updated_json)


if __name__ == "__main__":
    main()