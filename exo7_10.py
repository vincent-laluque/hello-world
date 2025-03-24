
def indexMax(liste):
    # renvoie l'index de l'élément ayant la valeur la plus élevée dans la liste
    max = liste[0]
    iMax = 0
    i = 0
    while (i < len(liste)):
        if (liste[i] > max):
            max = liste[i]
            iMax = i
        i += 1
    return iMax

serie = [5, 8, 2, 1, 9, 3, 6, 7]
print(indexMax(serie))
