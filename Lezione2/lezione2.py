#Davide Calcagni
#18/04/2024
import random

#2-3 Personal Message
name: str = "Francesco Cilurzo"
print(f"Hello {name}, would you like to learn some python?")

#2-4 Name Cases
name_upper: str = name.upper()
name_lower: str = name.lower()
print(f"Upper: {name_upper}, Lower: {name_lower}")

#2-5 Famouse Quote / 2-6 Famous Quote 2
print(f'Una volta {name} disse:"A caval goduto non rompere il cazzo"')

#2-8 File Extensions
filename: str = "python_nothes.txt"
filename_removed: str = filename.removesuffix(".txt")
print(f"prima {filename}, dopo {filename_removed}")

#3-1 Names
names_list: list = ["Davide", "Giacomo", "Veronica", "Catalina", "Matteo"]
for i in range(len(names_list)):
    print(names_list[i])

#3-2 Greetings
for i in range(len(names_list)):
    print(f"Ciao {names_list[i]}, come stai?")

#3-3 Your Own List
cars: str = ["Ferrari", "Panda", "Fiesta"]
sentence: str = ["Mi piacerebbe guidare una", "Ho sognato di avere una", "Sto guidando una"]
for i in range(len(cars)):
    print(f"{sentence[i]} {cars[i]}")

#3-4 Guest List
guest_list: list = ["Catalina", "Bruna", "Gino"]
print(f"{guest_list[0]} vorrei che venissi a cena con me")
print(f"{guest_list[1]} per festeggiare il tuo compleanno andiamo a cena")
print(f"{guest_list[2]} avrei voluto fare un'ultima cena con te prima succedesse")

#3-5 Changing Guest List
not_coming: str = guest_list.pop(2)
print(f"{not_coming} dato che non ci sei non puoi nemmeno venire")
guest_list.append("Roberto")
print(f"{guest_list[0]} vorrei che venissi a cena con me")
print(f"{guest_list[1]} per festeggiare il tuo compleanno andiamo a cena")
print(f"{guest_list[2]} vieni anche tu a cena")

#3-6 More Guestes
for i in range(len(guest_list)):
    print(f"Ciao {guest_list[i]}, ho trovato un tavolo più grande venite qui invece")
guest_list.insert(0, "Giacomo")
guest_list.insert(2, "Matteo")
guest_list.append("Veronica")
for i in range(len(guest_list)):
    print(f"Ciao {guest_list[i]}, sei invitat al nuovo luogo x con un tavolo più grande")

#3-7 Shrinking Guest List
copia_guest: list = guest_list.copy()
for i in range(len(guest_list)-2):
    deleted_guest: str = guest_list.pop(-i)
    print(f"Mi dispiace {deleted_guest}, ma non ci danno il tavolo in tempo, non venire pù")
for i in range(len(guest_list)):
    print(f"Ciao {guest_list[i]} non possono darci in tempo il tavolo più grande quindi saremo in meno, ma tu vieni lo stesso")
for i in range(len(guest_list)):
    del guest_list[0]
print(f"Ecco la lista delle persone dopo aver eliminato tutti: {guest_list}")

#3-8 Seeing the World
location: list = ["milano","londra","taipei","dacca","parigi"]
print(f"stampa lista non ordinata: {location}")
print(f"stampa lista ordinata usando sorted: {sorted(location)}")
print(f"stampa lista ordinata al contrario usando sorted: {sorted(location, reverse=True)}")
location.reverse()
print(f"stampa lista con ordine invertito: {location}")
location.reverse()
print(f"stampa lista rimessa apposto: {location}")
location.sort()
print(f"stampa lista usando sort: {location}")
location.sort(reverse=True)
print(f"stampa lista ordinata usando sort e reverse {location}")

#3-9 Dinner Guests
numero_partecipanti: int = len(copia_guest)
print(f"stampa il numero di partecipaneti massimi alla cena {numero_partecipanti}")

#6-1 Person
informazioni: dict = {"first_name": "Davide", "last_name": "Calcagni", "age": 19, "city": "Roma"}
print(f"stampa il dizionario {informazioni}")

#6-2 Favorite Numbers
numeri_preferiti: dict = {"Francesco": 10, "Giualiano": 89, "Luciano": 14, "Massimo": 22, "Giovanni": 67}
print(f"stampa lista di persone e il loro numero preferito {numeri_preferiti}")

#6-3 Glossary
glossario: dict = {"sort":"funzione che modifica il dizionario ordinandolo", 
                   "reverse": "funzione che modifica il dizionario invertendolo", 
                   "pop": "elimina un elemento di una lista dato un indice"
                   }
glossario_key: list = list(glossario.keys())
glossario_value: list = list(glossario.values())
for i in range(len(glossario)):
    print(f"la funzione {glossario_key[i]} e fa: {glossario_value[i]}")

#6-7 People
persone1: dict = {"Maria": "ha i capelli lunghi", "Pietro": "lavora in tribunale", "Claudio": "è un comico"}
persone2: dict = {"Spider-Man": "fa il super eroe", "Peter": "è un persona qualunque", "Batman": "cerca giustizia"}
people: list = []
people.append(informazioni)
people.append(persone1)
people.append(persone2)
print("stampa valori in people")
for i in range(len(people)):
    print(people[i])

#6-8 Pets
garfield: dict = {"tipo": "gatto", "nome padrone": "John"}
hamtaro: dict = {"tipo": "criceto", "nome padrone": "Camilla"}
destiny: dict = {"tipo": "cane","nome padrone": "Stefania"}
pets: list = []
pets.append(garfield)
pets.append(hamtaro)
pets.append(destiny)
print("stampa valori in pets")
for i in range(len(pets)):
    print(pets[i])

#6-9  Favorite Places
#tanto per rendere il tutto un po' più simpatico ho messo che il luogo preferito può cambiare
amici: list = ["Timofte", "Cătălina", "Ștefania"]
lista_luoghi: list = ["Roma", "Tropea", "Napoli", "Firenze", "Frosinone", "Campobasso"]
luoghi_preferiti: dict = {}
for i in range(len(amici)): #in pratica ho fatto una lista con i nomi e diversi luoghi, per ogni persona viene assegnato un luogo
    luoghi_preferiti[amici[i]] = lista_luoghi[random.randint(0, 5)]
    #volendo potevo assegnare una lista di luoghi ad ogni persona ma sarebbe stato più complesso e meno comprensibile
print(f"stampa lista luoghi preferiti con la persona \n {luoghi_preferiti}")

#6-10 Favorite Numbers
lista_persone: list = list(numeri_preferiti.keys())
dizionario_persone_numeri: dict = {}
for i in range(len(lista_persone)): #ciclo for per inserire manualmente i valori, si poteva fare anche senza input ma così è più fico
    #nota ho usato l'input solo per questo esercizio perchè altrimenti ogni prova durava un'eternità
    dizionario_persone_numeri[lista_persone[i]] = input(f"inserisci i numeri preferiti di {lista_persone[i]} (separati da virgole): ").split(",")
    #lo split serve per aggiungere più numeri alla volta, altrimenti si poteva fare con un ciclo while rendendo tutto un po' più completo ma anche complesso
print(f"stampo il dizionario con le persone i loro numeri preferiti\n{dizionario_persone_numeri} ")

#6-11 Cities
cities = {
    "Tokyo": {
        "country": "Japan",
        "population": "approximately 37.4 million",
        "fact": "Tokyo is the most populous metropolitan area in the world."
    },
    "New York City": {
        "country": "United States",
        "population": "approximately 8.4 million",
        "fact": "New York City is often referred to as 'The Big Apple'."
    },
    "London": {
        "country": "United Kingdom",
        "population": "approximately 9.3 million",
        "fact": "London is home to the world's oldest underground railway, known as the Tube."
    }
}
for city, info in cities.items():   #in questo ciclo gira per il primo dizionario dove ci sono scritti solo i nomi delle città
    print(f"\n{city}:")
    for key, value in info.items(): #questo ciclo stampa il dizionario che si trova nei valori del primo
        print(f"{key}: {value}")