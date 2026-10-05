import tkinter as tk

def on_click():
	label.config(text="Button was clicked!", fg="green")

def on_reset():
	label.config(text="Press the button above", fg="black")


root = tk.Tk()
root.title("Button Demo")
root.geometry("400x200")
root.bind('<Escape>', lambda e, w=root: w.destroy())

label = tk.Label(root, text="Press the button below", font=("Arial",14))
label.pack(pady=30)

# A regular button
my_button = tk.Button(
    root,
    text = "Click Me!",
    command=on_click,
    font=("Arial",12),
    bg="cornflowerblue",
    fg="white",
    padx=20,
    pady=5,
    cursor="hand2"
)
my_button.pack(pady=10)

# A reset button
reset_button = tk.Button(
    root,
    text="reset",
    command=on_reset,
    font=("Arial",10),
    bg="lightgray"
)
reset_button.pack(pady=5)

root.mainloop()

