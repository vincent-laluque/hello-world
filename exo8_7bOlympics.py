# Importons toutes les classes du module Tkinter:
from tkinter import *


# Création du widget (ou composant graphique ou contrôle) principal
fenetre = Tk()

# Création des widgets qui habitent dans le widget
zone = Canvas(fenetre, bg='white', height=400, width=600)
zone.pack()

def drawCircle(x1,y1,x2,y2,coul):
    "Tracé d'un anneau"
    zone.create_oval(x1,y1,x2,y2,outline=coul,width=6)

# Je souhaite avoir un tableau à 2 dimensions correspondant aux cadres des anneaux
Frames = [[50,50,150,150],[130,50,230,150],[210,50,310,150],[90,90,190,190],[170,90,270,190]]
Cols = ['blue','black','red','orange','green']

kk = 0
while(kk < 5):
    #drawCircle(Frames[kk][0],Frames[kk][1],Frames[kk][2],Frames[kk][3],Cols[kk])
    kk += 1

def drawOneCircle(indice):
    "Tracé d'un des anneaux olympiques"
    drawCircle(Frames[indice][0],Frames[indice][1],Frames[indice][2],Frames[indice][3],Cols[indice])

def T0():
    drawOneCircle(0)

def T1():
    drawOneCircle(1)

def T2():
    drawOneCircle(2)

def T3():
    drawOneCircle(3)

def T4():
    drawOneCircle(4)

boutonQuit = Button(fenetre,text='Quitter',command=zone.quit)
boutonQuit.pack(side=RIGHT)

boutonT0 = Button(fenetre,text="T0",command=T0)
boutonT0.pack(side=LEFT)

boutonT1 = Button(fenetre,text="T1",command=T1)
boutonT1.pack(side=LEFT)

boutonT2 = Button(fenetre,text="T2",command=T2)
boutonT2.pack(side=LEFT)

boutonT3 = Button(fenetre,text="T3",command=T3)
boutonT3.pack(side=LEFT)

boutonT4 = Button(fenetre,text="T4",command=T4)
boutonT4.pack(side=LEFT)




fenetre.mainloop()# démarrage du réceptionnaire d'évènements associé à la fenêtre
fenetre.destroy()
