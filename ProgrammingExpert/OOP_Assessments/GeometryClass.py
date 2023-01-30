import math

class Polygon:
    pass


class Triangle(Polygon):
    pass


class Rectangle(Polygon):
    pass


class Square(Rectangle):
    pass


# Use this function in your solution.
def get_triangle_area(side1, side2, side3):
    semi_perimeter = (side1 + side2 + side3) / 2
    return math.sqrt(
        semi_perimeter *
        (semi_perimeter - side1) *
        (semi_perimeter - side2) *
        (semi_perimeter - side3)
    )


# Use this function in your solution.
def get_rectangle_area(width, height):
    return width * height
