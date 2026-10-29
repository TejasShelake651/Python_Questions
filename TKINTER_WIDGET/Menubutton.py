
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Menubutton Example")
root.geometry("300x180")

menu_button = tk.Menubutton(
    root, text="Click Here",
    relief=tk.RAISED
)
menu_button.pack(pady=40)

menu = tk.Menu(menu_button, tearoff=0)
menu_button.config(menu=menu)

menu.add_command(
    label="Contact",
    command=lambda: messagebox.showinfo(
        "Contact", "Contact us at example@example.com"
    )
)
menu.add_command(
    label="About",
    command=lambda: messagebox.showinfo(
        "About", "Python Tkinter Application"
    )
)

root.mainloop()
