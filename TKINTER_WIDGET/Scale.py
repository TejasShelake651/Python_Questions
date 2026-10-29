
import tkinter as tk

root = tk.Tk()
root.title("Scale Example")
root.geometry("350x200")

scale = tk.Scale(
    root,
    from_=0,
    to=100,
    orient=tk.HORIZONTAL,
    label="Select a value"
)
scale.pack(pady=10)

label = tk.Label(root, text="")
label.pack()

def show_value():
    label.config(text="Value: " + str(scale.get()))

tk.Button(root, text="Show Value", command=show_value).pack()

root.mainloop()
