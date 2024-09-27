from flask import Flask, json, request, render_template

api = Flask(__name__)

#mettere una lista di liste dove ogni lista è un cittadino

#la chiave è il codice fiscale
#add cittadino
#read cittadino
#update cittadino
#delete cittadino


@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
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
        return 'Content-Type not supported!'
    
@api.route('/read_cittadino', methods=['POST'])
def GestisciReadCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        with open("user.json") as json_file:
            cittadini = json.load(json_file)
        for key, value in cittadini.items():
            if request.json == key:
                return cittadini[key]
        return "Cittadino non trovato"
    else:
        return 'Content-Type not supported!'


api.run(host="127.0.0.1", port=8080)
