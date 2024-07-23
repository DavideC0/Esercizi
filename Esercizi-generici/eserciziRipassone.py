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
    
class Veicolo:
    def __init__(self, marca: str, modello: str, anno: int) -> None:
        self.marca: str = marca
        self.modello: str = modello
        self.anno: int = anno
        
    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}")
            
class Auto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int, numero_porte: int) -> None:
        super().__init__(marca, modello, anno)
        self.numero_porte: int = numero_porte
        
    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.numero_porte}")
    
class Moto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int, tipo: str) -> None:
        super().__init__(marca, modello, anno)
        self.tipo: str = tipo
        
    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}")
        
def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    dict_result: dict[str:int] = {}
    for key, value in dict1.items():
        if key in dict_result:
            dict_result[key] += value
        else:
            dict_result[key] = value
            
    for key, value in dict2.items():
        if key in dict_result:
            dict_result[key] += value
        else:
            dict_result[key] = value  
    return dict_result    