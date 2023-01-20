# Write your code here
class Animal:
    @staticmethod
    def sleep():
        print("ZzzZzz")

    def animal_sound(self):
        raise NotImplementedError

    def wake_up(self):
        self.animal_sound()
        print("I am awake!")

class Lion(Animal):
    def animal_sound(self):
        print("Roar!")
