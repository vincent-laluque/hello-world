import tkinter as tk

root = tk.Tk()
root.title("My First GUI App")
root.geometry("400x200")

# Basic text label
title_label = tk.Label(
                       root,
                       text = "Welcome to hell",
                       font = ("Arial",18, "bold"),
                       fg = "darkblue"
                       )
title_label.pack()

# Label with wrapping and center alignment
description = tk.Label(
    root,
    text="Labels display static text. They are read-only - "
         "use Entry widgets for user input.",
    font=("Arial", 10),
    fg="gray",
    wraplength=350,
    justify="center"
)
description.pack(pady=10)

# Label with background color
highlight = tk.Label(
    root,
    text="Colored backgrounds are easy too!",
    font=("Arial", 12, "italic"),
    bg="lightyellow",
    padx=20,
    pady=10
)
highlight.pack(pady=10)

label = tk.Label(root, text="Hello Tkinter")
label.pack()

root.mainloop()




