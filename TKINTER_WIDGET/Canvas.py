
import tkinter as tk

root = tk.Tk()
root.title("Canvas Example")
root.geometry("450x350")

canvas = tk.Canvas(
    root, width=400, height=280, bg="white"
)
canvas.pack(padx=10, pady=10)

# Draw a line
canvas.create_line(20, 20, 180, 20, fill="blue", width=3)

# Draw a rectangle
canvas.create_rectangle(
    30, 50, 150, 120, outline="green", width=3
)

# Draw a circle
canvas.create_oval(
    200, 50, 300, 150, outline="red", width=3
)

# Display text
canvas.create_text(
    200, 210, text="Tkinter Canvas",
    font=("Arial", 16)
)

root.mainloop()
