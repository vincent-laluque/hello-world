
from dessins_tortue import *

# etoile5(400, 'red', 0)

up() # relever le crayon
goto(-300, 0)

c = 0
while c < 9:
    if c < 5:
        pas = (c % 5) + 1
    else:
        pas = 4 - (c % 5)
    color('green')
    write(pas)
    dimension = 25 + ((pas)*10)
    down()
    etoile5(dimension, 'orange', 0)
    up()
    forward(dimension + 10)
    c += 1

a = input()
