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