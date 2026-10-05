

from tkinter import *
# {Claude} L'avertissement de l'éditeur est du à:
# Pollution de l'espace de noms: import * déverse des dizaines de noms dans ton fichier (Button, Label,...)
# et tu ne sais plus d'où vient quoi
# Collisions silencieuses:si tu importes deux bibliothèques avec * et qu'elles définissent un même nom,
# la seconde écrase la première sans prévenir
# Lisibilité et analyse statique: l'éditeur ne peut plus vérifier si un nom existe vraiment
# Bonne pratique:
# import tkinter as tk
# root = tk.Tk()

from random import randrange

# Création du widget (= "Window gadget") ou (= "Composant graphique") ou ("Contrôle") principal

fenetre = Tk()

# Widget: ce terme désigne toute entité susceptible d'être placée dans une fenêtre d'application
# comme par exemple un bouton, une case à cocher, une image, etc., et parfois aussi la fenêtre elle-même.

# Création des widgets "esclaves":
zone = Canvas(fenetre, bg='ivory', height=600, width=600)
zone.pack()


def drawSquare(x, y, l, coul):
	"dessin d'un carré dont le coin en haut à gauche a pour coordonnées x et y"
	zone.create_rectangle(x, y, x+l, y+l, fill = coul)


def drawDamier():
	"Dessin d'un damier"

	squareLength = globLongueur
	xPointDebut= 0
	yPointDebut = 0

	rang = 0
	while (rang < 10):
		xPointDebut = squareLength
		yPointDebut = yPointDebut + squareLength

		translation = 0
		step = 0
		while (step<5):
			translation=xPointDebut+2*(step*squareLength)
			if ((rang%2)==0):
				drawSquare(translation, yPointDebut, squareLength, "black")
				drawSquare(translation+squareLength, yPointDebut, squareLength, "white")
			else:
				drawSquare(translation, yPointDebut, squareLength, "white")
				drawSquare(translation+squareLength, yPointDebut, squareLength, "black")
			step += 1
		rang += 1


def drawCircle(x, y, r, col):
	"Dessin d'un cercle de centre (x,y) et de rayon r"
	zone.create_oval(x+r, y+r, x-r, y-r, outline=col, width=1)


def drawRandomPoint():
	"Dessin d'un pion aléatoire sur le damier"

	squareLength = globLongueur

	randrow = randrange(10) + 1
	print(randrow)
	randcol = randrange(10) + 1
	print(randcol)

	randX = 0 + randcol*squareLength
	randY = 0 + randrow*squareLength

	borderPoint = 5

	zone.create_oval(randX + borderPoint, randY + borderPoint, randX +squareLength - borderPoint, randY+squareLength - borderPoint, fill='blue')

# horrible global variable I guess:
globLongueur = 45

footer  = Canvas(fenetre, bg = 'ivory', height=100, width= 600)
footer.pack(side=BOTTOM)

b1 = Button(fenetre, text='Quitter', command = zone.quit)
b1.pack(side = RIGHT, padx = 3, pady = 3)

b2 = Button(fenetre, text='Draw', command =drawDamier)
b2.pack(side = LEFT)

b3 = Button(fenetre, text="click", command=drawRandomPoint)
b3.pack()
fenetre.mainloop()

fenetre.destroy()




