class Inventory:
    def __init__(self):
        self.slots = []
        
    def add(self, item):
        self.slots.append(item)
        
    # to use len on an object, the object must
    # have a method named __len__
    def __len__(self):
        return len(self.slots)
        
    def __contains__(self, item):
        return item in self.slots
        
    def __iter__(self):
        # generator, yield data as 
        # we work through the iter
        yield from self.slots