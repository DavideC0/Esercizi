from flask import Flask, request
import random
import dbclient as db
import sys

api = Flask(__name__)
mydb = db.connect()
if mydb is None:
    print("Errore connessione al DB")
    sys.exit()
    
def controllo_privilegi_admin(user: dict):
    for key, value in user.items():
        sQuery = f"select stato from utenti where username = '{key}' and pass = '{value[0]}';"
        print(sQuery)
        iNumRecord = db.read_in_db(mydb, sQuery)
        if iNumRecord == 1:
            lRecord = db.read_next_row(mydb)
            iStato = lRecord[1][0]
            return iStato
        return False
    
def convert_query_toString(l: list):
    s = ""
    for elem in l:
        s += "Targa= " + elem[0] + " Marca= " + elem[1] + " Modello= " + elem[2] + "\n"    
    return s
    
    
@api.route('/login', methods=['POST'])
def login():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        iStato = -1
        for key, value in request.json.items():
            sQuery = f"select stato from utenti where username = '{key}' and pass = '{value[0]}';"
            print(sQuery)
            iNumRecord = db.read_in_db(mydb, sQuery)
            if iNumRecord == 1:
                print("Login terminato correttamente")
                lRecord = db.read_next_row(mydb)
                iStato = lRecord[1][0]
                return '{"Esito":"ok", "Stato": ' + str(iStato) + '}'
            elif iNumRecord == 0:
                print("Credenziali errate")
                return '{"Esito":"ko", "Stato": ' + str(iStato) + '}'
            elif iNumRecord <= -1:
                print("Dati errati")
                return '{"Esito":"ko", "Stato": ' + str(iStato) + '}'
            else:
                print("Attenzione: attacco in corso")
                return '{"Esito":"ko", "Stato": ' + str(iStato) + '}'
    else:
        return 'Content-Type not supported!'

@api.route('/registrazione', methods=['POST'])
def Registrazione():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        for key, value in request.json.items():
            sQuery = f"insert into utenti(username,pass,stato) values ('{key}', '{value[0]}',{random.randint(0,1)})"
            print(sQuery)
            iRetValue = db.write_in_db(mydb, sQuery) #restituisce 0 se è andato tutto bene, -1 errore, -2 duplicate key
            print(iRetValue)
            if iRetValue == -2:
                return "Nome utente già in uso"
            elif iRetValue == 0:
                return "Registrazione avvenuta con successo"
            else:
                return "Errore non gestito nella registrazione"
        return "Errore richiesta non conforme"
    else:
        return 'Content-Type not supported!'
    
@api.route('/ricerca_veicolo', methods=['POST'])
def ricerca_veicolo():
    content_type = request.headers.get('Content_Type')
    if (content_type == 'application/json'):
        data = request.json
        l = []
        if data["tipo_veicolo"] == 'auto' or  data["tipo_veicolo"] == 'Auto' or  data["tipo_veicolo"] == 'automobile' or  data["tipo_veicolo"] == 'Automobile':
            if data["marca"] and data["modello"]:
                #query con entrambi
                marca = data["marca"]
                modello = data["modello"]
                query = f"select * from Automobile where marca = '{marca}' and modello = '{modello}'"
                db.read_in_db(mydb, query)
                for elem in mydb:
                    l.append(elem)
                return convert_query_toString(l)
            elif data["marca"] and not data["modello"]:
                #query con soltanto il primo
                marca = data["marca"]
                query = f"select * from Automobile where marca = '{marca}'"
                db.read_in_db(mydb,query)
                for elem in mydb:
                    l.append(elem)
                return convert_query_toString(l)
            elif not data["marca"] and data["modello"]:
                #query con soltato il secondo elemento
                modello = data["modello"]
                query = f"select * from Automobile where modello = '{modello}'"
                db.read_in_db(mydb, query)
                for elem in mydb:
                    l.append(elem)
                return convert_query_toString(l)
            else:
                query = f"select * from Automobile"
                db.read_in_db(mydb, query)
                for elem in mydb:
                    l.append(elem)
                return convert_query_toString(l)
        elif data["tipo_veicolo"] == 'moto' or data["tipo_veicolo"] == 'Moto' or data["tipo_veicolo"] == 'motocicletta' or data["tipo_veicolo"] == 'Motocicletta':
            if data["marca"] and data["modello"]:
                #query con entrambi
                marca = data["marca"]
                modello = data["modello"]
                query = f"select * from Motocicletta where marca = '{marca}' and modello = '{modello}'"
                db.read_in_db(mydb, query)
                for elem in mydb:
                    l.append(elem)
                return convert_query_toString(l)
            elif data["marca"] and not data["modello"]:
                #query con soltanto il primo
                marca = data["marca"]
                query = f"select * from Motocicletta where marca = '{marca}'"
                db.read_in_db(mydb, query)
                for elem in mydb:
                    l.append(elem)
                return convert_query_toString(l)
            elif not data["marca"] and data["modello"]:
                #query con soltato il secondo elemento
                modello = data["modello"]
                query = f"select * from Motocicletta wheremodello = '{modello}'"
                db.read_in_db(mydb, query)
                for elem in mydb:
                    l.append(elem)
                return convert_query_toString(l)
            else:
                #query con nessun elemento specificato
                query = f"select * from Motocicletta"
                db.read_in_db(mydb, query)
                for elem in mydb:
                    l.append(elem)
                return convert_query_toString(l)
        else:
            return 'Tipo veicolo inserito non esistente'

api.run(host="127.0.0.1", port=8080)   