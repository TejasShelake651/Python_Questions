
import tkinter as tk

root = tk.Tk()
root.title("Frame Example")
root.geometry("350x220")

frame = tk.Frame(
    root, bg="lightblue",
    bd=3, relief=tk.SOLID
)
frame.pack(padx=30, pady=30, fill="both", expand=True)

tk.Label(
    frame, text="Student Login",
    bg="lightblue", font=("Arial", 14, "bold")
).pack(pady=10)

tk.Label(frame, text="Username:", bg="lightblue").pack()
tk.Entry(frame).pack(pady=5)

root.mainloop()
