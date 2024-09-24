def serializza(mylist):
    lista = "["
    for i in range(len(mylist)):
        lista += "'" + mylist[i] + "',"
    lista = lista[:-1]
    lista += "]"
    return lista

def deserializza(mylist: str):
    mylist = mylist[1:-1]
    mylist = mylist.replace(" ","")
    mylist = mylist.split(",")
    for i in range(len(mylist)):
        mylist[i] = mylist[i][1:-1]
    return mylist

mylist_1 = "['mario','gino','lucrezia']"
mylist_2 = ['mario','gino','lucrezia']

smylist = serializza(mylist_2)
dmylist = deserializza(mylist_1)
if smylist == mylist_1:
    print("Funzione di serializza avvenuta con successo")
else:
    print("Funzione di serializzazione non avvenuta")

if dmylist == mylist_2:
    print("Funzione di deserializza avvenuta con successo")
else:
    print("Funzione di deserializza non avvenuta")