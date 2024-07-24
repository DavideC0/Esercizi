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

def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:
    for key, value in dizionario.items():
        if value == valore:
            return key
    return None

class RecipeManager:
    def __init__(self) -> None:
        self.recipes: dict[str:list[str]] = {}

    def create_recipe(self, name, ingredients):
        self.recipes[name] = ingredients
        return self.recipes

    def add_ingredient(self, recipe_name, ingredient):
        self.recipes[recipe_name].append(ingredient)
        return self.recipes

    def remove_ingredient(self, recipe_name, ingredient):
        self.recipes[recipe_name].remove(ingredient)
        return self.recipes
    
    def update_ingredient(self, recipe_name, old_ingredient, new_ingredient):
        i = self.recipes[recipe_name].index(old_ingredient)
        self.remove_ingredient(recipe_name, old_ingredient)
        self.recipes[recipe_name].insert(i, new_ingredient)
        return self.recipes

    def list_recipes(self):
        return list(self.recipes.keys())
    
    def list_ingredients(self, recipe_name):
        return self.recipes[recipe_name]
    
    def search_recipe_by_ingredient(self, ingredient):
        dizionario = {}
        for key, value in self.recipes.items():
            if ingredient in value:
                dizionario[key] = value
        return dizionario

class Movie:
    def __init__(self, movie_id, title, director) -> None:
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = False

    def rent(self):
        if self.is_rented:
            print(f"Il film '{self.title}' è già noleggiato.")
        else:
            self.is_rented = True

    def return_movie(self):
        if self.is_rented:
            self.is_rented = False
        else:
            print(f"Il film {self.title} non è attualmente noleggiato.")

class Customer:
    def __init__(self, customer_id, name) -> None:
        self.customer_id = customer_id
        self.name = name
        self.rented_movies: list[Movie] = []
    
    def rent_movie(self, movie: Movie):
        if not movie.is_rented:
            movie.rent()
            self.rented_movies.append(movie)
        else:
            print(f"Il film '{movie.title}' è già noleggiato.")
    
    def return_movie(self, movie: Movie):
        if movie.is_rented:
            movie.return_movie()
            self.rented_movies.remove(movie)
        else:
            print(f"Il film '{movie.title}' non è stato noleggiato da questo cliente.")

class VideoRentalStore:
    def __init__(self) -> None:
        self.movies: dict[str:Movie] = {}
        self.customers: dict[str:Customer] = {}
    
    def add_movie(self, movie_id, title, director):
        if movie_id not in self.movies:
            self.movies[movie_id] = Movie(movie_id,title,director)
        else:
            print(f"Il film con ID {movie_id} esiste già.")
    
    def register_customer(self, customer_id: str, name: str):
        if customer_id not in self.customers:
            self.customers[customer_id] = Customer(customer_id, name)
        else:
            print(f"Il cliente con ID {customer_id} è già registrato.")

    def rent_movie(self, customer_id: str, movie_id: str):
        if customer_id in self.customers and movie_id in self.movies:
            self.customers[customer_id].rent_movie(self.movies[movie_id])
        else:
            print(f"Cliente o film non trovato.")
    
    def return_movie(self, customer_id: str, movie_id: str):
        if customer_id in self.customers and movie_id in self.movies:
            self.customers[customer_id].return_movie(self.movies[movie_id])
        else:
            print(f"Cliente o film non trovato.")
    
    def get_rented_movies(self, customer_id):
        if customer_id in self.customers:
            return self.customers[customer_id].rented_movies
        else:
            print(f"Cliente non trovato.")
            return []
        
def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    dizionario = {}
    for key, value in prodotti.items():
        if value - value*10/100 > 20:
            dizionario[key] = value
    return dizionario

def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA or conditionB and conditionC:
        return "Operazione permessa"
    else:
        return "Operazione negata"
    
def check_access(username: str, password, is_active: bool) -> str:
    if username == 'admin' and password == '12345' and is_active:
        return 'Accesso consentito'
    else:
        return 'Accesso negato'
    
def transform(x: int) -> int:
    if x % 2 == 0:
        return x / 2
    else:
        return x * 3 - 1

def frequency_dict(elements: list) -> dict:
    dizionario = {}
    for element in elements:
        if element in dizionario:
            dizionario[element] += 1
        else:
            dizionario[element] = 1
    return dizionario

def sum_above_threshold(numbers: list[int], bound: int) -> int:
    s: int = 0
    for i in numbers:
        if i > bound:
            s += i
    return s