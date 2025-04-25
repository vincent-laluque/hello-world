# Petit exercice utilisant la bibliothèque graphique tkinter

from tkinter import *
from random import randrange

# définition des fonctions gestionnaire d'événements
def drawline():
    "Tracé d'une ligne dans le canevas can1"
    global x1, y1, x2, y2, coul
    can1.create_line(x1,y1,x2,y2,width=2,fill=coul)

def changecolor():
    "Changement aléatoire de la couleur du tracé"
    global coul
    pal = ['purple', 'cyan', 'maroon', 'green', 'red', 'blue', 'orange', 'yellow']
    c = randrange(8)
    coul = pal[c]


# Programme principal
x1, y1, x2, y2 = 10, 190, 190, 10
coul = 'dark green'

# Création du widget principal ("maître"):
fen1 = Tk()

# Création des widgets "esclaves":
can1 = Canvas(fen1, bg='dark grey', height=200, width=200)
can1.pack(side=LEFT)

bou1 = Button(fen1, text='Quitter', command = fen1.quit) # fen1.quit() fait quitter le réceptionnaire d'événements (mainloop) associé à fen1
bou1.pack(side=BOTTOM)

bou2 = Button(fen1, text='Tracer une ligne', command = drawline)
bou2.pack()

bou3 = Button(fen1, text='Autre couleur', command=changecolor)
bou3.pack()

fen1.mainloop()

fen1.destroy()
