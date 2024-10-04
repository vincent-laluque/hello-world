rad = 0.5625244660546206

pi = 3.14159265359

# valeur d'un radian en degrés:
radian = 180/pi

# voici donc le nombre qu'il me faut exprimer en base (1/60):
number = rad*radian
print(number)

# à charge pour moi de trouver les nombres degres, minutes et secondes tels que:
# number = degres + minutes*(1/60) +secondes*(1/3600)
# number*3600 = degres*(60*60) + minutes*(60) +secondes

# et donc ici voilà le nombre qu'il me faut exprimer en base 60:
number = number*3600
print(number)

degres = number//3600
print(degres)

reste = number-(degres*3600)

minutes = reste//60
print(minutes)

secondes = reste - (minutes*60)

#Affichage
print(rad, "radian(s) = ",degres, "°", minutes, "'", secondes,'"')
