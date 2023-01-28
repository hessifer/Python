class Inventory:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        #self.items = {"": {}} 
        self.items = {} 
        self.item_count = 0

    def add_item(self, name, price, quantity):
        name = name.lower()

        if quantity <= self.max_capacity - self.item_count:
            if name in self.items.keys():
                return False
            else:
                self.items[name] = {
                    'price': price,
                    'quantity': quantity,
                }
                self.item_count += quantity
        else:
            return False
        
        return True

    def delete_item(self, name):
        name = name.lower()

        if not name in self.items.keys():
            return False
        self.items.__delitem__(name)
        
        return True

    def get_items_in_price_range(self, min_price, max_price):
        price_range = range(min_price, max_price + 1)
        item_price_match_list = []

        print(self.items)
        for k, v in self.items.items():
                if v['price'] in price_range:
                    item_price_match_list.append(k)
        
        return item_price_match_list

    def get_most_stocked_item(self):
        pass


if __name__ == '__main__':
    inventory = Inventory(5)
    inventory.add_item('Milk', 3.00, 1)
    inventory.add_item('eggs', 10.00, 1)
    inventory.add_item('bread', 4.00, 1)
    inventory.add_item('ham', 8.00, 1)
    print(inventory.get_items_in_price_range(8, 10))
