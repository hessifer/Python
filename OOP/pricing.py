class Pricing:
    _price = 0.0
    tax_rate = 0.12
  
    def __init__(self, base_price):
        self._price = base_price
    
    @property
    def price(self):
        return self._price + (self._price * self.tax_rate)
    
    @price.setter
    def price(self, price):
        self._price = price