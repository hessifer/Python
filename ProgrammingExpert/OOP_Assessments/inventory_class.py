class Inventory:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.items = {"": {}} 
        self.item_count = 0

    def add_item(self, name, price, quantity):
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
        pass

    def get_items_in_price_range(self, min_price, max_price):
        pass

    def get_most_stocked_item(self):
        pass