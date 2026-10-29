
import tkinter as tk

root = tk.Tk()
root.title("Main Window")
root.geometry("300x150")

def open_window():
    second = tk.Toplevel(root)
    second.title("Second Window")
    second.geometry("300x150")

    tk.Label(
        second, text="This is a Toplevel window"
    ).pack(pady=20)

    tk.Button(
        second, text="Close",
        command=second.destroy
    ).pack()

tk.Button(
    root, text="Open New Window",
    command=open_window
).pack(pady=40)

root.mainloop()
