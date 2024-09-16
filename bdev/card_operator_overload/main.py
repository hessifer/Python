SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
RANKS = ["2", "3", "4", "5", "6", "7",
         "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_index = RANKS.index(self.rank)
        self.suit_index = SUITS.index(self.suit)

    def __eq__(self, other):
        if self.suit == other.suit:
            if self.rank == other.rank:
                return True
        return False

    def __lt__(self, other):
        if self.rank_index < other.rank_index:
            return True
        elif self.rank_index == other.rank_index:
            if self.suit_index < other.suit_index:
                return True

        return False

    def __gt__(self, other):
        if self.rank_index > other.rank_index:
            return True
        elif self.rank_index == other.rank_index:
            if self.suit_index > other.suit_index:
                return True

        return False

    # don't touch below this line
    def __str__(self):
        return f"{self.rank} of {self.suit}"


if __name__ == "__main__":
    c1 = Card("2", "Clubs")
    c2 = Card("2", "Clubs")
    c3 = Card("2", "Diamonds")
    c4 = Card("3", "Clubs")
    c5 = Card("2", "Clubs")
    print(c1.__eq__(c2))
    print(c1.__eq__(c4))
    print(c3.__eq__(c5))
