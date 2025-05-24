class BankAccount:
    def __init__(self, account_number, balance=0):  # Fixed constructor name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def get_balance(self):
        return self.balance


def main():
    n = int(input())
    accounts = {}

    for _ in range(n):
        acc_num, bal = input().split()
        accounts[acc_num] = BankAccount(acc_num, int(bal))

    m = int(input())
    for _ in range(m):
        parts = input().split()
        op, acc_num, amount = parts[0], parts[1], int(parts[2])
        if op == "deposit":
            accounts[acc_num].deposit(amount)
        elif op == "withdraw":
            accounts[acc_num].withdraw(amount)

    total = 0
    for acc_num in accounts:
        bal = accounts[acc_num].get_balance()
        print(bal)
        total += bal

    print(total)

if __name__ == "__main__":  # Fixed entry point check
    main()
