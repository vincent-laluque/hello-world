
from dessins_tortue import *
from math import sqrt

up() # relever le crayon
goto(-300,0)

arete = 100

down()
triangle(arete,"red",0)
up()
right(90)
move = arete/(sqrt(3))
forward(move)
down()

triangle(arete,"green",150)  # 180°-30° = 150° 
up()

goto(300,0)
etoile6(100,"red",0)




a = input()
