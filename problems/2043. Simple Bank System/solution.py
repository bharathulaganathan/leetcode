class Bank:

    def __init__(self, balance: List[int]):
        self.accounts = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > len(self.accounts) or account2 > len(self.accounts) or self.accounts[account1-1] < money:
            return False
        self.accounts[account1-1] -= money
        self.accounts[account2-1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account > len(self.accounts):
            return False
        self.accounts[account-1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account > len(self.accounts) or self.accounts[account-1] < money:
            return False
        self.accounts[account-1] -= money
        return True

def run(input):
    trans, val = input
    ans = []
    for i in range(len(trans)):
        if trans[i] == "Bank":
            bank = Bank(val[i][0])
            ans.append(None)
        else:
            ans.append(getattr(bank, trans[i])(*val[i]))
    return ans
