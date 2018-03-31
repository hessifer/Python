class Circle:
    
    def __init__(self, diameter):
        self.diameter = diameter
        
    @property
    def radius(self):
        return self.diameter / 2
        
    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2
        
        
if __name__ == '__main__':
    # circle with diameter of 10
    small = Circle(10)
    
    # get the circle's radius
    print(small.radius)
    
    # set the circle's radius
    small.radius = 10
    print(small.diameter)
    