# Petit exercice utilisant la bibliothèque graphique tkinter

from tkinter import *
from random import randrange

# définition des fonctions gestionnaire d'événements
def drawline():
    "Tracé d'une ligne dans le canevas can1"
    global x1, y1, x2, y2, coul
    can1.create_polygon(x1,y1,x2,y2,x1+10,y1,x2,y2+50,width=2,fill=coul)
    # modification des coordonnées pour la ligne suivante:
    y2, y1 = y2+10, y1-10

def changecolor():
    "Changement aléatoire de la couleur du tracé"
    global coul
    pal = ['purple', 'cyan', 'maroon', 'green', 'red', 'blue', 'orange', 'yellow']
    c = randrange(3)
    c += 1
    coul = pal[c]
    print(coul)


# Programme principal
x1, y1, x2, y2 = 10, 190, 190, 10
#x1, y1, x2, y2 = 10, 100, 190, 100
coul = 'dark green'

# Création du widget principal ("maître"):
fen1 = Tk()

# Création des widgets "esclaves":
can1 = Canvas(fen1, bg='dark grey', height=200, width=200)
can1.pack(side=LEFT)

bou1 = Button(fen1, text='Quitter', command = fen1.quit) # fen1.quit() fait quitter le réceptionnaire d'événements (mainloop) associé à fen1
bou1.pack(side=BOTTOM)

bou2 = Button(fen1, text='Tracer un truc', command = drawline)
bou2.pack()

bou3 = Button(fen1, text='Autre couleur', command=changecolor)
bou3.pack()

fen1.mainloop()

fen1.destroy()


# Pour create_rectangle, les coordonées fournies en paramètres indiquent:
# can1.create_rectangle(x1,y1,x2,y2,width=2,fill=coul)
# Le point supérieur droit du rectangle: x1,y1 et Le point inférieur droit du rectangle: x2,y2

# Pour create_arc, les coordonées fournies en paramètres indiquent:
# can1.create_arc(x1,y1,x2,y2,start=90,extent=180,width=2,style=ARC,fill=coul)
# An arc object on a canvas, in its most general form, is a wedge-shaped slice taken out of an ellipse. This includes whole ellipses and circles as special cases
# Point (x0, y0) is the top left corner and (x1, y1) the lower right corner of a rectangle into which the ellipse is fit. If this rectangle is square, you get a circle. 
# A noter pour le start=90: il s'agit d'un décalage vers la gauche (sens trigonométrique)

# Pour create_oval:
# can1.create_oval(x1,y1,x2,y2,width=2,fill=coul)
# Ovals, mathematically, are ellipses, including circles as a special case. 
# The ellipse is fit into a rectangle defined by the coordinates (x0, y0) of the top left corner and the coordinates (x1, y1) of a point just outside of the bottom right corner. 

# Pour create_polygon:
# As displayed, a polygon has two parts: its outline and its interior. Its geometry is specified as a series of vertices [(x0, y0), (x1, y1), … (xn, yn)], 
# but the actual perimeter includes one more segment from (xn, yn) back to (x0, y0). 