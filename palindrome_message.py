"""Checks if enter message is a palindrome"""

def main():
    message = input('Enter a message: ').lower()
    message_clean = message

    # remove unwanted spaces and punctuations
    for c in ' ,.?':
        message_clean = message_clean.replace(c, "")

    if message_clean == message_clean[::-1]:
        print('The message is a palindrome.')

if __name__ == '__main__':
    main()