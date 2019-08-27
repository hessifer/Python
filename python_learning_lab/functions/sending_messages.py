#!/usr/bin/env python3

"""
    Copy the messages.py. Write a function called send_messages()
    that prints each text message and moves each message to a new list called
    sent_messages as it's printed. After calling the function, print both of 
    your lists to make sure the messages were moved correctly.
"""


def main():
    message_list = ['a star above', 'wonder twins activate', 'go go gadget go', 'i have the power']
    # show_messages(message_list)
    send_messages(message_list)
    print(f"Unsent Message List: {message_list}")


def show_messages(messages):
    for m in messages:
        print(f"{m}")


def send_messages(messages):
    sent_messages = []

    while messages:
        current_message = messages.pop(0)
        print(f"{current_message}")
        # sent_messages.append(current_message)
        sent_messages.append(current_message)

    print(f"Sent Messages List: {sent_messages}")


if __name__ == '__main__':
    main()
