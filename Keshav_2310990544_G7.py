import tkinter as tk
from tkinter import messagebox
import math

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

def square_root():
    try:
        number = float(entry.get())
        result = math.sqrt(number)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid Input")

def square():
    try:
        number = float(entry.get())
        result = number ** 2
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid Input")

def backspace():
    current_text = entry.get()
    entry.delete(len(current_text) - 1)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create the entry widget
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("/", 4, 3),
    ("sqrt", 5, 0), ("x^2", 5, 1), ("⌫", 5, 2)  # Backspace button
]

# Add buttons to the GUI
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, padx=30, pady=20, command=calculate)
    elif text == "sqrt":
        btn = tk.Button(root, text=text, padx=25, pady=20, command=square_root)
    elif text == "x^2":
        btn = tk.Button(root, text=text, padx=25, pady=20, command=square)
    elif text == "⌫":  # Backspace button
        btn = tk.Button(root, text=text, padx=25, pady=20, command=backspace)
    else:
        btn = tk.Button(root, text=text, padx=30, pady=20, command=lambda t=text: entry.insert(tk.END, t))
    btn.grid(row=row, column=col)

root.mainloop()
