import random

class Die:
    def __init__(self):
        self.__value = 1
    
    @property
    def value(self):
        return self.__value
        
    
    @value.setter
    def value(self, value):
        if value < 1 or value > 6:
            raise ValueError("die value must be from 1 to 6.")
        else:
            self.__value = value
        
    def roll(self):
        self.__value = random.randrange(1, 7)
        
class Dice:
    def __init__(self):
        self.__list = []
        
    @property
    def list(self):
        dice_tuple = tuple(self.__list)
        return dice_tuple
        
    def addDie(self, die):
        self.__list.append(die)
        
    def rollAll(self):
        for die in self.__list:
            die.roll()