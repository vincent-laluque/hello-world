# Définissez une fonction changeCar(ch, ca1, ca2, debut, fin) qui remplace tous les caractères ca1 par des caractères ca2
# dans la chaîne de caractères ch, à partir de l'indice debut et jusqu'à l'indice fin
# ces deux derniers arguments pouvant être omis (et dans ce cas la chaîne est traitée d'une extrémité à l'autre)

def changeCar(ch, ca1, ca2, debut = -1, fin = -1):
    # Un si grand classique...

    if (debut == -1):
        debut = 0
    if (fin == -1):
        fin = len(ch)

    result = ""
    indice = 0
    
    while (indice < len(ch)):
        if (indice >= debut) & (indice < fin):
            if (ch[indice] == ca1):
                result += ca2
            else:
                result += ch[indice]
        else:
            result += ch[indice]
        indice += 1

    return result

phrase = 'Ceci est une toute petite phrase.'
print(changeCar(phrase,' ','*'))
print(changeCar(phrase, ' ', '*', 8, 12))
print(changeCar(phrase, ' ', '*', 12))
print(changeCar(phrase, ' ', '*', fin=12))
