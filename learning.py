



# alors chaque journée j'apprends 5 équivalents clavier:
# Command + D is amazing because you can select all the same work in the same page
# With Command + X you can delete a whole line in the blink of an eye
# With Command + K + Command + K you can delete everything right to the cursor until the end of the lin
# With Command + RETURN you can add a line below the line where you are AND the cursor goes to the beginning
#  of the new line
# With Command + MAJ + RETURN you can add a line above the line where you are AND the cursor goes to the beginning
#  of this new line


import tkinter as tk


main = tk.Tk()


zone = tk.Canvas(main, width = 200, height = 150, bg ="light yellow")

zone.pack()

def drawCircle(x, y, r, col):
	"Dessin d'un cercle de centre x et y et de rayon r"
	zone.create_oval(x+r, y+r, x-r, y-r, outline=col, width=1)










	zone.create_oval(x+r, y+r, x-r, y-r, outline=col, width=1)



	zone.create_oval(x+r, y+r, x-r, y-r, outline=col, width=1)

def dealWithThisEvent(event):



	chaine.configure(text  = "Clic détecté en X =" + str(event.x) + ", Y=" + str(event.y))

	drawCircle(event.x,event.y, 10, 'red')



zone.bind("<Button-1>",dealWithThisEvent)

zone.pack()

chaine = tk.Label(main)
chaine.pack()

main.mainloop()



