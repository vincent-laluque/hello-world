
from dessins_tortue import *

up() # relever le crayon
goto(-350, 50)

i = 0

space = 25
while i < 5:
    down()
    carreAngle(space, 'red', 0)
    up()
    forward(space + 10)
    down()
    triangle(space, 'blue', 0)
    up()
    forward(space + 10)
    space += 10
    i += 1
         

a = input() # attendre
