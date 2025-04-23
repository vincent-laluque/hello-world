# Dans l'exemple qui suit nous allons créer une fenêtre très simple et y ajouter 
# deux widgets typiques: un bout de texte (Label) et un bouton (Button)
from tkinter import *
fen1 = Tk()
tex1 = Label(fen1, text='Bonjour tout le monde !', fg = 'red')
tex1.pack()
bou1 = Button(fen1, text='Quitter', command = fen1.destroy)
bou1.pack()
fen1.mainloop()


