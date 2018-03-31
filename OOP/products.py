class Product:
    '''class that provides methods and attributes associated to products'''
    def __init__(self, name, price, discountPercent):
        self.name = name
        self.price = price
        self.discountPercent = discountPercent
        
    def getDiscountAmount(self) -> float:
        '''calculate and return discount amount'''
        return self.price * self.discountPercent / 100
        
    def getDiscountPrice(self) -> float:
        '''calculate and return discount price'''
        return self.price - self.getDiscountAmount()