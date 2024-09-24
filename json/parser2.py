import json

def serialize(dictionary, file_path):
    try:
        with open(file_path, "w") as json_file:
            json.dump(dictionary, json_file, indent=4, separators=(',',': '))
        return True
    except:
        return False
    
def serialize2(dictionary, file_path):
    try:
        sData = json.dumps(dictionary)
        with open(file_path, "w") as json_file:
            json_file.write(sData)
        return True
    except:
        return False
    
def deserialize(file_path):
    try:
        with open(file_path, "r") as json_file:
            return json.load(json_file)
    except Exception as e:
        return e

dizionario = { "brand": "Ford",
"electric": False,
"year": 1964,
"colors": ["red", "white", "blue"]}

print(serialize(dizionario,"users.json"))
print(deserialize("users.json"))