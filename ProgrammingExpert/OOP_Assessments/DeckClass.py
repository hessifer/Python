import random

class Deck:
    # Class Attributes
    card_values = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
    card_suits = ['H', 'D', 'C', 'S']
    
    # Construtor
    def __init__(self):
        self.cards = []
        self.create_deck()
        
    def create_deck(self):
        for value in Deck.card_values:
            for suit in Deck.card_suits:
                card = value + suit
                self.cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self, n):
        cards_dealt = []
        
        for i in range(n):
            if len(self.cards) == 0:
                break
            
            cards_dealt.append(self.cards.pop())
        return cards_dealt
    
    def sort_by_suit(self):
        suits_sort = {"H": [], "D": [], "C": [], "S": []}
        
        for card in self.cards:
            suits_sort.get(card[-1]).append(card)
    
        self.cards = (suits_sort.get("H") + suits_sort.get("D") + suits_sort.get("C") + suits_sort.get("S"))
        
    def contains(self, card):
        return card in self.cards
    
    def copy(self):
        new_deck = Deck()
        new_deck.cards = self.cards[:]
        return new_deck
    
    def get_cards(self):
        return self.cards[:]
    
    def __len__(self):
        return len(self.cards)
        
        
    
    
        
    
    
    
    