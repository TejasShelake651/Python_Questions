
import tkinter as tk

root = tk.Tk()
root.title("Radiobutton Example")
root.geometry("300x200")

choice = tk.StringVar(value="Male")

tk.Radiobutton(root, text="Male", variable=choice, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=choice, value="Female").pack()
tk.Radiobutton(root, text="Other", variable=choice, value="Other").pack()

def show_choice():
    label.config(text="Selected: " + choice.get())

tk.Button(root, text="Submit", command=show_choice).pack(pady=10)
label = tk.Label(root, text="")
label.pack()

root.mainloop()
