from turtle import *

def triangle(x,y,aColor):
    goto(x,y)
    k = 0
    color(aColor)
    width(5)
    down()
    while(k < 3):
        k += 1
        forward(100)
        left(120)
    write(aColor)
    up()

triangle(0,0,'red')
triangle(50,50,'blue')
triangle(-20,-20,'green')
