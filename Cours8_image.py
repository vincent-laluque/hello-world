import tkinter as tk

fenetre = tk.Tk()

txt1 = tk.Label(fenetre, text = 'Premier champ :')
txt2 = tk.Label(fenetre, text = 'Second :')
txt3 = tk.Label(fenetre, text = 'Troisième :')

entr1 = tk.Entry(fenetre)
entr2 = tk.Entry(fenetre)
entr3 = tk.Entry(fenetre)

canevas =tk.Canvas(fenetre, width = 160, height = 160, bg = 'white')
photo = tk.PhotoImage(file = 'php.png')
item = canevas.create_image(80, 80, image =photo)

txt1.grid(row=1, sticky = tk.E)
txt2.grid(row=2, sticky = tk.E)
txt3.grid(row=3, sticky = tk.E)

entr1.grid(row =1, column =2)
entr2.grid(row =2, column =2)
entr3.grid(row =3, column =2)

canevas.grid(row =1, column =3, rowspan =3, padx =10, pady =5)

fenetre.mainloop()

