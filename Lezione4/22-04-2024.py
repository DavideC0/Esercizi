def counter(s: str) ->list[int]:
    lista: list = []
    lista.append(len(s))
    parole: str = s.split()
    lista.append(len(parole))
    parole_distinte: set = set(s.split()) 
    lista.append(len(parole_distinte))
    numero_frasi = len(str(lista.count('.'))) + len(str(lista.count('!'))) + len(str(lista.count('?')))
    lista.append(numero_frasi)
    return lista

def conta_occorrenze_parole(s: str) -> dict:
    s = s.replace('.','').replace('','').replace(';','').replace(':','').replace('?','').replace('!','')
    parole = stringa.split()
    occorrenze = {}
    for parola in parole:
        if parola in occorrenze:
            occorrenze[parola] += 1
        else:
            occorrenze[parola] = 1
    return occorrenze

def filtro_occorrenze(d: dict):
    filtrato: dict = {}
    for parola in d:
        if d[parola] > 1:
            filtrato[parola] = d[parola]
    return filtrato

def is_palindrome(parola):
    parola = parola.lower()
    parola = parola.replace(" ", "")
    lunghezza = len(parola)
    
    for i in range(lunghezza // 2):
        if parola[i] != parola[lunghezza - i - 1]:
            return False
    return True

s: str = "La meccanica quantistica è la teoria fisica che descrive il comportamento della materia, della radiazione e le reciproche interazioni, con particolare riguardo ai fenomeni caratteristici della scala di lunghezza o di energia atomica e subatomica, dove le precedenti teorie classiche risultano inadeguate. Come caratteristica fondamentale, la meccanica quantistica descrive la radiazione e la materia sia come fenomeni ondulatori che come entità particellari, al contrario della meccanica classica, che descrive la luce solamente come un'onda e, ad esempio, l'elettrone solo come una particella. Questa inaspettata e controintuitiva proprietà della realtà fisica, chiamata dualismo onda-particella, è la principale ragione del fallimento delle teorie sviluppate fino al XIX secolo nella descrizione degli atomi e delle molecole. La relazione tra natura ondulatoria e corpuscolare è enunciata nel principio di complementarità e formalizzata nel principio di indeterminazione di Heisenberg. Esistono numerosi formalismi matematici equivalenti della teoria, come la meccanica ondulatoria e la meccanica delle matrici; al contrario, ne esistono numerose e discordanti interpretazioni riguardo all'essenza ultima del cosmo e della natura, che hanno dato vita a un dibattito tuttora aperto nell'ambito della filosofia della scienza. La meccanica quantistica rappresenta, assieme alla teoria della relatività, uno spartiacque rispetto alla fisica classica, portando alla nascita della fisica moderna. Attraverso la teoria quantistica dei campi, generalizzazione della formulazione originale che include il principio di relatività ristretta, essa è a fondamento di molte altre branche della fisica, come la fisica atomica, la fisica della materia condensata, la fisica nucleare, la fisica delle particelle, la chimica quantistica."
x: str = "Ciao! come, stai? Ciao! come stai"
print(counter(x))

stringa = "Ciao, Ciao come stai? tutto bene bene ciao ciao ciao stai stai stai stai"
occorrenze_parole = conta_occorrenze_parole(stringa)
print(occorrenze_parole)
dizionario_filtrato: dict = filtro_occorrenze(occorrenze_parole)
print(dizionario_filtrato)

parola = "anna"
if is_palindrome(parola):
    print(f"{parola} è un palindromo")
else:
    print(f"{parola} non è un palindromo")