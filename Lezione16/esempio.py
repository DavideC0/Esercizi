reader = open("esempio.txt")

try:
    print(reader.readline())
    print(f"Sono nella try")
    raise Exception(f"Eccezione")

except Exception:
    print(f"Sono nella exept")
    
finally:
    print(reader)
    reader.close()
    print(f"Sono nella finaly")