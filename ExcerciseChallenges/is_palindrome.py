def is_palindrome(word):
    """checks word to see if it is a palindrome
    Parameters: str -> word - the word to check
    Returns: bool - True if palindrome, False if not
    """
    for index in range(len(word)):
        if word[index] != word[-(index + 1)]:
            return False
    return True


def is_palindrome_2(word):
    """checks word to see if it is a palindrome
    Parameters: str -> word - the word to check
    Returns: bool - True if palindrome, False if not
    """
    if word != word[::-1]:
        return False
    return True


def is_palindrome_3(word):
    """checks word to see if it is a palindrome
    Parameters: str -> word - the word to check
    Returns: bool - True if palindrome, False if not
    """
    if word != ''.join(list(reversed(word))):
        return False
    return True


def main():
    """the main entry for our program."""
    word = input("Please enter a word and I will tell you if it is a palindrome: ").lower()
    if word:
        # using an index
        print("{} is a palindrome: {}".format(word, is_palindrome(word)))
            
        # using string slicing
        print("{} is a palindrome: {}".format(word, is_palindrome_2(word)))

        # using bif reversed
        print("{} is a palindrome: {}".format(word, is_palindrome_3(word)))
        
    else:
        print("ERROR: you need to enter a word!")


if __name__ == '__main__':
    main()
