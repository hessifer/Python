class NumString:
    '''just a silly example of leveraging BIFs'''
    def __init__(self, value):
        self.value = str(value)
        
    def __str__(self):
        return self.value
        
    def __int__(self):
        return int(self.value)
        
    def __float__(self):
        return float(self.value)
        
    def __add__(self, other):
        if '.' in self.value:
            return float(self) + other
        return int(self) + other
        
    # reflective method    
    def __radd__(self, other):
        return self + other
        
    # inplace
    def __iadd__(self, other):
        self.value = self + other
        return self.value
        
    
        
        
if __name__ == '__main__':
    from numstring import NumString
    five = NumString(5)
    two_dot_three = NumString(2.3)
    
    age = NumString(25)
    print(age + 5)
    print(5 + age)
    print(age + 1)
    
    print(str(five))
    print(five)
    print(int(five))
    print(float(five))
    print(five + 4)
    print(two_dot_three + 2)
    

    
    
    