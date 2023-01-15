class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        self._balance = 0

    @property
    def balance(self):
        return round(self._balance)

    @balance.setter
    def balance(self, amount):
        if not isinstance(amount, (int, float)):
            pass
        elif not amount >= 0 or not amount <= 100000:
            pass
        else:
            self._balance = amount

    # balance = property(get_balance, set_balance)  # legacy property


def main():
    account = BankAccount("Nagalot")
    account.balance = 56.2
    print(account.balance)
    account.balance = 56.6
    print(account.balance)


if __name__ == "__main__":
    main()
