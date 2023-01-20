import random


class AbstractGame:
    # unlike other languages, Python does not have an abstract keyword
    def start(self):  # instance method
        while True:
            start = input("Would you like to play? (Yes): ")
            if start.lower() == "yes":
                break

        self.play()

    def end(self):
        print("The game has ended.")
        self.reset()

    def play(self):
        raise NotImplementedError("You must provide and \
            implementation for play().")

    def reset(self):
        raise NotImplementedError("You must provide an \
            implementation for reset().")


class RandomGuesser(AbstractGame):
    def __inti__(self, rounds):
        self.rounds = rounds
        self.round = 0

    def reset(self):
        self.round = 0

    def play(self):
        while self.round < self.rounds:
            self.round += 1

            print(f"Welcome to round {self.round}. Let's begin!")
            random_num = random.randint(0, 10)
            while True:
                guess = input("Enter a number between 1-10: ")

                if int(guess) == random_num:
                    print("You win!")
                    break
