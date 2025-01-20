# écrire un programme qui permet d'encoder des valeurs dans une liste


uneListe = []
n = 0
stop = False

while (stop == False):
    aValue = input("Veuillez entrer une valeur: ")
    if (aValue != ""):
        uneListe.append(int(aValue))
        n += 1
    else:
        stop = True

print(uneListe)

