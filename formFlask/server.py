from flask import Flask, render_template, request

api = Flask("__name__")
utenti = [["mario", "password1", "m", "0"], ["gianni", "password2", "m", "0"]]


@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@api.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@api.route('/visualizza', methods=['GET'])
def visualizza():
    nome = request.args.get('nome')
    password = request.args.get('password')
    for i in range(len(utenti)):
        if utenti[i][0] == nome and utenti[i][1] == password:
            return render_template('visualizza.html', nome=utenti[i][0], sesso=utenti[i][2], numero=utenti[i][3])    
    return render_template('errore.html')

@api.route('/registra', methods=['GET'])
def registra():
    return render_template('registra.html')

@api.route('/registrazione', methods=['GET'])
def registrazione():
    nome = request.args.get('nome')
    password = request.args.get('password')
    sesso = request.args.get('sesso')
    utenti.append([nome,password,sesso,0])
    return render_template("index.html")

api.run(host="0.0.0.0", port=8085)