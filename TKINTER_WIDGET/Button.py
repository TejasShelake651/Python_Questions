
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Button Example")
root.geometry("300x150")

def show_message():
    messagebox.showinfo("Message", "Button clicked!")

button = tk.Button(root, text="Click Here", command=show_message)
button.pack(pady=40)

root.mainloop()
