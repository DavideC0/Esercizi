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
    username = user["username"]
    password = user["password"]
    query = f"select * from utente where username = '{username}' and password = '{password}'"
    n_record = db.read_in_db(mydb,query)
    if n_record == 1:
        return True
    return False
    
def convert_query_toString_veicolo(l: list):
    s = ""
    for elem in l:
        s += "Targa= " + elem[0] + " Marca= " + elem[1] + " Modello= " + elem[2] + " Prezzo base= " + str(elem[3]) + "Filiale= "+ elem[4] + "\n"    
    return s

def convert_query_toString_accessorio(l: list):
    s = ""
    for elem in l:
        s += "Id= " + str(elem[0]) + " Nome= " + elem[1] + " Compatibilità= " + elem[2] + " Descrizione= " + elem[3] + " Prezzo= " + str(elem[4]) + "\n"
    return s

def convert_query_toString_vendita(l: list):
    s = ""
    for elem in l:
        s += "Targa= " + elem["targa"] + " Marca= " + elem["marca"] + " Modello= " + elem["modello"] + " Prezzo iniziale= " + str(elem["prezzo_base"]) + " Data di vendita= " + str(elem["data_vendita"]) + " Prezzo di vendita= " + str(elem["prezzo_vendita"]) + "\n"
    return s
    
@api.route('/login', methods=['POST'])
def login():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        dati_login = request.json
        username = dati_login["username"]
        password = dati_login["password"]
        query = f"select * from utente where username = '{username}' and password = '{password}'"
        n_record = db.read_in_db(mydb,query)        
        if n_record == 1:
            return '{"Esito":"ok", "messaggio": "Login terminato con successo"}'
        elif n_record == 0:
            return '{"Esito":"ko", "messaggio": "Credenziali errate"}'
        elif n_record <= -1:
            print("Dati errati")
            return '{"Esito":"ko", "messaggio": "Dati errati"}'
        else:
            return '{"Esito":"ko", "messaggio": "Errore generico"}'
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
                query = f"select a.targa, a.marca, a.modello, a.prezzo_base, f.nome from Automobile a, filiale f where a.filiale = f.id and marca = '{marca}' and modello = '{modello}'"
                db.read_in_db(mydb, query)
                for elem in mydb:
                    l.append(elem)
                return convert_query_toString_veicolo(l)
            elif data["marca"] and not data["modello"]:
                #query con soltanto il primo
                marca = data["marca"]
                query = f"select a.targa, a.marca, a.modello, a.prezzo_base, f.nome from Automobile a, filiale f where a.filiale = f.id and marca = '{marca}'"
                db.read_in_db(mydb,query)
                for elem in mydb:
                    l.append(elem)
                return convert_query_toString_veicolo(l)
            elif not data["marca"] and data["modello"]:
                #query con soltato il secondo elemento
                modello = data["modello"]
                query = f"select a.targa, a.marca, a.modello, a.prezzo_base, f.nome from Automobile a, filiale f where a.filiale = f.id and modello = '{modello}'"
                db.read_in_db(mydb, query)
                for elem in mydb:
                    l.append(elem)
                return convert_query_toString_veicolo(l)
            else:
                query = f"select a.targa, a.marca, a.modello, a.prezzo_base, f.nome from Automobile a, filiale f where a.filiale = f.id"
                db.read_in_db(mydb, query)
                for elem in mydb:
                    l.append(elem)
                return convert_query_toString_veicolo(l)
        elif data["tipo_veicolo"] == 'moto' or data["tipo_veicolo"] == 'Moto' or data["tipo_veicolo"] == 'motocicletta' or data["tipo_veicolo"] == 'Motocicletta':
            if data["marca"] and data["modello"]:
                #query con entrambi
                marca = data["marca"]
                modello = data["modello"]
                query = f"select a.targa, a.marca, a.modello, a.prezzo_base, f.nome from Motocicletta a, filiale f where a.filiale = f.id and marca = '{marca}' and modello = '{modello}'"
                db.read_in_db(mydb, query)
                for elem in mydb:
                    l.append(elem)
                return convert_query_toString_veicolo(l)
            elif data["marca"] and not data["modello"]:
                #query con soltanto il primo
                marca = data["marca"]
                query = f"select a.targa, a.marca, a.modello, a.prezzo_base, f.nome from Motocicletta a, filiale f where a.filiale = f.id and marca = '{marca}'"
                db.read_in_db(mydb, query)
                for elem in mydb:
                    l.append(elem)
                return convert_query_toString_veicolo(l)
            elif not data["marca"] and data["modello"]:
                #query con soltato il secondo elemento
                modello = data["modello"]
                query = f"select a.targa, a.marca, a.modello, a.prezzo_base, f.nome from Motocicletta a, filiale f where a.filiale = f.id modello = '{modello}'"
                db.read_in_db(mydb, query)
                for elem in mydb:
                    l.append(elem)
                return convert_query_toString_veicolo(l)
            else:
                #query con nessun elemento specificato
                query = f"select a.targa, a.marca, a.modello, a.prezzo_base, f.nome from Motocicletta a, filiale f where a.filiale = f.id"
                db.read_in_db(mydb, query)
                for elem in mydb:
                    l.append(elem)
                return convert_query_toString_veicolo(l)
        else:
            return 'Tipo veicolo inserito non esistente'
        
@api.route('/ricerca_accessorio', methods=['POST'])
def ricerca_accessorio():
    content_type = request.headers.get('Content_Type')
    if (content_type == 'application/json'):
        data = request.json
        l = []
        if data["compatibilità"] == 'auto' or  data["compatibilità"] == 'Auto' or  data["compatibilità"] == 'automobile' or  data["compatibilità"] == 'Automobile':
            query = f"select * from Acessorio where tipo_veicolo_compatibilità = 'Auto'"
            db.read_in_db(mydb,query)
            for elem in mydb:
                l.append(elem)
            return convert_query_toString_accessorio(l)
        elif data["compatibilità"] == 'moto' or  data["compatibilità"] == 'Moto' or  data["compatibilità"] == 'motocicletta' or  data["compatibilità"] == 'Motocicletta':
            query = f"select * from Acessorio where tipo_veicolo_compatibilità = 'Moto'"
            db.read_in_db(mydb,query)
            for elem in mydb:
                l.append(elem)
            return convert_query_toString_accessorio(l)
        elif data["compatibilità"] == "":
            query = f"select * from Acessorio"
            db.read_in_db(mydb,query)
            for elem in mydb:
                l.append(elem)
            return convert_query_toString_accessorio(l)
        else:
            return "Tipologia di compatibilità inesistente"
        
@api.route('/ricerca_vendite', methods=['POST'])
def ricerca_vendite():
    content_type = request.headers.get('Content_Type')
    if (content_type == 'application/json'):
        data = request.json[0]
        accesso = request.json[1]
        if controllo_privilegi_admin(accesso):
            l = []
            if data["inizio"] != "" and data["fine"] != "":
                #query con entrambi i limiti data_vendita between '{inizio}' and '{fine}'
                inizio = data["inizio"]
                fine = data["fine"]
                query = f"select json_agg(t) from (select a.targa, a.marca, a.modello, a.prezzo_base, v.data_vendita, v.prezzo_vendita from vendita_auto v, Automobile a where data_vendita between '{inizio}' and '{fine}' and a.targa = v.targa_auto union select m.targa, m.marca, m.modello, m.prezzo_base, v.data_vendita, v.prezzo_vendita from vendita_moto v, motocicletta m where data_vendita between '{inizio}' and '{fine}' and m.targa = v.targa_moto) t"
                db.read_in_db(mydb,query)
                for elem in mydb:
                    l.append(elem)
                return l[0][0]
            elif data["inizio"] != "" and data["fine"] == "":
                #query con solatanto il limite iniziale
                inizio = data["inizio"]
                query = f"select json_agg(t) from (select a.targa, a.marca, a.modello, a.prezzo_base, v.data_vendita, v.prezzo_vendita from vendita_auto v, Automobile a where data_vendita > '{inizio}' and a.targa = v.targa_auto union select m.targa, m.marca, m.modello, m.prezzo_base, v.data_vendita, v.prezzo_vendita from vendita_moto v, motocicletta m where data_vendita > '{inizio}' and m.targa = v.targa_moto) t"
                db.read_in_db(mydb,query)
                for elem in mydb:
                    l.append(elem)
                return l[0][0]
            elif data["inizio"] == "" and data["fine"] != "":
                #query con soltanto il limite finale
                fine = data["fine"]
                query = f"select json_agg(t) from (select a.targa, a.marca, a.modello, a.prezzo_base, v.data_vendita, v.prezzo_vendita from vendita_auto v, Automobile a where data_vendita <'{fine}' and a.targa = v.targa_auto union select m.targa, m.marca, m.modello, m.prezzo_base, v.data_vendita, v.prezzo_vendita from vendita_moto v, motocicletta m where data_vendita <'{fine}' and m.targa = v.targa_moto) t"
                db.read_in_db(mydb,query)
                for elem in mydb:
                    l.append(elem)
                return l[0][0]
            else:
                #query con tutto
                query = f"select json_agg(t) from (select a.targa, a.marca, a.modello, a.prezzo_base, v.data_vendita, v.prezzo_vendita from vendita_auto v, Automobile a where a.targa = v.targa_auto union select m.targa, m.marca, m.modello, m.prezzo_base, v.data_vendita, v.prezzo_vendita from vendita_moto v, motocicletta m where m.targa = v.targa_moto) t"
                db.read_in_db(mydb,query)
                for elem in mydb:
                    l.append(elem)
                return l[0][0]
        return "Bad credentials"
    
@api.route('/inserisci_veicolo', methods=['POST'])
def inserisci_veicolo():
    content_type = request.headers.get('Content_Type')
    if (content_type == 'application/json'):
        data = request.json[0]
        accesso = request.json[1]
        if controllo_privilegi_admin(accesso):
            try:
                data['prezzo_base'] = float(data["prezzo_base"])
            except:
                return "Il prezzo base inserito non è un tipo valido"
            try:
                data["filiale"] = int(data["filiale"])
            except:
                return "Il tipo di id della filiale inserita è sbagliato"
            if data["tipo_veicolo"] == 'auto' or  data["tipo_veicolo"] == 'Auto' or  data["tipo_veicolo"] == 'automobile' or  data["tipo_veicolo"] == 'Automobile':
                print("auto")
                targa = data["targa"]
                marca = data["marca"]
                modello = data["modello"]
                prezzo = data["prezzo_base"]
                filiale = data["filiale"]
                query = f"insert into automobile (targa, marca, modello, prezzo_base, filiale) values ('{targa}', '{marca}', '{modello}', '{prezzo}', '{filiale}')"
                try:
                    db.write_in_db(mydb,query)
                except Exception as e:
                    print(e)
                    return "Errore nell'inserimento"
                return "Automobile aggiunta con successo"
            elif data["tipo_veicolo"] == 'moto' or data["tipo_veicolo"] == 'Moto' or data["tipo_veicolo"] == 'motocicletta' or data["tipo_veicolo"] == 'Motocicletta':
                print("moto")
                targa = data["targa"]
                marca = data["marca"]
                modello = data["modello"]
                prezzo = data["prezzo_base"]
                filiale = data["filiale"]
                query = f"insert into motocicletta (targa, marca, modello, prezzo_base, filiale) values ('{targa}', '{marca}', '{modello}', '{prezzo}', '{filiale}')"
                try:
                    db.write_in_db(mydb,query)
                except Exception as e:
                    print(e)
                    return "Errore nell'inserimento"
                return "Motocicletta aggiunta con successo"
            else:
                print("niente")
                return "La tipologia inserita non è supportata"
        return "Bad credentials"

@api.route('/inserisci_accessorio', methods=['POST'])
def inserisci_accessorio():
    content_type = request.headers.get('Content_Type')
    if (content_type == 'application/json'):
        data = request.json[0]
        accesso = request.json[1]
        if controllo_privilegi_admin(accesso):
            try:
                data["prezzo"] = float(data["prezzo"])
            except:
                return "Prezzo inserito non valido"
            if data["compatibilità"] == 'auto' or  data["compatibilità"] == 'Auto' or  data["compatibilità"] == 'automobile' or  data["compatibilità"] == 'Automobile':
                compatibilità = "Auto"
            elif data["compatibilità"] == 'moto' or  data["compatibilità"] == 'Moto' or  data["compatibilità"] == 'motocicletta' or  data["compatibilità"] == 'Motocicletta':
                compatibilità = "Moto"
            else:
                return "Tipologia di compatibilità non esistente"
            nome = data["nome"]
            descrizione = data["descrizione"]
            prezzo = data["prezzo"]
            query = f"insert into acessorio (nome,tipo_veicolo_compatibilità,descrizione,prezzo) values ('{nome}','{compatibilità}','{descrizione}','{prezzo}')"
            try:
                db.write_in_db(mydb,query)
            except Exception as e:
                print(e)
                return "Errore nell'inserimento"
            return "Inserimento avvenuto con successo"
        return "Bad credentials"

@api.route('/inserisci_vendita_auto', methods=['POST'])
def inserisci_vendita_auto():
    content_type = request.headers.get('Content_Type')
    if (content_type == 'application/json'):
        data = request.json[0]
        accesso = request.json[1]
        if controllo_privilegi_admin(accesso):
            targa = data["targa"]
            data_vendita = data["data_vendita"]
            prezzo_vendita = data["prezzo_vendita"]
            query = f"insert into vendita_auto (targa_auto,data_vendita,prezzo_vendita) values ('{targa}','{data_vendita}','{prezzo_vendita}')"
            try:
                db.write_in_db(mydb,query)
            except:
                return "Errore nell'inserimento"
            return "Inserimento avvenuto con successo"
        return "Bad credentials"
    
@api.route('/inserisci_vendita_moto', methods=['POST'])
def inserisci_vendita_moto():
    content_type = request.headers.get('Content_Type')
    if (content_type == 'application/json'):
        data = request.json[0]
        accesso = request.json[1]
        if controllo_privilegi_admin(accesso):
            targa = data["targa"]
            data_vendita = data["data_vendita"]
            prezzo_vendita = data["prezzo_vendita"]
            query = f"insert into vendita_moto (targa_moto,data_vendita,prezzo_vendita) values ('{targa}','{data_vendita}','{prezzo_vendita}')"
            try:
                db.write_in_db(mydb,query)
            except:
                return "Errore nell'inserimento"
            return "Inserimento avvenuto con successo"
        return "Bad credentials"
api.run(host="127.0.0.1", port=8080)