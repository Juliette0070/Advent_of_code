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

def get_number(chaine):
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

def is_a_number(chaine):
    if chaine in ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]:
        return True
    return False

def looks_like_a_number(chaine):
    nbs = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for nb in nbs:
        if nb.startswith(chaine):
            return True
    return False

def separate_numbers(ligne):
    nombres = []
    currents = []
    for i in range(len(ligne)):
        deleted = []
        if ligne[i].isdigit():
            currents.clear()
            nombres.append(ligne[i])
        else:
            for j in range(len(currents)):
                if is_a_number(currents[j] + ligne[i]):
                    deleted.append(j)
                    nombres.append(get_number(currents[j] + ligne[i]))
                elif looks_like_a_number(currents[j] + ligne[i]):
                    currents[j] += ligne[i]
                elif not looks_like_a_number(currents[j] + ligne[i]):
                    deleted.append(j)
        if looks_like_a_number(ligne[i]):
            currents.append(ligne[i])
        deleted.sort(reverse=True)
        for ind in deleted:
            currents.pop(ind)
    return nombres

def get_nombre2(ligne):
    nb1 = ""
    nb2 = ""
    nombres = separate_numbers(ligne)
    if len(nombres) > 0:
        nb1 = nombres[0]
        nb2 = nombres[-1]
    if nb1 == "":
        nb1 = "0"
        nb2 = "0"
    return int(nb1+nb2)

def somme_chiffres(nom_fichier):
    somme = 0
    fichier = get_fichier(nom_fichier)
    for ligne in fichier.split('\n'):
        nb = get_nombre2(ligne)
        print(nb, ligne)
        somme += nb
    return somme

print(somme_chiffres('jour1/input'))
