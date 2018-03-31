from dice_ex import D20

class Hand(list):
    def __init__(self, size=2, die_class=None, *args, **kwargs):
        if not die_class:
            raise ValueError("You must provide a die class.")
        super().__init__()
        
        for _ in range(size):
            self.append(die_class())
        self.sort
        
    @property
    def total(self):
        return sum(self)
    
    @classmethod
    def roll(cls, size):
        return cls(size=size, die_class=D20)
        
if __name__ == "__main__":
    hands = Hand.roll(2)
    print(f"Number of Hands: {hands.total}")
