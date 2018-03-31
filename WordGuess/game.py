class Game:
    """Used to define the structure of our game."""

    def __init__(self, word):
        """Our constructor for Game
        Args:
            word (str): the game's secret word
        """

        self.word = word.lower()
        self._hits = []
        self._misses = []
        self._hint = list('-' * len(self.word))

    @property
    def hint(self):
        """returns hint value."""
        return self._hint

    @property
    def hits(self):
        """returns hits value."""
        return self._hits

    @property
    def misses(self):
        """returns misses value."""
        return self._misses

    @misses.setter
    def misses(self, value):
        """setter to update misses value."""
        self._misses.append(value)

    def is_hit(self, guess):
        """Determines if lettered guessed is a hit
        Args:
            guess (str): the letter guessed

        Returns:
            result (bool): returns True for hit or False for miss
        """

        if guess in self.word:
            self._hits.append(guess)
            self._build_hint(guess)
            return True

        self._misses.append(guess)
        return False

    def is_correct_word(self):
        """Checks to see if the guessed_word is correct.
        Returns:
            True/False (bool): true if word is correct false otherwise.
        """
        return "".join(self._hint) == self.word

    def show_stats(self):
        """Computes game stats for player.
        Returns:
            stats (dict): a dictionary with the computed game stats.
        """
        stats = {}
        stats['attempts'] = len(self._hits + self._misses)
        stats['hits'] = len(self._hits)
        stats['misses'] = len(self._misses)
        return stats

    def _build_hint(self, guess):
        """determines what is displayed as our hint.
        Args:
            guess (str): the letter guessed
        """

        # hold the index of our hits
        locs = []

        # set default value for position in secret word
        pos = 0

        # get the positon of the matching letter in our secret word
        pos = self.word.find(guess, pos)

        # as long as we find a matching letter add it to locs
        while pos != -1:
            locs.append(pos)
            pos = self.word.find(guess, pos + 1)

        # update the hint to reflect the correct guesses
        for loc in locs:
            # self._hint = self._hint[:loc] + guess + self._hint[loc + 1:]
            self._hint.pop(loc)
            self._hint.insert(loc, guess)
            
        """
        result = ""
        
        for l in self.word:
            if l in self._hits:
                result += l
            else:
                result += '-'
        """

        """
        for letter in self.word:
            if letter == guess:
                self._hint += guess
            else:
                self._hint += '-'
        """

