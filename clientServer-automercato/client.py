import requests,json
import sys

base_url = "http://127.0.0.1:8080"
auth = False

def Login():
    username = input("Inserisci l'username ")
    password = input("Inserisci la password ")
    return {"username": username, "password": password}

def ricercaveicolo():
    tipo_veicolo = input("Inserisci il tipo di veicolo (auto o moto) ")
    marca = input("Inserisci la marca (lasciare vuoto per non specificare) ")
    modello = input("Inserisci il modello (lasciare vuoto per non specificare) ")
    l = {"tipo_veicolo": tipo_veicolo}
    if marca:
        l["marca"] = marca
    else:
        l["marca"] = False
    if modello:
        l["modello"] = modello
    else:
        l["modello"] = False
    return l

def ricercaaccessorio():
    compatibilità = input("Inserisci la compatibilità dell'accessorio ((auto, moto o lasciare vuoto per entrambi) ")
    return {"compatibilità": compatibilità}
    

stato = -1
while True:
    if not auth:
        print("Operazioni disponibili:")
        print("1. Login (Solo per admin per aggiunta di nuovi elementi o nuovi utenti admin)")
        print("2. Ricerca di un auto o moto")
        print("3. Ricerca accessori veicolo")
        print("4. Esci")
        operazione = input("Cosa vuoi fare? ")
        if operazione == '1':
            api_url = base_url + '/login'
            accesso = Login()
            try:
                response = requests.post(api_url,json=accesso)
                print(response.content)
                jResponse = response.json()
                if jResponse['Esito'] == "ok":
                    auth = True
                    print(jResponse['messaggio'])
            except Exception as e:
                print(e)
                print("Problemi di comunicazione con il server, riprova più tardi")
        elif operazione == '2':
            api_url = base_url + '/ricerca_veicolo'
            jsonDataRequest = ricercaveicolo()
            try:
                response = requests.post(api_url,json=jsonDataRequest)
                print(response.content.decode('UTF-8'))
            except:
                print("Problemi di comunicazione con il server, riprova più tardi")
        elif operazione == '3':
            api_url = base_url + '/ricerca_accessorio'
            jsonDataRequest = ricercaaccessorio()
            try:
                response = requests.post(api_url,json=jsonDataRequest)
                print(response.content.decode('UTF-8'))
            except:
                print("Problemi di comunicazione con il server, riprova più tardi")
        elif operazione == '4':
            sys.exit()
        else:
            print("Errore operazione non esistente")
    else:        
        while(True):
            print("Operazioni disponibili:")
            print("1. Inserisci un nuovo veicolo")
            print("2. Inserisci un nuovo accessorio")
            print("3. Inserisci dati di vendita di un auto")
            print("4. Inserisci dati di vendita di una moto")
            print("5. Ottieni report vendite")
            print("6. Ottieni report vendite tra due date")
            print("7. Logout")
            print("8. Esci")
            sOper = input("Cosa vuoi fare? ")
            if sOper == "1":
                print("Richiesto atto di nascita")
                api_url = base_url + "/add_cittadino"
                jsonDataRequest = GetDatiCittadino()
                try:
                    response = requests.post(api_url,json=[jsonDataRequest,accesso], verify=False)
                    print(response.content)
                
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")
            elif sOper == "2":
                print("Richiesto cittadino")
                api_url = base_url + "/read_cittadino"
                jsonDataRequest = GetCittadino()
                try:
                    response = requests.post(api_url,json=[jsonDataRequest,accesso], verify=False)
                    print(response.content)
                    
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")
            elif sOper == "3":
                print("Richiesto cittadino")
                api_url = base_url + "/update_cittadino"
                jsonDataRequest = UpdateCittadino()
                try:
                    response = requests.post(api_url,json=[jsonDataRequest,accesso], verify=False)
                    print(response.content)
                    
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")
            elif sOper == "4":
                print("Richiesto cittadino")
                api_url = base_url + "/delete_cittadino"
                jsonDataRequest = DeleteCittadino()
                try:
                    response = requests.post(api_url,json=[jsonDataRequest,accesso], verify=False)
                    print(response.content)
                    
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")
            elif sOper == "7":
                auth = False
                print("Logout effetuato con successo")
                break
            elif sOper=="8":
                print("Buona giornata!")
                sys.exit()  