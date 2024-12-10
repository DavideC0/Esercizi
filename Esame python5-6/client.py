import requests
import sys
import datetime
import json

base_url = "http://127.0.0.1:8080"
auth = False
auth_mark = False
auth_fil = False

def Login():
    username = input("Inserisci l'username ")
    password = input("Inserisci la password ")
    return {"username": username, "password": password}

def ricercaCasa():
    ricerca = {}
    ricerca['indirizzo'] = input("Inserisci l'indirizzo (Lasciare vuoto per non specificare) ")
    ricerca['metrimin'] = input("Inserisci il minimo di metri quadrati (Lasciare vuoto per non specificare) ")
    ricerca['prezzomax'] = input("Inserisci il prezzo massimo (Lasciare vuoto per non specificare) ")
    return ricerca

def ricercaCasaAffitto():
    ricerca = {}
    ricerca['tipo'] = input("Tipo di affitto totale o parziale? ").upper()
    ricerca['indirizzo'] = input("Inserisci l'indirizzo (Lasciare vuoto per non specificare) ")
    ricerca['prezzomax'] = input("Inserisci il prezzo massimo (Lasciare vuoto per non specificare) ")
    return ricerca

def vendiCasa():
    ricerca = {}
    ricerca['catastale'] = input("Inserisci il catastale ")
    ricerca['data'] = str(datetime.date.today())
    ricerca['proponente'] = input("Inserisci la filiale proponente ")
    ricerca['venditrice'] = input("Inserisci la filiale venditice (lascia vuoto se è la stessa proponente) ")
    if not ricerca['venditrice']:
        ricerca['venditrice'] = ricerca['proponente']
    ricerca['prezzo'] = input("Inserisci il prezzo di vendita ")
    return ricerca

def affittaCasa():
    ricerca = {}
    ricerca['catastale'] = input("Inserisci il catastale ")
    ricerca['data'] = str(datetime.date.today())
    ricerca['proponente'] = input("Inserisci la filiale proponente ")
    ricerca['venditrice'] = input("Inserisci la filiale venditice (lascia vuoto se è la stessa proponente) ")
    if not ricerca['venditrice']:
        ricerca['venditrice'] = ricerca['proponente']
    ricerca['prezzo'] = input("Inserisci il prezzo di vendita ")
    ricerca['durata'] = input("Inserisci la durata del contratto in mesi ")
    return ricerca

def ottieniPeriodo():
    periodo = {}
    periodo['inizio'] = input("Inserisci l'inizio del periodo in formato YYYY-MM-DD ")
    periodo['fine'] = input("Insersici la fine del periodo in formato YYYY-MM-DD ")
    return periodo

def datiVendita():
    dati = {}
    dati['catastale'] = input("Inserisci il codice catastale ")
    dati['indirzzo'] = input("Inserisci l'indirizzo")
    dati['civico'] = input("Inserisci il numero civico")
    dati['piano'] = input("Inserisci il piano")
    dati['metri'] = input("Inserisci la grandezza in metri quadrati")
    dati['vani'] = input("Inserisci i vani")
    dati['prezzo'] = input("Inserisci il prezzo")
    dati['filiale'] = input("Inserisci la filiale di appartenenza")
    return dati

def datiAffitto():
    dati = {}
    dati['catastale'] = input("Inserisci il codice catastale ")
    dati['indirzzo'] = input("Inserisci l'indirizzo")
    dati['civico'] = input("Inserisci il numero civico")
    dati['tipo'] = input("Inserisci il tipo di affitto (totale/parziale)").upper()
    dati['bagno'] = input("Inserisci se il bagno è personale (True/False)")
    dati['prezzo'] = input("Inserisci il prezzo")
    dati['filiale'] = input("Inserisci la filiale di appartenenza")
    return dati
    
    
while True:
    if not auth:
        print("Operazioni disponibili:")
        print("1. Login")
        print("2. Esci")
        operazione = input("Cosa vuoi fare? ")
        if operazione == '1':
            api_url = base_url + '/login'
            accesso = Login()
            try:
                response = requests.post(api_url,json=accesso)
                jResponse = response.json()
                print(jResponse["tipo"][0])
                if jResponse["tipo"][0] == "FILIALE":
                    auth = True
                    auth_fil = True
                    print("Login effettuato")
                elif jResponse["tipo"][0] == "MARKETING":
                    auth = True
                    auth_mark = True
                    print("Login effetuato")
                else:
                    print("Errore nel login")
            except Exception as e:
                print(e)
                print("Problemi di comunicazione con il server, riprova più tardi")
        elif operazione == '2':
            sys.exit()
        else:
            print("Errore operazione non esistente")
    else:
        if auth_fil:
            while True:
                print("Operazioni disponibili:")
                print("1. Ricerca di una casa in vendita")
                print("2. Ricerca di una casa in affitto")
                print("3. Vendi una casa")
                print("4. Affitta una casa")
                print("5. Aggiungi una casa da vendere")
                print("6. Aggiungi una casa da affitare")
                print("7. Logout")
                print("8. Esci")
                operazione = input("Cosa vuoi fare? ")
                if operazione == "1":
                    api_url = base_url + "/ricerca_casa_vendita"
                    jsonDataRequest = ricercaCasa()
                    try:
                        response = requests.post(api_url,json=[jsonDataRequest,accesso])
                        print(response.content.decode("UTF-8"))
                    except:
                        print("Problemi di comunicazione con il server, riprova più tardi")
                elif operazione == "2":
                    api_url = base_url + "/ricerca_casa_affitto"
                    jsonDataRequest = ricercaCasaAffitto()
                    try:
                        response = requests.post(api_url,json=[jsonDataRequest,accesso])
                        print(response.content.decode("UTF-8"))
                    except:
                        print("Problemi di comunicazione con il server, riprova più tardi")
                elif operazione == "3":
                    api_url = base_url + "/inserisci_vendita_casa"
                    jsonDataRequest = vendiCasa()
                    try:
                        response = requests.post(api_url,json=[jsonDataRequest,accesso])
                        print(response.content.decode("UTF-8"))
                    except Exception as e:
                        print(e)
                        print("Problemi di comunicazione con il server, riprova più tardi")
                elif operazione == "4":
                    api_url = base_url + "/inserisci_affitto_casa"
                    jsonDataRequest = affittaCasa()
                    try:
                        response = requests.post(api_url,json=[jsonDataRequest,accesso])
                        print(response.content.decode("UTF-8"))
                    except:
                        print("Problemi di comunicazione con il server, riprova più tardi")
                elif operazione == "5":
                    api_url = base_url + "/aggiungi_casa_daVendere"
                    jsonDataRequest = datiVendita()
                    try:
                        response = requests.post(api_url,json=[jsonDataRequest,accesso])
                        print(response.content.decode("UTF-8"))
                    except Exception as e:
                        print(e)
                        print("Problemi di comunicazione con il server, riprova più tardi")
                elif operazione == "6":
                    api_url = base_url + "/aggiungi_casa_daAffitare"
                    jsonDataRequest = datiAffitto()
                    try:
                        response = requests.post(api_url,json=[jsonDataRequest,accesso])
                        print(response.content.decode("UTF-8"))
                    except Exception as e:
                        print(e)
                        print("Problemi di comunicazione con il server, riprova più tardi")
                elif operazione == "7":
                    auth = False
                    auth_fil = False
                    print("Logout effetuato con successo")
                    break
                elif operazione=="8":
                    print("Buona giornata!")
                    sys.exit()
        elif auth_mark:
            while True:
                print("Operazioni disponibili:")
                print("1. Ottieni dati di vendita e affitti per filiale in un periodo")
                print("2. Calcola i guadigni in un periodo")
                print("3. Logout")
                print("4. Esci")
                operazione = input("Cosa vuoi fare? ")
                if operazione == "1":
                    api_url = base_url + "/ottieni_vendite"
                    jsonDataRequest = ottieniPeriodo()
                    try:
                        response = requests.post(api_url,json=[jsonDataRequest,accesso])
                        nome = "Log vendite " + str(datetime.datetime.now()) + ".json"
                        with open(nome, "w") as file:
                            json.dump(response.json(), file, indent=4)
                            print(f"Report salvato in {nome}")
                    except:
                        print("Problemi di comunicazione con il server, riprova più tardi")
                elif operazione == "2":
                    api_url = base_url + "/ottieni_guadagni"
                    jsonDataRequest = ottieniPeriodo()
                    try:
                        response = requests.post(api_url,json=[jsonDataRequest,accesso])
                        nome = "Log guadagni " + str(datetime.datetime.now()) + ".json"
                        with open(nome, "w") as file:
                            json.dump(response.json(), file, indent=4)
                            print(f"Report salvato in {nome}")
                    except:
                        print("Problemi di comunicazione con il server, riprova più tardi")
                elif operazione == "3":
                    auth = False
                    auth_mark = False
                    print("Logout effetuato con successo")
                    break
                elif operazione=="4":
                    print("Buona giornata!")
                    sys.exit()
        else:
            print("Errore")
            sys.exit()