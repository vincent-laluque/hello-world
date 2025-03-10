from turtle import *
from dessins_tortue import *

up()
goto(-300,0)

move = 80

right(120)
k = 0
while (k < 5):
    if (k < 3):
        pas = (k % 3) + 1
    else:
        pas = 2 - (k % 3)
    # write(pas)
    move = 40 + (pas*20)
    k += 1
    etoile6(move,"red",0)
    forward(move+10)
    down()
    carre(move,"blue")
    up()
    forward(move+10)
forward(move)

a = input()
