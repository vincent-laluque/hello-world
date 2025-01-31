from math import sqrt

print("Entrez un nombre donc vous souhaitez connaître la racine:")
nombre = float(input())

if (nombre >= 0):
    print("La racine carrée de",nombre,"est:",sqrt(nombre))
else:
    print("On ne peut pas donner la racine carrée d'un nombre négatif")
