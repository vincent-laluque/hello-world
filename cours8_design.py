import tkinter as tk

fenetre_racine = tk.Tk()



# frame1 = tk.Frame(fenetre_racine, width = 200, height = 100, bg = 'red')
# frame1.pack(side=tk.TOP)

# txt1 = tk.Label(frame1, text='Premier champ :', width = 15)
# txt1.pack(side=tk.LEFT)

# entr1 = tk.Entry(frame1)
# entr1.pack(side=tk.RIGHT)


# frame2 = tk.Frame(fenetre_racine, width = 200, height = 100, bg = 'blue')
# frame2.pack(side=tk.BOTTOM)

# txt2 = tk.Label(frame2, text='Second :', width = 15)
# txt2.pack(side=tk.LEFT)

# entr2 = tk.Entry(frame2)
# entr2.pack(side=tk.RIGHT)



txt1 = tk.Label(fenetre_racine, text = 'Premier champ :')
txt2 = tk.Label(fenetre_racine, text = 'Second :')
entr1 = tk.Entry(fenetre_racine)
entr2 = tk.Entry(fenetre_racine)

txt1.grid(row=0, sticky = tk.E)
txt2.grid(row=1, sticky = tk.E)
entr1.grid(row=0, column=1)
entr2.grid(row=1, column=1)

fenetre_racine.mainloop()

