def get_fichier(nom_fichier):
    with open(nom_fichier, 'r') as f:
        return f.read()

def has_symbol_nearby(fichier, num_ligne, num_carac):
    if num_ligne != 0:
        if num_carac != 0 and fichier[num_ligne-1][num_carac-1] in symbols:
            return True
        if fichier[num_ligne-1][num_carac] in symbols:
            return True
        if num_carac != len(fichier[num_ligne])-1 and fichier[num_ligne-1][num_carac+1] in symbols:
            return True
    if num_carac != 0 and fichier[num_ligne][num_carac-1] in symbols:
        return True
    if num_carac != len(fichier[num_ligne])-1 and fichier[num_ligne][num_carac+1] in symbols:
        return True
    if num_ligne != len(fichier)-1:
        if num_carac != 0 and fichier[num_ligne+1][num_carac-1] in symbols:
            return True
        if fichier[num_ligne+1][num_carac] in symbols:
            return True
        if num_carac != len(fichier[num_ligne])-1 and fichier[num_ligne+1][num_carac+1] in symbols:
            return True
    return False

def somme_des_parties(nom_fichier):
    fichier = get_fichier(nom_fichier).split("\n")
    fichier.pop()
    """fichier = ["467..114..",
               "...*......",
               "..35..633.",
               "......#...",
               "617*......",
               ".....+.58.",
               "..592.....",
               "......755.",
               "...$.*....",
               ".664.598.."]"""
    somme = 0
    oks = []
    current_number = ""
    current_number_valid = False
    for num_ligne in range(len(fichier)):
        for num_carac in range(len(fichier[num_ligne])):
            if fichier[num_ligne][num_carac].isdigit():
                current_number += fichier[num_ligne][num_carac]
                if not current_number_valid and has_symbol_nearby(fichier, num_ligne, num_carac):
                    current_number_valid = True
            else:
                if current_number_valid:
                    somme += int(current_number)
                    oks.append(current_number)
                current_number = ""
                current_number_valid = False
    return somme

def gear_ratio(fichier, num_ligne, num_carac):
    pass

def is_a_gear(fichier, num_ligne, num_carac):
    if fichier[num_ligne][num_carac] == "*":
        nb_numbers_around = 0
        if num_ligne != 0:
            if num_carac != 0 and fichier[num_ligne-1][num_carac-1].isdigit():
                nb_numbers_around += 1
            if fichier[num_ligne-1][num_carac].isdigit():
                nb_numbers_around += 1
            if num_carac != len(fichier[num_ligne])-1 and fichier[num_ligne-1][num_carac+1].isdigit():
                nb_numbers_around += 1
        if num_carac != 0 and fichier[num_ligne][num_carac-1].isdigit():
            nb_numbers_around += 1
        if num_carac != len(fichier[num_ligne])-1 and fichier[num_ligne][num_carac+1].isdigit():
            nb_numbers_around += 1
        if num_ligne != len(fichier)-1:
            if num_carac != 0 and fichier[num_ligne+1][num_carac-1].isdigit():
                nb_numbers_around += 1
            if fichier[num_ligne+1][num_carac].isdigit():
                nb_numbers_around += 1
            if num_carac != len(fichier[num_ligne])-1 and fichier[num_ligne+1][num_carac+1].isdigit():
                nb_numbers_around += 1
    return False

def somme_des_gears(nom_fichier):
    pass

def all_caracs(nom_fichier):
    fichier = get_fichier(nom_fichier)
    caracs = set()
    for ligne in fichier:
        for carac in ligne:
            caracs.add(carac)
    return caracs

symbols = ["@", "-", "*", "$", "/", "&", "+", "%", "=", "#"]
print(somme_des_parties("jour3/input"))
#517021