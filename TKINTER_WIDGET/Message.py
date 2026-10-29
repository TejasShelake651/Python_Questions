
import tkinter as tk

root = tk.Tk()
root.title("Message Example")
root.geometry("350x200")

message = tk.Message(
    root,
    text="Welcome to Python programming. "
         "Tkinter is used to create graphical "
         "user interface applications.",
    width=280,
    bg="lightgreen",
    font=("Arial", 12)
)
message.pack(pady=30)

root.mainloop()
