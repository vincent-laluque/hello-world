import tkinter as tk


main = tk.Tk()


zone = tk.Canvas(main, width = 200, height = 150, bg ="light yellow")
zone.pack()


def drawCircle(x, y, r, col):
	"Dessin d'un cercle de centre x et y et de rayon r"
	zone.create_oval(x+r, y+r, x-r, y-r, outline=col, width=1)


def dealWithThisEvent(event):
	chaine.configure(text  = "Clic détecté en X =" + str(event.x) + ", Y=" + str(event.y))
	drawCircle(event.x,event.y, 10, 'red')



zone.bind("<Button-1>",dealWithThisEvent)
zone.pack()

chaine = tk.Label(main)
chaine.pack()

main.mainloop()



