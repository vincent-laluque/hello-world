
from tkinter import *

# Création du widget (= "Window gadget") ou (= "Composant graphique") ou ("Contrôle") principal

fenetre = Tk()

# Widget: ce terme désigne toute entité susceptible d'être placée dans une fenêtre d'application
# comme par exemple un bouton, une case à cocher, une image, etc., et parfois aussi la fenêtre elle-même.

# Création des widgets "esclaves":
zone = Canvas(fenetre, bg='white', height=400, width=600)
zone.pack(side=LEFT)

def drawCircle(x1,y1,x2,y2,coul):
    "Tracé d'un anneau"
# Ovals, mathematically, are ellipses, including circles as a special case. 
# The ellipse is fit into a rectangle defined by the coordinates (x0, y0) of the top left corner 
# and the coordinates (x1, y1) of a point just outside of the bottom right corner. 
    zone.create_oval(x1,y1,x2,y2,outline=coul,width=3)

def drawCircles():
    "Tracé des cinq anneaux"
x1, y1, x2, y2 = 50, 50, 150, 150
drawCircle(x1,y1,x2,y2,'blue')
x1 =x1+80
x2 = x2+80
drawCircle(x1,y1,x2,y2,'black')
x1 =x1+80
x2 = x2+80
drawCircle(x1,y1,x2,y2,'red')
x1, y1, x2, y2 = 50, 50, 150, 150
x1 =x1+40
x2 = x2+40
y1 = y1+40
y2 = y2 +40
drawCircle(x1,y1,x2,y2,'orange')
x1 =x1+80
x2 = x2+80
drawCircle(x1,y1,x2,y2,'green')

boutonQuit = Button(fenetre, text='Quitter', command=zone.quit)
boutonQuit.pack(side=BOTTOM)

boutonExecute = Button(fenetre, text='Execute', command=drawCircles)
boutonExecute.pack(side=BOTTOM)
fenetre.mainloop()

fenetre.destroy()
