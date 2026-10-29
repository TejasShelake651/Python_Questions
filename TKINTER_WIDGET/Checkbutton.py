
import tkinter as tk

root = tk.Tk()
root.title("Checkbutton Example")
root.geometry("300x200")

python_var = tk.IntVar()
java_var = tk.IntVar()

tk.Checkbutton(root, text="Python", variable=python_var).pack()
tk.Checkbutton(root, text="Java", variable=java_var).pack()

def show_selection():
    result = []
    if python_var.get():
        result.append("Python")
    if java_var.get():
        result.append("Java")

    label.config(text="Selected: " + ", ".join(result))

tk.Button(root, text="Submit", command=show_selection).pack(pady=10)
label = tk.Label(root, text="")
label.pack()

root.mainloop()
