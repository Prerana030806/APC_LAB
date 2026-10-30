import tkinter as tk
from tkinter import messagebox

def greet():
    name = name_entry.get().strip()
    if name:
        messagebox.showinfo("Greeting", "Hello, " + name + "!")
    else:
        messagebox.showwarning("Input Required", "Please enter your name.")

window = tk.Tk()
window.title("Tkinter GUI")
window.geometry("350x200")

heading = tk.Label(window, text="Welcome to Python GUI", font=("Arial", 16))
heading.pack(pady=15)

name_entry = tk.Entry(window, width=30)
name_entry.pack(pady=8)

greet_button = tk.Button(window, text="Submit", command=greet)
greet_button.pack(pady=10)

window.mainloop()
