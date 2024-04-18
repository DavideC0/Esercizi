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
