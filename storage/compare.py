from datetime import datetime


def process_jsons(old_data, new_data):
    """
    Compare two JSON-like dictionaries, find the oldest new entry, and update the old data.

    Args:
        old_data (dict): Dictionary representing the old JSON data.
        new_data (dict): Dictionary representing the new JSON data.

    Returns:
        tuple: A tuple containing:
            - str: The phone number of the relevant new entry.
            - str: The text from this entry.
            - dict: The updated old_data dictionary.
            If no new entry is found, returns (None, None, old_data).
    """
    oldest_entry = None
    oldest_timestamp = None

    # Compare entries and find the oldest new one
    for number, messages in new_data.items():
        old_messages = old_data.get(number, [])
        old_texts = {msg['text'] for msg in old_messages}

        # Identify new messages
        new_messages = [msg for msg in messages if msg['text'] not in old_texts]

        for message in new_messages:
            message_time = datetime.fromisoformat(message['receivedAt'][:-5])

            if oldest_timestamp is None or message_time < oldest_timestamp:
                oldest_entry = {"number": number, "text": message['text']}
                oldest_timestamp = message_time

    # If no new messages were found, return None for the first two return values
    if not oldest_entry:
        return None, None, old_data

    # Update the old data with the oldest new entry
    number = oldest_entry["number"]
    text = oldest_entry["text"]
    old_data[number] = old_data.get(number, []) + [
        msg for msg in new_data[number] if msg['text'] == text
    ]

    return number, text, old_data