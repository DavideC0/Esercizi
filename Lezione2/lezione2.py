#Davide Calcagni
#18/04/2024

print("Hello World")
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