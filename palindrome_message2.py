"""Check a message to see if it is a palindrome."""


def main():
    message = input('Enter a message: ').lower()
    message_clean = message
    strip_these = ['"', "'", '!', '.', '?', '$', '%']
    palindrome = True

    # strip message of unwanted spaces and punctuation
    for c in strip_these:
        message_clean = message_clean.replace(c, "")

    # get last pos of message_clean
    mc_last_pos = len(message_clean) - 1

    # get middle pos of message_clean
    mc_mid_pos = mc_last_pos // 2

    # compare letters one by one
    for i in range(mc_mid_pos + 1):
        if message_clean[i] != message_clean[mc_last_pos]:
            palindrome = False
            break
        mc_last_pos -= 1


    if palindrome:
        print('The message entered is a palindrome.')
    else:
        print('The message entered was not a palindrome.')


if __name__ == '__main__':
    main()
