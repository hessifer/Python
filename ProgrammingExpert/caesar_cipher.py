def caesar_cipher(string, offset):
    # write a function that accepts a string and returns the caesar cipher
    # encoding of that string according to a secondary input parameter
    # offset will always be a positive integer that is no greater than
    # 26 and the input string will contain only lowercase letters

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                'x', 'y', 'z']

    # calculate caesar cipher
    encrypted = []

    for c in string:
        idx = alphabet.index(c)
        letter = alphabet[idx - offset]
        encrypted.append(letter)
    
    return "".join(encrypted)

def main():
    print(caesar_cipher("hello", 3))
    print(caesar_cipher("apple", 5))


if __name__ == "__main__":
    main()
