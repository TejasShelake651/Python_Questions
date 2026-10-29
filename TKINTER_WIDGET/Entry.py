
import tkinter as tk

root = tk.Tk()
root.title("Entry Example")
root.geometry("350x180")

tk.Label(root, text="Enter your name:").pack(pady=5)

entry = tk.Entry(root)
entry.pack()

def display():
    result.config(text="Hello, " + entry.get())

tk.Button(root, text="Submit", command=display).pack(pady=10)

result = tk.Label(root, text="")
result.pack()

root.mainloop()
