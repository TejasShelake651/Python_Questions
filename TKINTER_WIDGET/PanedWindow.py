
import tkinter as tk

root = tk.Tk()
root.title("PanedWindow Example")
root.geometry("450x250")

paned = tk.PanedWindow(
    root, orient=tk.HORIZONTAL,
    sashwidth=6, bg="gray"
)
paned.pack(fill="both", expand=True, padx=10, pady=10)

left = tk.Label(
    paned, text="Left Pane",
    bg="lightblue", width=20
)

right = tk.Label(
    paned, text="Right Pane",
    bg="lightgreen", width=20
)

paned.add(left)
paned.add(right)

root.mainloop()

