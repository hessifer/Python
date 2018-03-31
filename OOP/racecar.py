class RaceCar:
    
    def __init__(self, color, fuel_remaining, laps=0, **kwargs):
        self.color = color
        self.fuel_remaining = fuel_remaining
        self.laps = laps
        for key, value in kwargs.items():
            setattr(self, key, value)
            
    def run_lap(self, length):
        self.fuel_remaining -= (length * 0.125)
        self.laps += 1
            
            
if __name__ == '__main__':
    myCar = RaceCar('blue', 10, 0)
    
    print(myCar.color)
    print(myCar.fuel_remaining)
    
    myCar.run_lap(5)
    print(myCar.laps)
    print(myCar.fuel_remaining)