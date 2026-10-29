
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("MessageBox Example")
root.geometry("350x200")

def show_info():
    messagebox.showinfo("Information", "Welcome to Python!")

def show_warning():
    messagebox.showwarning("Warning", "Please check your input.")

def show_error():
    messagebox.showerror("Error", "An error occurred.")

def ask_question():
    answer = messagebox.askyesno(
        "Confirmation", "Do you want to continue?"
    )
    if answer:
        messagebox.showinfo("Result", "You selected Yes")
    else:
        messagebox.showinfo("Result", "You selected No")

tk.Button(root, text="Information", command=show_info).pack(pady=5)
tk.Button(root, text="Warning", command=show_warning).pack(pady=5)
tk.Button(root, text="Error", command=show_error).pack(pady=5)
tk.Button(root, text="Ask Yes/No", command=ask_question).pack(pady=5)

root.mainloop()
