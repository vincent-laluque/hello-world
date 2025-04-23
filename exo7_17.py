# Définissez une fonction eleMax(liste, debut, fin) qui renvoie l'élément ayant la plus grand valeur dans la liste transmise.
# Les deux arguments debut et fin indiquerons les indices entre lesquels doit s'exercer la recherche, et chacun d'eux pourra être omis.

def eleMax(liste, debut = -1, fin = -1):
    # Comment fait-on déjà pour définir des arguments optionnels ?
    # En fait il suffit de leur donner une valeur par défaut
    if (debut == -1):
        start = 0
    else:
        start = debut
    if (fin == -1):
        stop = len(liste)
    else:
        stop = fin
    indice = 0
    max = 0
    while (indice < len(liste)):
        if ((indice >= start) & (indice <= stop)):
            if (liste[indice] > max):
                max = liste[indice]
        indice += 1
    return max

serie = [9, 3, 6, 1, 7, 5, 4, 8, 2]

print(eleMax(serie))
print(eleMax(serie, 2, 5))
print(eleMax(serie, 2))
print(eleMax(serie, fin = 3, debut = 1))

