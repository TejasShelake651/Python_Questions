
import tkinter as tk

root = tk.Tk()
root.title("Spinbox Example")
root.geometry("300x180")

tk.Label(root, text="Select Semester:").pack(pady=10)

spinbox = tk.Spinbox(root, from_=1, to=8)
spinbox.pack()

label = tk.Label(root, text="")
label.pack(pady=10)

def show_value():
    label.config(text="Semester: " + spinbox.get())

tk.Button(root, text="Submit", command=show_value).pack()

root.mainloop()
