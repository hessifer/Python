import inspect
import unittest

from banking_class import BankAccount


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(inspect.isclass(BankAccount),
                        "BankAccount should be a class.")

    def test_case_2(self):
        account = BankAccount("Tim")
        self.assertTrue(hasattr(account, "get_balance"),
                        "A BankAccount should have a \
                        `get_balance` method.")
        self.assertTrue(hasattr(account, "set_balance"),
                        "A BankAccount should have a \
                        `set_balance` method.")

    def test_case_3(self):
        account = BankAccount("Tim")
        self.assertEqual(0, account.get_balance())

    def test_case_4(self):
        account = BankAccount("Clement")
        account.set_balance(-1)
        self.assertEqual(0, account.get_balance())
        account.set_balance("1.0")
        self.assertEqual(0, account.get_balance())
        account.set_balance(100001)
        self.assertEqual(0, account.get_balance())

    def test_case_5(self):
        account = BankAccount("Antoine")
        account.set_balance(56.2)
        self.assertEqual(56, account.get_balance())
        account.set_balance(56.6)
        self.assertEqual(57, account.get_balance())


if __name__ == '__main__':
    unittest.main()
