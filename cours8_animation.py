import tkinter as tk

window = tk.Tk()
window.title("Exercice d'animation avec tkinter")


def avance(gd, hb):
	global x1, y1
	x1, y1 = x1 + gd, y1 +hb
	can1.coords(oval1, x1,y1, x1+30, y1+30)

# gestionnaires d'événements:
def depl_gauche():
	avance(-10, 0)

def depl_droite():
	avance(10, 0)

def depl_haut():
	avance(0, -10)

def depl_bas():
	avance(0, 10)

# programme principal
x1, y1 = 10, 10 # coordonnées initiales

# création des widgets esclaves
can1 = tk.Canvas(window, bg = 'dark grey', height = 300, width = 300)
oval1 = can1.create_oval(x1, y1, x1 + 30, y1 + 30, width = 2, fill='red')
can1.pack(side=tk.LEFT)

tk.Button(window, text = 'Quitter', command=window.quit).pack(side=tk.BOTTOM)
tk.Button(window, text = 'Gauche', command = depl_gauche).pack()
tk.Button(window, text = 'Droite', command = depl_droite).pack()
tk.Button(window, text = 'Haut', command = depl_haut).pack()
tk.Button(window, text = 'Bas', command = depl_bas).pack()

window.mainloop()



