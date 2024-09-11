import base64

riga = input("inserire una stringa: ")
print(f"Riga letta: {riga}")

riga_64 = base64.b64encode(riga.encode("utf-8"))
print("Riga codificata: ", riga_64.decode("utf-8"))

riga_decoded = base64.b64decode(riga_64)
print("Riga decodificata: ", {riga_decoded.decode("utf-8")})