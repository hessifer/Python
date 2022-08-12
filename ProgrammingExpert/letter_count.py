word = input("Enter a string: ")
letter_count = dict()

for letter in word:
    letter_count[letter] = letter_count.get(letter, 0) + 1

for key, value in letter_count.items():
    print(f"{key}: {value}")
