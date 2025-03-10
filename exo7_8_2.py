from dessins_tortue import *
from turtle import *

up()
goto(0,-200)

largeur = 40

k = 0

while (k < 9):

    down()
    etoile5(largeur,"red",180)
    up()
    forward(largeur+10)
    down()
    triangle(largeur,"blue",0)
    up()
    forward(largeur+10)
    down()
    etoile6(largeur,"green",0)
    up()
    forward(largeur+10)
    down()
    carreAngle(largeur,"grey",0)
    up()
    forward(largeur+10)

    largeur = largeur + 10
    k += 1

a=input()

