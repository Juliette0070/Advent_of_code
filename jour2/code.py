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
                dico_t[sous_sous_element[2]] = sous_sous_element[1]
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

print(make_dico('jour2/input'))