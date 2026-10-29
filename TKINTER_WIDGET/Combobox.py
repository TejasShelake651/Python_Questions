
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Combobox Example")
root.geometry("350x200")

tk.Label(root, text="Select a language:").pack(pady=10)

combo = ttk.Combobox(
    root,
    values=["Python", "Java", "C++"],
    state="readonly"
)
combo.pack()
combo.set("Python")

label = tk.Label(root, text="")
label.pack(pady=10)

def show_selection(event=None):
    label.config(text="Selected: " + combo.get())

combo.bind("<<ComboboxSelected>>", show_selection)
ttk.Button(root, text="Show", command=show_selection).pack()

root.mainloop()
