import random

from attributes import Agile, Sneaky
from characters import Character


# MRO Method Resolution Order - tells python how to figure out which superclass' method to call
# when two superclasses have methods with the same name
class Thief(Agile, Sneaky, Character):
    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))