import json

numero_domande_tot: int = 0
media_risposte_possibili: float = 0
numero_domande_matematica: int = 0

with open("quiz.json") as json_file:
    file = json.load(json_file)

for key, value in file["quiz"].items():
    for key1, value1 in value.items():
        numero_domande_tot += 1
        for key2, value2 in value1.items():
            if key2 == "options":
                media_risposte_possibili += len(value1[key2])
    if key == "maths":
        for key1, value1 in value.items():
            numero_domande_matematica += 1

media_risposte_possibili = media_risposte_possibili / numero_domande_tot

print(f"Il numero di domande totali è: {numero_domande_tot}")
print(f"La media delle risposte possibili è: {media_risposte_possibili}")
print(f"Il numero delle domande di matematica è: {numero_domande_matematica}")