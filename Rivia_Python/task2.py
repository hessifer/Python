"""
Write a program that parses a line of text (input from user) 
and returns all the unique vowels found.
"""

def main():
    VOWELS = ['a', 'e', 'i', 'o', 'u']
    text = input('Please enter a line of text: ')
    unique_vowels = set()

    for c in text:
        if c in VOWELS:
            unique_vowels.add(c)
    print(f"{' '.join(unique_vowels)}")


if __name__ == '__main__':
    main()
