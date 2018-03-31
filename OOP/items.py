class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def __str__(self):
        return '{}: {}'.format(self.name, self.description)
        

# child class of Item
# inherits from Item
class Weapon(Item):
    def __init__(self, name, description, power):
        '''initialize parent class attributes'''
        super().__init__(name, description)
        self.power = power