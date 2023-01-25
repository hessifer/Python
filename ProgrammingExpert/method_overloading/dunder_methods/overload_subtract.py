class StoreItem:
    TAX = 0.13

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.after_tax_price = 0
        self.set_after_tax_price()
    
    def set_after_tax_price(self):
        self.after_tax_price = round(self.price * (1 + self.TAX), 2)

    def __sub__(self, discount):
        return StoreItem(self.name, self.price - discount)

    def __mul__(self, value):
        return StoreItem(self.name, self.price * value)


bread = StoreItem("Bread", 7)
# discounted_bread = bread - 2
discounted_bread = bread * 0.8  # apply 20% discount 
print(discounted_bread.after_tax_price)
