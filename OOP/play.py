from thieves import Thief
from inventory import Inventory
from items import Item
from items import Weapon

charles = Thief(name="Charles", sneaky=False)
print(charles.sneaky)
print(charles.agile)
print(charles.hide(8))
print("\n\n")
print("Printing Class and Instance information using __str__.")
print(charles)

# instantiate an Item object
coin = Item('coin', 'a gold coin')

# instantiate an Inventory object
inventory = Inventory()
inventory.add(coin)

print("You have {} item(s) in your inventory.".format(len(inventory)))
if coin in inventory:
    print("You have a gold coin in your inventory.")
    

sword = Weapon('sword', '2h sharp sword', 50)
inventory = Inventory()
inventory.add(sword)
for item in inventory:
    print("Item Name: {} - Item Description: {}".format(item.name, item.description))





