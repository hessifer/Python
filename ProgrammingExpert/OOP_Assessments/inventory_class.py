class Inventory:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
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
        self.item_count -= self.items[name]['quantity']
        self.items.__delitem__(name)
        
        return True

    def get_items_in_price_range(self, min_price, max_price):
        if isinstance(min_price, float):
            min_price = int(min_price)
        
        if isinstance(max_price, float):
            max_price = int(max_price)

        price_range = range(min_price, max_price + 1)
        item_price_match_list = []

        for k, v in self.items.items():
                if int(v['price']) in price_range:
                    item_price_match_list.append(k)
        
        return item_price_match_list

    def get_most_stocked_item(self):
        item_with_highest_quantity = ""
        highest_quantity = 0

        if len(self.items) == 0:
            return None
        for k, v in self.items.items():
            if v['quantity'] > highest_quantity:
                item_with_highest_quantity = k
            elif v['quantity'] == highest_quantity:
                item_with_highest_quantity = ""
 
        if not item_with_highest_quantity:
            return None

        return item_with_highest_quantity

    def __str__(self):
        return f"Items in Inventory: {self.items}, Inventory Capacity: {self.max_capacity}"
