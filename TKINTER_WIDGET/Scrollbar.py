
import tkinter as tk

root = tk.Tk()
root.title("Scrollbar Example")
root.geometry("300x250")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set)
for i in range(1, 51):
    listbox.insert(tk.END, "Item " + str(i))

listbox.pack(side=tk.LEFT)
scrollbar.config(command=listbox.yview)

root.mainloop()
