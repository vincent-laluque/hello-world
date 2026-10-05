# Dessin d'un damier avec placement de pions au hasard
from tkinter import *
from random import randrange # générateur de nombres aléatoires

def damier():
	"dessiner dix lignes de carrés avec décalage alterné"
	y = 0
	while y <10:
		if y % 2 == 0:
			x = 0
		else:
			x = 1
		ligne_de_carres(x*c, y*c)
		y += 1

def ligne_de_carres(x, y):
	"dessiner une ligne de carrés en partant de x, y"
	i = 0
	while i < 5:
		can.create_rectangle(x, y, x+c, y+c, fill='navy')
		i += 1
		x += c*2

def cercle(x, y, r, coul):
	"dessiner un cercle de centre x,y et de rayon r"
	can.create_oval(x-r, y-r, x+r, y+r, fill=coul)

def ajouter_pion():
	"dessiner un pion au hasard sur le damier"
	# tirer au hasard les coordonnées d'un pion:
	x = c/2 + randrange(10) * c
	y = c/2 + randrange(10) * c
	cercle(x, y, c/3, 'red')

c = 30

fen = Tk()
can = Canvas(fen, width =c*10, height =c*10, bg='ivory')
can.pack(side=TOP, padx =5, pady =5)
b1 = Button(fen, text='damier', command = damier)
b1.pack(side=LEFT, padx = 3, pady = 3)
b2 = Button(fen, text ='pions', command=ajouter_pion)
b2.pack(side=RIGHT, padx =3, pady =3)
fen.mainloop()
