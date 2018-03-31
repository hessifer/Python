class Inventory(object):
    def __init__(self):
        self.slots = []

    def add_item(self, item):
        self.slots.append(item)
        
# create subclass of Inventory
class SortedInventory(Inventory):
    # override parent method
    def add_item(self, item):
        # call parent add_item method
        super(SortedInventory, self).add_item(item)
        self.slots.sort()
        

if __name__ == '__main__':
    mySI = SortedInventory()
    print(dir(mySI))
    print(mySI.slots)
    mySI.add_item('hot dog')
    mySI.add_item('apple')
    mySI.add_item('pear')
    print(mySI.slots)