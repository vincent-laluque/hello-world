import tkinter as tk

window = tk.Tk()

tk.Label(window, text='Premier champ :').grid(sticky = tk.E)
tk.Label(window, text='Deuxième champ :').grid(sticky = tk.E)
tk.Label(window, text='Troisième champ :').grid(sticky = tk.E)

entr1 = tk.Entry(window)
entr2 = tk.Entry(window)
entr3 = tk.Entry(window)

entr1.grid(row = 0, column = 1)
entr2.grid(row = 1, column = 1)
entr3.grid(row = 2, column = 1)

check1 = tk.Checkbutton(window, text = 'Case à cocher pour voir')
check1.grid(columnspan = 2)

can1 = tk.Canvas(window, width = 160, height = 160, bg = 'white')
photo = tk.PhotoImage(file = 'php.png')
can1.create_image(80, 80, image=photo)
can1.grid(row = 0, column = 2, rowspan = 4, padx = 10, pady = 5)

window.mainloop()
