import math

class Polygon:
    def get_area(self):
        raise NotImplementedError("get_area() needs to be impelmented.")
    
    def get_sides(self):
        raise NotImplementedError("get_sides() needs to be implemented.")
    
    def get_perimeter(self):
        return sum(self.get_sides())
        

class Triangle(Polygon):
    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]
    
    def get_sides(self):
        return self.sides
    
    def get_area(self):
        semi_perimeter = sum(self.sides) / 2
        return math.sqrt(
            semi_perimeter *
            (semi_perimeter - self.sides[0]) *
            (semi_perimeter - self.sides[1]) *
            (semi_perimeter - self.sides[2])
        )


class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_sides(self):
        return [self.width, self.width, self.height, self.height]
    
    def get_area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

