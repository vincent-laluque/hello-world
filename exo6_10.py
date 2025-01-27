# Entrer le nom et le sexe de l'utilisateur
print("Entrer le nom et le sexe de l'utilisateur (M/F) séparés par une virgule: ")
# NB: il faut rentrer "Cunégonde","F" pour que ça marche...

ch = input()
elements = list(eval(ch))

# la fonction intégrée len() renvoie le nombre d'éléments présents dans la liste
if (len(elements) == 2):
    name = elements[0]
    sexe = elements[1]

    if (sexe == 'F'):
        print("Chère Mademoiselle",name)
    else:
        print("Cher Monsieur",name)
else:
    print("Incorrect number of elements")
