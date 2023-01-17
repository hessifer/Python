class Temperature:
    # Write your code here
    min_temperature = 0
    max_temperature = 1000

    @classmethod
    def update_min_temperature(cls, temperature):
        if temperature >= cls.max_temperature:
            raise Exception("Invalid temperature.")
        else:
            cls.min_temperature = temperature
    
    @classmethod
    def update_max_temperature(cls, temperature):
        if temperature <= cls.min_temperature:
            raise Exception("Invalid temperature.")
        else:
            cls.max_temperature = temperature

    def __init__(self, kelvin):
        if kelvin <= Temperature.min_temperature or kelvin >= Temperature.max_temperature:
            raise Exception("Invalid temperature.")
        else:
            self.kelvin = kelvin
