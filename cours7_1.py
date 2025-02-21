from dessins_tortue import *

up()  #relever le crayon
goto(-150, 50) # reculer en haut à gauche

# dessiner 10 carrés rouges, alignés:
i = 0
while i < 10:
    down() # abaisser le crayon
    carre(25, 'red') # tracer un carré
    up() # relever le crayon
    forward(30) # avancer
    i += 1
a = input() # attendre