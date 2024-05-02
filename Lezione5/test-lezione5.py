import math

def find_element(lst: list[int], element: int) -> bool:
    for item in lst:
        if item == element:
            return True
        return False
    

lista = [1,2,3,4,5]
elemento = 7

print(find_element(lista,elemento))

def check_parentheses(stringa):
    stack = []
    parentesi_aperte = ['(', '[', '{']
    parentesi_chiuse = [')', ']', '}']
    for carattere in stringa:
        if carattere in parentesi_aperte:
            stack.append(carattere)
        elif carattere in parentesi_chiuse:
            if not stack:
                return False
            parentesi_aperta_corrispondente = stack.pop()
            if parentesi_aperte.index(parentesi_aperta_corrispondente) != parentesi_chiuse.index(carattere):
                return False
    return len(stack) == 0

print(check_parentheses("()()"))

print(check_parentheses("(()))("))

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    if len(dict2) >=  len(dict1):
        for key in dict2:
            if key in dict1:
                dict2[key] = dict2[key] + dict1[key]
            else:
                pass
            Cdict: dict = dict2.copy()
    else:
        for key in dict1:
            if key in dict2:
                dict1[key] = dict1[key] + dict2[key]
            else:
                pass
            Cdict: dict = dict1.copy()

    key_dict1 = dict1.keys()
    value_dict1 = dict1.values()
    key_dict2 = dict2.keys()
    value_dict2 = dict2.values()
    return Cdict

def unisci_dizionari(dizionario1, dizionario2):
    dizionario_unione = dizionario1.copy()
    for chiave, valore in dizionario2.items():
        if chiave in dizionario_unione:
            dizionario_unione[chiave] += valore
        else:
            dizionario_unione[chiave] = valore
    return dizionario_unione

