class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


# don't touch above this line


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows

    def use_arrows(self, num):
        if num > self.get_num_arrows():
            raise Exception("not enough arrows")
        else:
            # self.__num_arrows = self.get_num_arrows() - num
            self.__num_arrows -= num


class Crossbowman(Archer):
    def __init__(self, name, num_arrows):
        super().__init__(name, num_arrows)

    def triple_shot(self, target):
        self.use_arrows(3)

        return f"{target.get_name()} was shot by 3 crossbow bolts"


if __name__ == "__main__":
    archer = Archer("Sophia the Archer", 7)
    crossbowman = Crossbowman("Victor the Crossbowman", 3)

    print(crossbowman.triple_shot(archer))
