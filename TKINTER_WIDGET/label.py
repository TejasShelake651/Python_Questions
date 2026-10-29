
import tkinter as tk

root = tk.Tk()
root.title("Label Example")
root.geometry("300x150")

label = tk.Label(root, text="Welcome to Python GUI")
label.pack(pady=30)

root.mainloop()
