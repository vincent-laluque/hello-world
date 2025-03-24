def compteCar(ca, ch):
    # renvoie le nombre de fois que l'on rencontre le caractère ca dans la chaine de caractères ch
    nbfois = 0
    indice = 0
    while (indice < len(ch)):
        if(ch[indice] == ca):
            nbfois += 1
        indice += 1
    return nbfois

print(compteCar('e', 'Cette phrase est un exemple'))

