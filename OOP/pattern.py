class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern
        
    def __str__(self):
        results = []
        
        for i in self.pattern:
            if i == '.':
                results.append('dot')
            elif i == '_':
                results.append('dash')
        return "-".join(results)
                
    

class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)