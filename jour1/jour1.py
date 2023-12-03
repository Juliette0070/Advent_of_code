def get_fichier(nom_fichier):
    with open(nom_fichier, 'r') as f:
        return f.read()

def get_nombre(ligne):
    nb1 = ""
    nb2 = ""
    for i in range(len(ligne)):
        if ligne[i].isdigit() and nb1 == "":
            nb1 = ligne[i]
        if ligne[-(i+1)].isdigit() and nb2 == "":
            nb2 = ligne[-(i+1)]
    if nb1 == "":
        nb1 = "0"
        nb2 = "0"
    return int(nb1+nb2)

def is_a_number(chaine):
    match chaine:
        case "zero":
            return "0"
        case "one":
            return "1"
        case "two":
            return "2"
        case "three":
            return "3"
        case "four":
            return "4"
        case "five":
            return "5"
        case "six":
            return "6"
        case "seven":
            return "7"
        case "eight":
            return "8"
        case "nine":
            return "9"
        case _:
            return chaine


def separe_nombre(ligne):
    nombres = []
    current = ""
    for i in range(len(ligne)):
        if ligne[i].isdigit():
            nombres.append(ligne[i])
        elif current + ligne[i]:
            pass

def get_nombre2(ligne):
    nb1 = ""
    nb2 = ""
    for i in range(len(ligne)):
        pass
    if nb1 == "":
        nb1 = "0"
        nb2 = "0"
    return int(nb1+nb2)

def somme_chiffres(nom_fichier):
    somme = 0
    fichier = get_fichier(nom_fichier)
    for ligne in fichier.split('\n'):
        somme += get_nombre(ligne)
    return somme

print(somme_chiffres('input'))