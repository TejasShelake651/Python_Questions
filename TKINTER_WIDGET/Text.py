
import tkinter as tk

root = tk.Tk()
root.title("Text Widget Example")
root.geometry("400x300")

text = tk.Text(root, height=8, width=40)
text.pack(padx=10, pady=10)

text.insert(tk.END, "Write your text here...")

def show_text():
    content = text.get("1.0", tk.END).strip()
    result.config(text="Characters: " + str(len(content)))

tk.Button(root, text="Count Characters", command=show_text).pack()

result = tk.Label(root, text="")
result.pack(pady=10)

root.mainloop()
