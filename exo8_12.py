import tkinter as tk

widget_principal = tk.Tk()
widget_principal.title("Deux astres")


# J'ai besoin de deux labels en haut du widget principale m'affichant la masse des deux astres



labelM1 = tk.Label(widget_principal, text= "M1 =")
labelM1.grid(row = 0, column = 0, sticky = tk.W)

labelM2 = tk.Label(widget_principal, text= "M2 =")
labelM2.grid(row = 0, column = 1, sticky = tk.W)

widget_dessin = tk.Canvas(widget_principal, width = 600, height = 400, bg = "darkblue")
widget_dessin.grid(row = 1, columnspan = 2)

labelM3 = tk.Label(widget_principal, text = "Distance =")
labelM3.grid(row = 2, column = 0, sticky = tk.W)

labelM4 = tk.Label(widget_principal, text = "Force =")
labelM4.grid(row = 2, column = 1, sticky = tk.W)


widget_principal.mainloop()











