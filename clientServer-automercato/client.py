import requests
import sys
import datetime
import json

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

def aggiungi_veicolo():
    tipo_veicolo = input("Inserisci il tipo di veicolo (auto o moto) ")
    targa = input("Inserisci la targa ")
    marca = input("Inserisci la marca ")
    modello = input("Inserisci il modello ")
    prezzo_base = input("Inserisci il prezzo di base ")
    filiale = input("Inserisci l'id della filiale ")
    return {"tipo_veicolo": tipo_veicolo,"targa": targa, "marca": marca, "modello": modello, "prezzo_base": prezzo_base, "filiale":filiale}

def ricercaaccessorio():
    compatibilità = input("Inserisci la compatibilità dell'accessorio ((auto, moto o lasciare vuoto per entrambi) ")
    return {"compatibilità": compatibilità}
def aggiungi_accessorio():
    nome = input("Inserisci il nome dell'accessorio ")
    compatibilita = input("Inserisci per uale tipo di veicolo è usato (auto o moto) ")
    descrizione = input("Inserisci la descrizione dell'accessorio ")
    prezzo = input("Inserisci quanto costa ")
    return {"nome": nome, "compatibilità": compatibilita, "descrizione": descrizione, "prezzo": prezzo}

def ricercavendita():
        data_inizio = input("Inserisci la data di inizio (formato YYYY-MM-DD, inserire un formato sbagliato sarà come una data nulla, lasciare vuoto per non specificare) ")
        data_fine = input("Inserisci la data di fine (formato YYYY-MM-DD, inserire un formato sbagliato sarà come una data nulla, lasciare vuoto per non specificare) ")
        l = {}
        if data_inizio != "":
            try:
                datetime.date.fromisoformat(data_inizio)
            except:
                data_inizio = ""
            finally:
                l["inizio"] = data_inizio
        else:
            l["inizio"] = data_inizio
        
        if data_fine != "":
            try:
                datetime.date.fromisoformat(data_fine)
            except:
                data_fine = ""
            finally:
                l["fine"] = data_fine
        else:
            l["fine"] = data_fine
        return l
    
def inserisci_dati_vendita():
    targa = input("Inserisci la targa del veicolo venduto ")
    data_vendita = input("Inserisci quando è stato venduto (formato YYYY-MM-DD) ")
    prezzo_vendita = input("Inserisci il prezzo di vendita")
    try:
        datetime.date.fromisoformat(data_vendita)
    except:
        data_vendita = "2000-01-01"
    return {"targa": targa, "data_vendita": data_vendita, "prezzo_vendita": prezzo_vendita}
    
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
            print("6. Registra un nuovo admin")
            print("7. Logout")
            print("8. Esci")
            operazione = input("Cosa vuoi fare? ")
            if operazione == "1":
                api_url = base_url + "/inserisci_veicolo"
                jsonDataRequest = aggiungi_veicolo()
                try:
                    response = requests.post(api_url,json=[jsonDataRequest,accesso])
                    print(response.content.decode("UTF-8"))
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")
            elif operazione == "2":
                api_url = base_url + "/inserisci_accessorio"
                jsonDataRequest = aggiungi_accessorio()
                try:
                    response = requests.post(api_url,json=[jsonDataRequest,accesso])
                    print(response.content.decode("UTF-8"))
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")
            elif operazione == "3":
                api_url = base_url + "/inserisci_vendita_auto"
                jsonDataRequest = inserisci_dati_vendita()
                try:
                    response = requests.post(api_url,json=[jsonDataRequest,accesso])
                    print(response.content.decode("UTF-8"))
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")
            elif operazione == "4":
                api_url = base_url + "/inserisci_vendita_moto"
                jsonDataRequest = inserisci_dati_vendita()
                try:
                    response = requests.post(api_url,json=[jsonDataRequest,accesso])
                    print(response.content.decode("UTF-8"))
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")
            elif operazione == "5":
                api_url = base_url + "/ricerca_vendite"
                jsonDataRequest = ricercavendita()
                try:
                    response = requests.post(api_url,json=[jsonDataRequest,accesso])
                    with open("risultati.json", "w") as file:
                        json.dump(response.json(), file, indent=4)
                    print("Risultati salvati in risultati.json")
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")
            elif operazione == "6":
                api_url = base_url + "/registrazione"
                jsonDataRequest = Login()
                try:
                    response = requests.post(api_url,json=[jsonDataRequest,accesso])
                    print(response.content.decode("UTF-8"))
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")
            elif operazione == "7":
                auth = False
                print("Logout effetuato con successo")
                break
            elif operazione=="8":
                print("Buona giornata!")
                sys.exit()  