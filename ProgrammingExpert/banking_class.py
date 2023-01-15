class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        self._balance = 0

    def get_balance(self):
        return round(self._balance)

    def set_balance(self, amount):
        if not isinstance(amount, (int, float)):
            pass
        elif not amount >= 0 or not amount <= 100000:
            pass
        else:
            self._balance = amount

    balance = property(get_balance, set_balance)  # legacy property


def main():
    account = BankAccount("Nagalot")
    account.set_balance(56.2)
    print(account.get_balance())
    account.set_balance(56.6)
    print(account.get_balance())


if __name__ == "__main__":
    main()
