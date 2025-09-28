import random


class Die:
    def __init__(self, sides=2, value=0):
        if not sides >= 2:
            raise ValueError("Must have at least 2 sides.")
        if not isinstance(sides, int):
            raise ValueError("Sides must be a whole number.")
        if not isinstance(value, int):
            raise ValueError("Value must be a whole number.")
        self.sides = sides
        self.value = value or random.randint(1, sides)

    def __int__(self):
        return self.value

    def __eq__(self, other):
        return int(self) == other

    def __ne__(self, other):
        return int(self) != other

    def __gt__(self, other):
        return int(self) > other

    def __lt__(self, other):
        return int(self) < other

    def __ge__(self, other):
        return int(self) >= other

    def __le__(self, other):
        return int(self) <= other

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other):
        return int(self) + other

    def __repr__(self):
        return str(self.value)


class D6(Die):
    """inherit from Die, make 6 sided always."""
    def __init__(self):
        # overide parent class __init__
        super().__init__(sides=6)


class D4(Die):
    """inherit from Die, make 4 sided always."""
    def __init__(self):
        # override parent __init__
        super().__init__(sides=4)


class D3(Die):
    """inherit from Die, make 3 sided always."""
    def __init__(self):
        # override parent __init__
        super().__init__(sides=3)


if __name__ == "__main__":
    d6 = D6()
    d4 = D4()

    print("Hello")
    print(f"d6 Value: {int(d6)}")
    print(f"d4 Value: {int(d4)}")
    print()
    print(f"d6 > 2: {d6 > 2}")
    print(f"d6 < 5: {d6 < 5}")
    print(f"d6 <= 3: {d6 <= 3}")
    print(f"d6 >= 2: {d6 >= 2}")
    print(f"d6 != 3: {d6 != 3}")
    print(f"d6 == 6: {d6 == 6}")
    print(f"d4 + d6: {d4 + d6}")
    print(f"d4 + 5: {d4 + 5}")
    print(f"3 + d6: {3 + d6}")
