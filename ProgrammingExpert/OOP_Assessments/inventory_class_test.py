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

    def test_case_4(self):
        inventory = Inventory(2)
        inventory.add_item('Milk', 3.89, 1)
        self.assertTrue(inventory.delete_item('MILK'))
        self.assertFalse(inventory.delete_item('squash'))

    def test_case_5(self):
        inventory = Inventory(5)
        inventory.add_item('Milk', 3.00, 1)
        inventory.add_item('eggs', 10.00, 1)
        inventory.add_item('bread', 4.00, 1)
        inventory.add_item('ham', 8.00, 1)
        self.assertEqual(sorted(['eggs', 'ham']), sorted(inventory.get_items_in_price_range(8, 10)))
        self.assertEqual(sorted(['milk', 'bread']), sorted(inventory.get_items_in_price_range(1, 7)))
        self.assertEqual([], inventory.get_items_in_price_range(11, 100))

    def test_case_6(self):
        inventory = Inventory(14)
        self.assertTrue(inventory.add_item('Chocolate', 4.99, 4))
        self.assertTrue(inventory.delete_item('Chocolate'))
        self.assertFalse(inventory.delete_item('Chocolate'))
        self.assertFalse(inventory.delete_item('Bread'))
        self.assertTrue(inventory.add_item('Chocolate', 4.99, 2))
        self.assertTrue(inventory.add_item('Bread', 4.99, 2))
        self.assertTrue(inventory.add_item('Ham', 4.99, 9))
        self.assertIn(inventory.get_most_stocked_item(), ('ham', 'bread', 'chocolate'))
        self.assertTrue(inventory.get_most_stocked_item(), "ham")

    def test_case_8(self):
        max_capacity = 4
        inventory = Inventory(max_capacity)
        self.assertEqual(inventory.add_item('Chocolate', 4.99, 1), True)
        self.assertEqual(inventory.add_item('Cereal', 6.99, 1), True)
        self.assertEqual(inventory.add_item('Milk', 3.99, 2), True)
        self.assertEqual(inventory.add_item('Butter', 2.99, 1), False)
        self.assertEqual(inventory.delete_item('Bread'), False)
        self.assertEqual(inventory.delete_item('Cereal'), True)
        self.assertEqual(['chocolate'], inventory.get_items_in_price_range(4.50, 6.50))


if __name__ == "__main__":
    unittest.main()
