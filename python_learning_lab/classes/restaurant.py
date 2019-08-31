class Restaurant:
    """An example of a Restaurant class with methods and attributes."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize our Restaurant attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Displays the restaurant's name and cuisine type."""
        print(f"{self.restaurant_name} sells {self.cuisine_type} food.")

    def open_restaurant(self):
        """Open the restaurant."""
        print(f"{self.restaurant_name} is now open.")


if __name__ == '__main__':
    restaurant = Restaurant('Popeyes', 'Southern Fried Chicken')
    print(f"{restaurant.restaurant_name}")
    print(f"{restaurant.cuisine_type}")
    restaurant.describe_restaurant()
    restaurant.open_restaurant()

    res1 = Restaurant('Wendys', 'Hamburgers')
    res2 = Restaurant('Sakura', 'Hibachi')
    res3 = Restaurant('Jon Thai', 'Thai')

    res1.describe_restaurant()
    res2.describe_restaurant()
    res3.describe_restaurant()
