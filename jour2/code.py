def get_fichier(nom_fichier):
    with open(nom_fichier, 'r') as f:
        return f.read()

def transforme_liste(chaine):
    liste = []
    for element in chaine.split(';'):
        liste_t = []
        dico_t = {}
        for sous_element in element.split(','):
            sous_sous_element = sous_element.split(' ')
            if len(sous_sous_element) == 3:
                dico_t[sous_sous_element[2]] = int(sous_sous_element[1])
            liste_t.append(sous_element)
        liste.append(dico_t)
    return liste

def make_dico(nom_fichier):
    fichier = get_fichier(nom_fichier)
    dico = {}
    for ligne in fichier.split('\n'):
        if ligne:
            cle, valeur = ligne.split(':')
            valeur = transforme_liste(valeur)
            dico[cle] = valeur
    return dico

def is_a_valid_game(game):
    for dico in game:
        if not (dico.get("red",0) <= 12 and dico.get("green",0) <= 13 and dico.get("blue",0) <= 14):
            return False
    return True

def num_game(game):
    return int(game.split(' ')[1])

def somme_parties_possibles(nom_fichier):
    dico = make_dico(nom_fichier)
    somme = 0
    for game, values in dico.items():
        if is_a_valid_game(values):
            somme += num_game(game)
    return somme

def power(liste):
    max_red = 0
    max_green = 0
    max_blue = 0
    for dico in liste:
        if dico.get("red",0) > max_red:
            max_red = dico.get("red",0)
        if dico.get("green",0) > max_green:
            max_green = dico.get("green",0)
        if dico.get("blue",0) > max_blue:
            max_blue = dico.get("blue",0)
    return max_red * max_green * max_blue

def somme_power(nom_fichier):
    dico = make_dico(nom_fichier)
    somme = 0
    for _, values in dico.items():
        somme += power(values)
    return somme

#condition : 12red, 13green, 14blue 
print(somme_parties_possibles('jour2/input'))
print(somme_power('jour2/input'))