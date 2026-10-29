
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Menu Example")
root.geometry("350x200")

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(
    label="New",
    command=lambda: messagebox.showinfo("New", "New selected")
)
file_menu.add_command(
    label="About",
    command=lambda: messagebox.showinfo("About", "Tkinter Menu")
)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

root.mainloop()
