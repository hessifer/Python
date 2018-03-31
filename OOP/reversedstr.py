class ReversedStr(str):
    def __new__(*args, **kwargs):
        # sub-classing built-ins
        # class method that operates on class and not instance
        # __new__
        self = str.__new__(*args, **kwargs)
        self = self[::-1]
        return self
        
        
if __name__ == '__main__':
    import reversedstr
    
    rs = reversedstr.ReversedStr('hello')
    print(rs)