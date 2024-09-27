import requests,json

base_url = "http://127.0.0.1:8080"

def GetDatiCittadino():
    nome = "Mario"
    cognome = "Garibaldi"
    dataN = "07/11/1890"
    codF = "dcfv501u"
    datiCittadino = {codF:{"nome":nome, "cognome": cognome, "dataNascita":dataN}}
    return datiCittadino


api_url = base_url + "/add_cittadino"
jsonDataRequest = GetDatiCittadino()
response = requests.post(api_url,json=jsonDataRequest)
