class Protected:
    __name = "Security"
    
    def __method(self):
        return self.__name
        
        
if __name__ == '__main__':
    protected = Protected()
    print(protected.__method())