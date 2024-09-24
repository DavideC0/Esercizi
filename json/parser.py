def serializza(mylist: str):
    mylist = mylist[1:-1]
    mylist = mylist.replace(" ","")
    mylist = mylist.split(",")
    for i in range(len(mylist)):
        mylist[i] = mylist[i][1:-1]
    return mylist

def deserializza(mylist):
    lista = "["
    for i in range(len(mylist)):
        lista += "'" + mylist[i] + "', "
    lista = lista[:-2]
    lista += "]"
    return lista

mylist_1 = "['mario', 'gino','lucrezia']"
mylist_2 = ['mario', 'gino','lucrezia']

print(f"Stampa la lista uno con la serializzazione {serializza(mylist_1)} passaggio da tipo stringa a {type(serializza(mylist_1))}")
print(f"Stampa la lista uno con la deserializzazione {deserializza(mylist_2)} passaggio da tipo stringa a {type(deserializza(mylist_2))}")

