class Archer:
    def __init__(self, name, health, num_arrows):
        self.name = name
        self.health = health
        self.num_arrows = num_arrows

    def get_shot(self):
        if self.health > 1:
            self.health -= 1
        else:
            raise Exception(f"{self.name} is dead")

    def shoot(self, target):
        if self.num_arrows > 0:
            self.num_arrows -= 1
            print(f"{self.name} shoots {target.name}")
            target.get_shot()
        else:
            raise Exception(f"{self.name} can't shoot")

    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.num_arrows} arrows")


if __name__ == "__main__":
    archer1 = Archer("Robin", 2, 5)
    archer2 = Archer("Oliver", 1, 5)
    archer1.shoot(archer2)
    archer1.print_status()
    archer2.shoot(archer1)
    archer2.print_status()
    archer1.shoot(archer2)
    archer1.print_status()
    archer2.shoot(archer1)
    archer2.print_status()

