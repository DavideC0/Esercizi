def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
    dictionary: dict[str:list[int]] = {}
    for i in range(len(tuples)):
        if tuples[i][0] in dictionary:
            dictionary[tuples[i][0]].append(tuples[i][1])
        else:
            dictionary[tuples[i][0]] = [tuples[i][1]]
    return dictionary

class Account:
    def __init__(self, id) -> None:
        self.account_id = id
        self.saldo = 0
        
    def deposit(self, amount):
        self.saldo += amount
        
    def get_balance(self):
        return self.saldo

class Bank:
    def __init__(self) -> None:
        self.accounts: dict[str:Account] = {}
        
    def create_account(self, account_id):
        account = Account(account_id)
        self.accounts[account_id] = account
        return account
    
    def deposit(self, account_id, amount):
        self.accounts[account_id].deposit(amount)
        
    def get_balance(self, account_id):
        return self.accounts[account_id].get_balance()   