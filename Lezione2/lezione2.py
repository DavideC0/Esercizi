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