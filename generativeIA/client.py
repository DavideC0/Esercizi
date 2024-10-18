import requests,json
import subprocess
import sys
from myjson import *

def ComponiJsonPerImmagine(sImagePath):
  subprocess.run(["rm", "./image.jpg"])
  subprocess.run(["rm", "./request.json"])
  subprocess.run(["cp", sImagePath,"./image.jpg"])
  subprocess.run(["bash", "./creajson.sh"])

base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key="
api_key = "AIzaSyAqt_mbEIRbhv2DUdashytfpqymXUCC0mw"
api_url = base_url + api_key
auth = False

while(True):
    print("Operazioni disponibili:")
    print("1. Inserisci una domanda")
    print("2. Richiedi domanda su un'immagine")
    print("3. Esci)")
    sOper = input("Cosa vuoi fare? ")
    if sOper == "1":
        sDomanda = input("Inserisci la domanda ")
        jsonDataRequest = jsonDataRequest = {"contents": [{"parts":[{"text": sDomanda}]}]}
        response = requests.post(api_url,json=jsonDataRequest, verify=True)
        if response.status_code == 200:
            listaRisposte = response.json()["candidates"]
            for risposta in listaRisposte:
                testo = risposta["content"]["parts"][0]["text"]
            print(testo)
    
    elif sOper == "2":
        sImg = input("Inserisci il file img da analizzare: ")
        sDomanda = input("Inserisci la domanda ")
        ComponiJsonPerImmagine(sImg)
        jsonDataRequest = JsonDeserialize("request.json")
        response = requests.post(api_url,json=jsonDataRequest, verify=True)
        if response.status_code == 200:
            listaRisposte = response.json()["candidates"]
            for risposta in listaRisposte:
                testo = risposta["content"]["parts"][0]["text"]
            print(testo)
    elif sOper=="3":
        print("Buona giornata!")
        sys.exit()
    else:
        print("Operazione non valida")