# Write your code here
class Animal:
    def __init__(self, age, weight, height):
        self.age = age
        self.weight = weight
        self.height = height


class Mammal(Animal):
    def __init__(self, age, weight, height, sex):
        super().__init__(age, weight, height)
        self.sex = sex


class Reptile(Animal):
    def __init__(self, age, weight, height, num_of_legs=4):
        super().__init__(age, weight, height)
        self.num_of_legs = num_of_legs


class Monkey(Mammal):
    fingers = 5

    def __init__(self, age, weight, height, sex, color):
        super().__init__(age, weight, height, sex)
        self.color = color


class Lizard(Reptile):
    tail = True

    def __init__(self, age, weight, height, num_of_legs, color):
        super().__init__(age, weight, height, num_of_legs)
        self.color = color
