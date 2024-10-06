from flask import Flask, json, request, render_template
import random

api = Flask(__name__)

@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        if login_interno(request.login):
            with open("user.json") as json_file:
                cittadini = json.load(json_file)
            for key, vale in request.json.items():
                if key in cittadini:
                    print("Errore codice fiscale già esistente")
                    return "True"
            with open("user.json", "w") as json_file:
                cittadini |= request.json
                json.dump(cittadini, json_file)
            return "True"
        else:
            return "Dati errati"
    else:
        return 'Content-Type not supported!'
    
@api.route('/read_cittadino', methods=['POST'])
def GestisciReadCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        if login_interno(request.login):
            with open("user.json") as json_file:
                cittadini = json.load(json_file)
            for key, value in cittadini.items():
                if request.json == key:
                    return cittadini[key]
            return "Cittadino non trovato"
        else:
            return "Dati errati"
    else:
        return 'Content-Type not supported!'
    
@api.route('/update_cittadino', methods=['POST'])
def GestisciUpdateCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        if login_interno(request.login):
            with open("user.json") as json_file:
                cittadini = json.load(json_file)
        
            if request.json[0] not in cittadini:
                return "Errore, codice fiscale non trovato"

            for i in range(len(request.json) - 1):
                if request.json[i+1]:
                    if i + 1 == 1:
                        cittadini[request.json[0]]["cognome"] = request.json[i+1]
                    elif i + 1 == 2:
                        cittadini[request.json[0]]["dataNascita"] = request.json[i+1]
                    elif i + 1 == 3:
                        cittadini[request.json[0]]["nome"] = request.json[i+1]
            with open("user.json", "w") as json_file:
                json.dump(cittadini, json_file)
            return "Modifica avvenuta con successo"   
        else:
            return "Dati errati"     
    else:
        return 'Content-Type not supported!'

@api.route('/delete_cittadino', methods=['POST'])
def GestisciDeleteCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        if login_interno(request.login):
            with open("user.json") as json_file:
                cittadini = json.load(json_file)
        
            if request.json not in cittadini:
                return "Errore, codice fiscale non trovato"
            cittadini.pop(request.json)
            with open("user.json", "w") as json_file:
                json.dump(cittadini, json_file)
                
            return "Eliminazione avvenuta con successo"
        else:
            return "Dati errati"
    else:
        return 'Content-Type not supported!'
    
@api.route('/login', methods=['POST'])
def login():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        with open('login.json') as json_file:
            user = json.load(json_file)
        
        for key, value in request.json.items():
            if key in user:
                if user[key] == value:
                    return "True"
        return "Nome utente o password non trovati"
    else:
        return 'Content-Type not supported!'

@api.route('/registrazione', methods=['POST'])
def Registrazione():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        with open('login.json') as json_file:
            user = json.load(json_file)        
        for key, value in request.json.items():
            if key not in user:
                request.json[key].append(random.randint(0,1))
                user |= request.json
                with open('login.json', 'w') as json_file:
                    json.dump(user, json_file)
            else:
                return "Nome utente già in uso"
        return "Registrazione avvenuta con successo"
    else:
        return 'Content-Type not supported!'
    
def login_interno(user: dict):
    with open('login.json') as json_file:
        users = json.load(json_file)
    for key, value in user.items():
        if key in users:
            if users[key] == value:
                return True
    return False

api.run(host="127.0.0.1", port=8080, ssl_context='adhoc')
