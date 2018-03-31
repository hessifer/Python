'''
Make a subclass of list. Name it Liar.

Override the __len__ method so that it always returns the wrong number of items in the list. 
For example, if a list has 5 members, the Liar class might say it has 8 or 2.

You'll probably need super() for this.
'''

class Liar(list):
    def __init__(self, *args):
        self.arg = []
        
    def __len__(self):
        super().__len__()
        return len(self.arg) + 1
        

if __name__ == '__main__':
    myList = ['blue', 'green', 'orange']
    myLiar = Liar(myList)
    print("The length of your list is: {}".format(myLiar.__len__()))