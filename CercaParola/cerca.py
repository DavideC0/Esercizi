import os
import PyPDF2

def cercaParolaInNomefile(file, sParola):
    sFileLower = file.lower()
    sParolaLower = sParola.lower()
    if (sFileLower.find(sParolaLower) >= 0):
        return True
    else:
        return False

def cercaProlaInFileTxt(path, sParola):
    with open(path, "r") as file:
        line = file.readline()
        while len(line) > 0:
            iRet = line.lower().find(sParola.lower())
            if iRet >= 0:
                return True
            line = file.readline()
            print(f"Riga letta {line}")
    return False

def cercaProlaInFilePdf(path, sParola):
    iret = 0
    object = PyPDF2.PdfReader(path)
    numPages = len(object.pages)
    print(f"Il file {path} contiene {numPages} pagine")
    for i in range(0, numPages):
        pageObj = object.pages[i]
        text = pageObj.extract_text()
        iret = text.lower().find(sParola.lower())
        if iret >= 0:
            return True
        return False
    
def cercaParolaInContenutoFile(path, sParola):
    bret = False
    fileName, fileExt = os.path.splitext(path)
    if fileExt.lower() == ".txt":
        bret = cercaProlaInFileTxt(path, sParola)
    elif fileExt.lower() == ".pdf":
        bret = cercaProlaInFilePdf(path, sParola)
    return bret
        
        

sRoot = input("Inserisci la directory dover cercare: ")
sParola = input("Inserisci la parola da cercare ")
sOutDir = input("Inserisci la directory dove salvare i risultati ")

bret = False
for root, listDir, files in os.walk(sRoot):
    print(f"Nella directory {root} ci sono {len(listDir)} sottodirectory e {len(files)} file")
    for file in files:
        bret = cercaParolaInNomefile(file, sParola)
        if bret:
            print(f"Trovata parola in file {file}")
        else:
            sFilePathCompleto = os.path.join(root, file)
            bret = cercaParolaInContenutoFile(sFilePathCompleto, sParola)
            if bret:
                print(f"Parola trovata in {file}")
            else:
                print(f"Parola non trovata in {file}")