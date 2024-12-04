from flask import Flask, render_template, request
import os

api = Flask(__name__)

@api.route("/", methods=['GET'])
def index():
    return render_template("send.html")

@api.route('/mansendfile', methods=['POST'])
def ricevidati():
    domanda = request.form.get('question')
    image = request.files.get("image")
    lunghezza = len(image)
    
    answer = domanda + " file immagine " + str(lunghezza)
    return render_template("send.html", answer=answer)
    

api.run(host="0.0.0.0", port=8085)