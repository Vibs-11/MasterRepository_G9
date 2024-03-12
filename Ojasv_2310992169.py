import tkinter as tk
from tkinter import ttk
from math import sqrt, sin, cos, tan, radians

def on_click(button_value):
    current = entry_var.get()
    
    if button_value == "=":
        try:
            result = eval(current)
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif button_value == "C":
        entry_var.set("")
    elif button_value == "√":
        try:
            result = sqrt(float(current))
            entry_var.set(result)
        except ValueError:
            entry_var.set("Error")
    elif button_value == "%":
        try:
            result = eval(current) / 100
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif button_value in ("sin", "cos", "tan"):
        try:
            angle = radians(float(current))
            if button_value == "sin":
                result = sin(angle)
            elif button_value == "cos":
                result = cos(angle)
            elif button_value == "tan":
                result = tan(angle)
            entry_var.set(result)
        except ValueError:
            entry_var.set("Error")
    else:
        entry_var.set(current + str(button_value))

def change_theme(theme_name):
    style.theme_use(theme_name)

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")

# Entry widget for displaying the input and results
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, justify="right", font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=6, sticky="nsew", pady=5)

# Configure grid weights to make the entry expandable
for i in range(6):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i, weight=1)

# Style for ttk themed buttons
style = ttk.Style()
style.configure("TButton", font=("Arial", 12))

# Buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("√", 5, 0), ("%", 5, 1), ("C", 5, 2),
    ("sin", 1, 4), ("cos", 2, 4), ("tan", 3, 4)
]

for (text, row, col) in buttons:
    ttk.Button(root, text=text, command=lambda t=text: on_click(t)).grid(row=row, column=col, sticky="nsew")

# Color themes
theme_label = tk.Label(root, text="Color Themes:", font=("Arial", 12))
theme_label.grid(row=6, column=0, columnspan=2)

themes = ["clam", "alt", "default", "classic"]
for i, theme in enumerate(themes):
    ttk.Button(root, text=theme.capitalize(), command=lambda t=theme: change_theme(t)).grid(row=6, column=i+2, sticky="nsew")

# Run the GUI
root.mainloop()