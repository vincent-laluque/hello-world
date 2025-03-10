from turtle import *
from dessins_tortue import *

up()
goto(-300,0)

move = 80

right(120)
k = 0
while (k < 5):
    k += 1
    etoile6(move,"blue",0)
    forward(move+10)
    down()
    carre(move,"blue")
    up()
    forward(move+10)
forward(move)

a = input()
