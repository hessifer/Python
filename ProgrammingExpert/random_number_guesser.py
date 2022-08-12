import random


def main():
    # get valid start number from user
    while True:
        try:
            start = int(input("Enter the start of the range: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        else:
            break

    # get valid end number from user
    while True:
        try:
            stop = int(input("Enter the end of the range: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        else:
            if stop < start:
                print("Please enter a valid number.")
                continue
            else:
                break

    # generate random number within this range
    number_to_guess = random.randint(start, stop)

    # check if number was guessed, if so display the number of attempts it took
    tries = get_correct_answer(number_to_guess)
    if tries > 1:
        print(f"You guessed the number in {tries} attempts ")
    else:
        print(f"You guessed the number in {tries} attempt ")


def get_correct_answer(answer):
    # have user try and guess number
    # once user guesses number, display how many attempts it took
    attempts = 1
    guess = input("Guess a number: ")

    while True:
        if guess.isnumeric():
            if int(guess) == answer:
                break
        else:
            print("Please enter a valid number.")
        guess = input("Guess a number: ")
        attempts += 1

    return attempts


if __name__ == "__main__":
    main()
