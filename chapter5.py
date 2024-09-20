
pi = 3.14159

deg = 32
min = 13
sec = 49

# Conversion des secondes en une fraction de minute:
fm = sec/60

# Conversion des minutes en une fraction de degré:
fd = (min + fm)/60

# Valeur de l'angle en degrés "décimalisés"
ang = deg + fd

pi = 3.14159265359

# valeur d'un radian en degrés:

rad = 180/pi

#Conversion de l'angle en radians:
arad = ang/rad

#Affichage
print(deg, "°", min, "'", sec,'" =', arad, "radian(s)")



