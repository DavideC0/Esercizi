import requests,json
import sys

base_url = "http://127.0.0.1:8080"

def GetDatiCittadino():
    nome = input("Qual'è il nome? ")
    cognome = input("Qual'è il cognome ")
    dataN = input("Qual'è la data di nascita? ")
    codF = input("Qual'è il codice fiscale? ")
    """
    {
        "nome": "Mario",
        "cognome":"Retti",
        "data nascita": "22/05/2010",
        "codice fiscale": "dfrcde23t44h501u"
    }
    """
    datiCittadino = {codF:{"nome":nome, "cognome": cognome, "dataNascita":dataN}}
    return datiCittadino

def GetCittadino():
    return input("Inserisci il codice fiscale della persona richiesta ")

def UpdateCittadino():
    dati_da_modifcare = [None for _ in range(4)]
    dati_da_modifcare[0] = input("Inserisci il codice fiscale della persona a cui vuoi modificarei i dati")
    nome = input("Inserisci il nome modificato (Lascia vuoto per non cambiare) ")
    cognome = input("Inserisci il cognome modificato (Lascia vuoto per non cambiare) ")
    dataN = input("Inserisci la data di nascita modificata (Lascia vuoto per non cambiare) ")
    if cognome:
        dati_da_modifcare[1] = cognome
    if dataN:
        dati_da_modifcare[2] = dataN
    if nome:
        dati_da_modifcare[3] = nome
    return dati_da_modifcare

def DeleteCittadino():
    return input("Inserisci il codice fiscale della persona da eliminare ")



print("Operazioni disponibili:")
print("1. Inserisci cittadino (es. atto di nascita)")
print("2. Richiedi cittadino (es. cert. residenza)")
print("3. Modifica cittadino (es. cambio residenza)")
print("4. Elimina cittadino (es. trasferim altro comune)")
print("5. Esci")
sOper = input("Cosa vuoi fare? ")
while(True):
    if sOper == "1":
        print("Richiesto atto di nascita")
        api_url = base_url + "/add_cittadino"
        jsonDataRequest = GetDatiCittadino()
        try:
            response = requests.post(api_url,json=jsonDataRequest)
            print(response)
        
        except:
            print("Problemi di comunicazione con il server, riprova più tardi")
    elif sOper == "2":
        print("Richiesto cittadino")
        api_url = base_url + "/read_cittadino"
        jsonDataRequest = GetCittadino()
        try:
            response = requests.post(api_url,json=jsonDataRequest)
            print(response.content)
            
        except:
            print("Problemi di comunicazione con il server, riprova più tardi")
    elif sOper == "3":
        print("Richiesto cittadino")
        api_url = base_url + "/update_cittadino"
        jsonDataRequest = UpdateCittadino()
        try:
            response = requests.post(api_url,json=jsonDataRequest)
            print(response.content)
            
        except:
            print("Problemi di comunicazione con il server, riprova più tardi")
    elif sOper == "4":
        print("Richiesto cittadino")
        api_url = base_url + "/delete_cittadino"
        jsonDataRequest = DeleteCittadino()
        try:
            response = requests.post(api_url,json=jsonDataRequest)
            print(response.content)
            
        except:
            print("Problemi di comunicazione con il server, riprova più tardi")
    elif sOper=="5":
        print("Buona giornata!")
        sys.exit()
    print("Operazioni disponibili:")
    print("1. Inserisci cittadino (es. atto di nascita) ")
    print("2. Richiedi cittadino (es. cert. residenza) ")
    print("3. Modifica cittadino (es. cambio residenza)")
    print("4. Elimina cittadino (es. trasferim altro comune) ")
    print("5. Esci")
    sOper = input("Cosa vuoi fare? ")    