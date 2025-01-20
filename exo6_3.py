from math import *

lalongeur = input("Donne moi la longeur de mon pendule :")
longueur = float(lalongeur)

# La valeur de la constante de gravitation est de 9,81 m/s²
g = 9.81 

# Calcul de la période de mon pendule:
T = 2*pi*sqrt(longueur/g)

print("La période de mon pendule est donc de :",T, " secondes")