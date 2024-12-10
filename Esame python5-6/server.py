from flask import Flask, request
import random
import dbclient as db
import sys

api = Flask(__name__)
mydb = db.connect()
if mydb is None:
    print("Errore connessione al DB")
    sys.exit()
    
def controllo_privilegi_filiale(user: dict):
    username = user["username"]
    password = user["password"]
    query = f"select * from utenti where username = '{username}' and password = '{password}' and tipo_utente = 'FILIALE'"
    n_record = db.read_in_db(mydb,query)
    if n_record == 1:
        return True
    return False

def controllo_privilegi_marketing(user: dict):
    username = user["username"]
    password = user["password"]
    query = f"select * from utenti where username = '{username}' and password = '{password}' and tipo_utente = 'MARKETING'"
    n_record = db.read_in_db(mydb,query)
    if n_record == 1:
        return True
    return False

def prettyJsonVendite(l):
    pretty_list = []
    for elem in l:
        pretty_list.append({"Filiale": elem[0], "Data": elem[1], "Case vendute": elem[2], "Case affitate:": elem[3]})
    return pretty_list

def prettyJsonGuadagni(l):
    pretty_list = []
    for elem in l:
        pretty_list.append({"Filiale": elem[0], "Guadagno vendite": elem[1], "Guadagno affitti": elem[2], "Guadagno totale:": elem[3]})
    return pretty_list 
            
@api.route('/login', methods=['POST'])
def login():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        dati_login = request.json
        username = dati_login["username"]
        password = dati_login["password"]
        query = f"select tipo_utente from utenti where username = '{username}' and password = '{password}'"
        n_record = db.read_in_db(mydb,query)        
        if n_record == 1:
            for elem in mydb:
                return {"tipo": elem}
        elif n_record == 0:
            return '{"Esito":"ko", "messaggio": "Credenziali errate"}'
        elif n_record <= -1:
            print("Dati errati")
            return '{"Esito":"ko", "messaggio": "Dati errati"}'
        else:
            return '{"Esito":"ko", "messaggio": "Errore generico"}'
    return 'Content-Type not supported!'

@api.route('/ricerca_casa_vendita', methods=['POST'])
def ricerca_casa_vendita():
    content_type = request.headers.get('Content_Type')
    if (content_type == 'application/json'):
        data = request.json[0]
        accesso = request.json[1]
        if controllo_privilegi_filiale(accesso):
            try:
                l = []
                query = f"select * from case_in_vendita where stato = 'LIBERO' "
                if data['indirizzo']:
                    indirizzo = data['indirizzo']
                    query += f"and indirizzo = '{indirizzo}' "
                if data['metrimin']:
                    metri = data['metrimin']
                    query += f"and metri > '{metri}' "
                if data['prezzomax']:
                    prezzo = data['prezzomax']
                    query += f"and prezzo >= '{prezzo}'"
                db.read_in_db(mydb,query)
                for elem in mydb:
                    l.append(elem)
                return l
            except:
                return "Errore nella query"

@api.route('/ricerca_casa_affitto', methods=['POST'])
def ricerca_casa_affitto():
    content_type = request.headers.get('Content_Type')
    if (content_type == 'application/json'):
        data = request.json[0]
        accesso = request.json[1]
        if controllo_privilegi_filiale(accesso):
            try:
                l = []
                tipo = data['tipo']
                query = f"select * from case_in_affitto where tipo_affitto = '{tipo}' "
                if data['indirizzo']:
                    indirizzo = data['indirizzo']
                    query += f"and indirizzo = '{indirizzo}' "
                if data['prezzomax']:
                    prezzo = data['prezzomax']
                    query += f"and prezzo_mensile >= '{prezzo}'"
                print(query)
                db.read_in_db(mydb,query)
                for elem in mydb:
                    l.append(elem)
                return l
            except Exception as e:
                print(e)
                return "Errore nella query"
        return "bad credentials"

@api.route('/inserisci_vendita_casa', methods=['POST'])
def vendiCasa():
    content_type = request.headers.get('Content_Type')
    if (content_type == 'application/json'):
        data = request.json[0]
        accesso = request.json[1]
        if controllo_privilegi_filiale(accesso):
            try:
                catastale = data['catastale']
                giorno = data['data']
                proponente = data['proponente']
                venditrice = data['venditrice']
                prezzo = float(data['prezzo'])
                query = f"insert into vendite_casa values ('{catastale}','{giorno}','{proponente}','{venditrice}','{prezzo}')"
                db.write_in_db(mydb, query)
                query = f"update case_in_vendita set stato = 'OCCUPATO' where catastale = '{catastale}'"
                db.write_in_db(mydb,query)
                return "Inserimento avvenuto con successo"
            except Exception as e:
                print(e)
                return "Errore nell'inserimento"
            
@api.route('/inserisci_affitto_casa', methods=['POST'])
def affittaCasa():
    content_type = request.headers.get('Content_Type')
    if (content_type == 'application/json'):
        data = request.json[0]
        accesso = request.json[1]
        if controllo_privilegi_filiale(accesso):
            try:
                catastale = data['catastale']
                giorno = data['data']
                proponente = data['proponente']
                venditrice = data['venditrice']
                prezzo = float(data['prezzo'])
                durata = int(data['durata'])
                query = f"insert into affitti_casa values ('{catastale}','{giorno}','{proponente}','{venditrice}','{prezzo}', '{durata}')"
                db.write_in_db(mydb, query)
                return "Inserimento avvenuto con successo"
            except Exception as e:
                print(e)
                return "Errore nell'inserimento"
            
@api.route('/ottieni_vendite', methods=['POST'])
def ottieniVendite():
    content_type = request.headers.get('Content_Type')
    if (content_type == 'application/json'):
        data = request.json[0]
        accesso = request.json[1]
        if controllo_privilegi_marketing(accesso):
            l = []
            inizio = data['inizio']
            fine = data['fine']
            query = f"""
            SELECT 
            filiale_venditrice AS Filiale,
            TO_CHAR(data_vendita, 'YYYY-MM') AS Mese,
            COUNT(catastale) AS Numero_Case_Vendute,
            0 AS Numero_Case_Affittate
            FROM vendite_casa
            WHERE data_vendita BETWEEN '{inizio}' AND '{fine}'
            GROUP BY filiale_venditrice, TO_CHAR(data_vendita, 'YYYY-MM')

            UNION ALL

            SELECT 
            filiale_venditrice AS Filiale,
            TO_CHAR(data_affitto, 'YYYY-MM') AS Mese,
            0 AS Numero_Case_Vendute,
            COUNT(catastale) AS Numero_Case_Affittate
            FROM affitti_casa
            WHERE data_affitto BETWEEN '{inizio}' AND '{fine}'
            GROUP BY filiale_venditrice, TO_CHAR(data_affitto, 'YYYY-MM');
            """
            db.read_in_db(mydb,query)
            for elem in mydb:
                l.append(elem)
            return prettyJsonVendite(l)
        
@api.route('/ottieni_guadagni', methods=['POST'])
def ottieniGuadagni():
    content_type = request.headers.get('Content_Type')
    if (content_type == 'application/json'):
        data = request.json[0]
        accesso = request.json[1]
        if controllo_privilegi_marketing(accesso):
            l = []
            inizio = data['inizio']
            fine = data['fine']
            query = f"""
            SELECT 
                Filiale,
                SUM(Guadagno_Vendite) AS Guadagno_Vendite,
                SUM(Guadagno_Affitti) AS Guadagno_Affitti,
                SUM(Guadagno_Vendite + Guadagno_Affitti) AS Guadagno_Totale
                FROM (
                SELECT 
                    filiale_venditrice AS Filiale,
                    SUM(
                        CASE 
                            WHEN filiale_proponente = filiale_venditrice THEN prezzo_vendita * 0.03
                            ELSE prezzo_vendita * 0.01
                        END
                    ) AS Guadagno_Vendite,
                    0 AS Guadagno_Affitti
                FROM vendite_casa
                WHERE data_vendita BETWEEN '2024-01-01' AND '2024-12-31'
                GROUP BY filiale_venditrice

                UNION ALL

                SELECT 
                    filiale_venditrice AS Filiale,
                    0 AS Guadagno_Vendite,
                    COUNT(catastale) * 500 AS Guadagno_Affitti
                FROM affitti_casa
                WHERE data_affitto BETWEEN '2024-01-01' AND '2024-12-31'
                GROUP BY filiale_venditrice
                ) AS Risultati
                GROUP BY Filiale;
            """
            db.read_in_db(mydb,query)
            for elem in mydb:
                l.append(elem)
            return prettyJsonGuadagni(l)
        
@api.route('/aggiungi_casa_daVendere', methods=['POST'])
def aggiungiVendere():
    content_type = request.headers.get('Content_Type')
    if (content_type == 'application/json'):
        data = request.json[0]
        accesso = request.json[1]
        if controllo_privilegi_filiale(accesso):
            try:
                catastale = data['catastale']
                indirizzo = data['indirzzo']
                civico = data['civico']
                piano = int(data['piano'])
                metri = int(data['metri'])
                vani = int(data['vani'])
                prezzo = float(data['prezzo'])
                filiale = data['filiale']
                query = f"insert into case_in_vendita values ('{catastale}','{indirizzo}','{civico}','{piano}','{metri}','{vani}','{prezzo}','LIBERO','{filiale}')"
                db.write_in_db(mydb,query)
                return "Inserimento avvenuto con successo"
            except:
                return "Errore nell'inserimento"
            
@api.route('/aggiungi_casa_daAffitare', methods=['POST'])
def aggiungiAffitto():
    content_type = request.headers.get('Content_Type')
    if (content_type == 'application/json'):
        data = request.json[0]
        accesso = request.json[1]
        if controllo_privilegi_filiale(accesso):
            try:
                catastale = data['catastale']
                indirizzo = data['indirzzo']
                civico = data['civico']
                tipo = data['tipo']
                bagno = bool(data['bagno'])
                prezzo = float(data['prezzo'])
                filiale = data['filiale']
                query = f"insert into case_in_affitto values ('{catastale}','{indirizzo}','{civico}','{tipo}','{bagno}','{prezzo}','{filiale}')"
                db.write_in_db(mydb,query)
                return "Inserimento avvenuto con successo"
            except:
                return "Errore nell'inserimento"

api.run(host="127.0.0.1", port=8080)