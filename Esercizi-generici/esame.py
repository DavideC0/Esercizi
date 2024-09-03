class ContactManager:
    def __init__(self) -> None:
        self.contacts: dict[str: list[str]] = {}
        
    def create_contact(self, name: str, phone_numbers: list[str]):
        if name not in self.contacts:
            self.contacts[name] = phone_numbers
            new_dict: dict[str:list[str]] = {}
            new_dict[name] = phone_numbers 
            return  new_dict
        else:
            return "Errore: il contatto esiste già."
        
    def add_phone_number(self, contact_name: str, phone_number: str):
        if contact_name in self.contacts:
            if phone_number not in self.contacts[contact_name]:
                self.contacts[contact_name].append(phone_number)
                new_dict: dict[str:list[str]] = {}
                new_dict[contact_name] = self.contacts[contact_name]
                return new_dict
            else:
                return "Errore: il numero di telefono esiste già."
        else:    
            return "Errore: il contatto non esiste."
    
    def remove_phone_number(self, contact_name: str, phone_number: str):
        if contact_name in self.contacts:
            if phone_number in self.contacts[contact_name]:
                self.contacts[contact_name].remove(phone_number)
                new_dict: dict[str:list[str]] = {}
                new_dict[contact_name] = self.contacts[contact_name]
                return new_dict
            else:
                return "Errore: il numero di telefono non è presente."
        else:
            return "Errore: il contatto non esiste."
    
    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number: str):
        if contact_name in self.contacts:
            if old_phone_number in self.contacts[contact_name]:
                self.contacts[contact_name].remove(old_phone_number)
                self.contacts[contact_name].append(new_phone_number)
                new_dict: dict[str:list[str]] = {}
                new_dict[contact_name] = self.contacts[contact_name]
                return new_dict
            else:
                return "Errore: il numero di telefono non è presente."
        else:
            return "Errore: il contatto non esiste."
    
    def list_contacts(self):
        return list(self.contacts.keys())
    
    def list_phone_numbers(self, contact_name: str):
        if contact_name in self.contacts:
            return self.contacts[contact_name]
        else:
            return "Errore: il contatto non esiste."
    
    def search_contact_by_phone_number(self, phone_number: str):
        lista: list[str] = []
        for key, value in self.contacts.items():
            if phone_number in value:
                lista.append(key)
        if len(lista) == 0:
            return "Nessun contatto trovato con questo numero di telefono."
        return lista
            
class Elettrodomestico:
    def __init__(self, marca: str, modello: str, potenza: int) -> None:
        self.marca: str = marca
        self.modello: str = modello
        self.potenza: int = potenza
        
    def descrivi_elettrodomestico(self):
        return f"Marca: {self.marca}, Modello: {self.modello}, Potenza: {self.potenza}W"
    
class Frigorifero(Elettrodomestico):
    def __init__(self, marca: str, modello: str, potenza: int, capacità: int) -> None:
        super().__init__(marca, modello, potenza)
        self.capacità: int = capacità
        
    def descrivi_elettrodomestico(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Potenza: {self.potenza}W, Capacità: {self.capacità}L")

class Lavatrice(Elettrodomestico):
    def __init__(self, marca: str, modello: str, potenza: int, carico_max: int) -> None:
        super().__init__(marca, modello, potenza)
        self.carico_max: int = carico_max
    
    def descrivi_elettrodomestico(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Potenza: {self.potenza}W, Carico massimo: {self.carico_max}kg")
    
 	

# Test case per verificare la funzionalità delle classi
# Creazione di oggetti Frigorifero e Lavatrice e descrizione degli elettrodomestici
frigo = Frigorifero("Samsung", "RT38K5538S8", 100, 380)
lavatrice = Lavatrice("LG", "F4J6VY1W", 200, 10)

# Descrizione degli elettrodomestici
frigo.descrivi_elettrodomestico()
lavatrice.descrivi_elettrodomestico()