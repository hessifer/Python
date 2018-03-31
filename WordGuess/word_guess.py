#!/usr/bin/env python3
"""begins the word guess game."""

from game import Game
from prompter import Prompter


def main():
    # create our game and prompt object
    my_game = Game("tate")
    prompt = Prompter()

    # display initial hint
    print(f"Guess this word: {'-' * len(my_game.word)}")

    # ask for a letter until the word is guessed
    # once the word is guessed display game stats
    while True:
        try:
            guess = prompt.get_guess()
        except ValueError as ve:
            # add non alphabetical entry to misses and display error msg
            my_game.misses = guess
            print(ve)
        else:
            if my_game.is_hit(guess):
                print(f"You found the letter: {guess}")
                print("".join(my_game.hint))
                print()
                if my_game.is_correct_word():
                    border = "\n" + '-' * (40 + len(my_game.word))
                    banner = "Congratulations, you guessed the word '{}'"
                    print(border)
                    print(banner.format(my_game.word))
                    # display stats here
                    stats = my_game.show_stats()
                    print(f"Attempts: {stats.get('attempts')}")
                    print(f"Misses: {stats.get('misses')}")
                    print(f"Hits: {stats.get('hits')}")
                    print(border)
                    break
            else:
                print("".join(my_game.hint))


if __name__ == '__main__':
    main()
