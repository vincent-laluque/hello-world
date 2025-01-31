from math import *
# Convertir une note scolaire N quelconque 
note, plafond = eval(input("Entrer une note sur quelque chose, séparez les deux chiffres par une virgule:"))
print(note,"sur",plafond)

percentage = (note/plafond)*100

if (percentage >= 80):
    appreciation = "A"
elif (percentage < 80) and (percentage >= 60):
    appreciation = "B"
elif (percentage < 60) and (percentage >= 50):
    appreciation = "C"
elif (percentage < 50) and (percentage >= 40):
    appreciation = "D"
else:
    appreciation = "E"

print("Avec un pourcentage de",int(percentage),"%, votre appréciation est de:",appreciation)