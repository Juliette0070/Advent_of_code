def get_fichier(nom_fichier):
    with open(nom_fichier, 'r') as f:
        return f.read()
