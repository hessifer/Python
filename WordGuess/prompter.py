class Prompter:
    """Used to control how we interact with the player."""

    def get_guess(self):
        """Asks the player for a guess.
        Returns:
            guess (str): the lowercase version of the letter guessed
        """

        # get player's guess
        guess = input("Please guess a single letter: ").lower()

        # make sure the player entered a single alphabetical letter
        if not guess.isalpha():
            raise ValueError("You must enter a single alphabetical letter.")

        return guess
