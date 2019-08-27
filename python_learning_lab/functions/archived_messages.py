#!/usr/bin/env python3

"""
    Copy the sending_messages.py. Call the function send_messages() with a copy
    of the list of messages. After calling the function, print both of your
    lists to show that the original list has retained it's messages.
"""


def main():
    message_list = ['a star above', 'wonder twins activate', 'go go gadget go', 'i have the power']
    # show_messages(message_list)
    send_messages(message_list[:])
    print(f"Message List: {message_list}")


def show_messages(messages):
    for m in messages:
        print(f"{m}")


def send_messages(messages):
    sent_messages = []

    while messages:
        current_message = messages.pop(0)
        print(f"{current_message}")
        sent_messages.append(current_message)

    print(f"Sent Messages: {sent_messages}")


if __name__ == '__main__':
    main()
