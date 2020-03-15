"""Checks if enter message is a palindrome"""


def is_palindrome(message):
    message_clean = message

    # remove unwanted spaces and punctuations
    for c in ' ,.?':
        message_clean = message_clean.replace(c, "")

    if message_clean == message_clean[::-1]:
        return True
    return False


def main():
    message = input('Enter a message: ').lower()

    if is_palindrome(message):
        print('The message is a palindrome.')
    else:
        print('The message is not a palindrome.')


if __name__ == '__main__':
    import timeit
    print(timeit.timeit('is_palindrome("bob")', setup="from __main__ import is_palindrome"))
    # main()
