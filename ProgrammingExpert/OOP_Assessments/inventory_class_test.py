import unittest

from inventory_class import Inventory

class InventoryClassTest(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(hasattr(Inventory, 'add_item'))
        inventory = Inventory(0)
        self.assertFalse(inventory.add_item('Chocolate', 4.99, 1))

    def test_case_2(self):
        inventory = Inventory(3)
        self.assertFalse(inventory.add_item('Chocolate', 4.99, 4))

    def test_case_3(self):
        inventory = Inventory(3)
        self.assertTrue(inventory.add_item('Chocolate', 4.99, 1))
        self.assertTrue(inventory.add_item('Butter', 4.99, 1))
        self.assertFalse(inventory.add_item('Butter', 4.99, 1))
        self.assertFalse(inventory.add_item('Bread', 4.99, 2))
        self.assertTrue(inventory.add_item('Bread', 4.99, 1))



if __name__ == "__main__":
    unittest.main()
