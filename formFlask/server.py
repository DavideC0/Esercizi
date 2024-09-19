from flask import Flask, render_template, request

api = Flask("__name__")
utenti = [["mario", "password1", "m", "0"], ["gianni", "password2", "m", "0"]]


@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@api.route('/visualizza', methods=['GET'])
def visualizza():
    nome = request.args.get('nome')
    cognome = request.args.get('cognome')
    return render_template('visualizza.html', nome=nome, cognome=cognome)

api.run(host="0.0.0.0", port=8085)