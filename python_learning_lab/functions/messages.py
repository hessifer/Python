#!/usr/bin/env python3

""" Make a list containing a series of short text messages.
    Pass the list to a function called show_messages(), which
    prints each text message.
"""


def main():
    message_list = ['a star above', 'wonder twins activate', 'go go gadget go', 'i have the power']
    show_messages(message_list)


def show_messages(messages):
    for m in messages:
        print(f"{m}")


if __name__ == '__main__':
    main()
