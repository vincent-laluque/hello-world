import tkinter as tk
from math import *

main = tk.Tk() # le widget principal on va dire ?

# action à effectuer si l'utilisateur actionne la touche "enter" alors qu'il édite le champ d'entrée:
def evaluate(event):
	chaine.configure(text="Résultat = "+str(eval(entree.get())))

entree = tk.Entry(main)
entree.bind("<Return>", evaluate)
chaine = tk.Label(main)
entree.pack()
chaine.pack()

main.mainloop()