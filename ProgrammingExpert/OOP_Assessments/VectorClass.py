class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, vector):
        return self.a == vector.a and self.b == vector.b

    def __ne__(self, vector):
        return not self.__eq__(vector)

    def __str__(self):
        return f"a = {self.a}, b = {self.b}"

    def __repr__(self):
        return self.__str__()

    def __add__(self, vector):
        x = self.a + vector.a
        y = self.b + vector.b
        return Vector(x, y)

    def __sub__(self, vector):
        x = self.a - vector.a
        y = self.b -vector.b
        return Vector(x, y)

    def __mul__(self, vector):
        x = self.a * vector.a
        y = self.b * vector.b
        return x + y
