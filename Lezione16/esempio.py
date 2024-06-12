# reader = open("esempio.txt")

# try:
#     print(reader.readline())
#     print(f"Sono nella try")
#     raise Exception(f"Eccezione")

# except Exception:
#     print(f"Sono nella exept")
    
# finally:
#     print(reader)
#     reader.close()
#     print(f"Sono nella finally")

with open("esempio.txt") as reader:
    line = reader.readline()
    line_counter = 0
    while line != '':
        print(f"{line} - number: {line_counter}")
        line = reader.readline()
        line_counter += 1
        
with open("esempioCorto.txt", "a") as reader:
    l = ["ciao sono flavio\n", "ciao sono maria\n", "ciao sono luca\n"]
    reader.writelines(l)