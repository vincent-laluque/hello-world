import tkinter as tk

def pointeur(event):
	chaine.configure(text = "Clic détecté en X =" + str(event.x) +\
	                 ", Y =" +str(event.y))

main = tk.Tk()
cadre = tk.Frame(main, width = 200, height = 150, bg = "light yellow")
cadre.bind("<Button-1>", pointeur)
cadre.pack()
chaine = tk.Label(main)
chaine.pack()

main.mainloop()

