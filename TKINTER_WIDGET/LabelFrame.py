
import tkinter as tk

root = tk.Tk()
root.title("LabelFrame Example")
root.geometry("350x220")

frame = tk.LabelFrame(
    root, text="Personal Information",
    padx=15, pady=15
)
frame.pack(padx=20, pady=30, fill="x")

tk.Label(frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(frame).grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Age:").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(frame).grid(row=1, column=1, padx=5, pady=5)

root.mainloop()
