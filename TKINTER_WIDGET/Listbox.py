
import tkinter as tk

root = tk.Tk()
root.title("Listbox Example")
root.geometry("300x250")

listbox = tk.Listbox(root)
for item in ["Python", "Java", "C++", "JavaScript"]:
    listbox.insert(tk.END, item)

listbox.pack(pady=10)

def show_item():
    selected = listbox.curselection()
    if selected:
        label.config(text="Selected: " + listbox.get(selected[0]))

tk.Button(root, text="Show Selection", command=show_item).pack()
label = tk.Label(root, text="")
label.pack(pady=10)

root.mainloop()
