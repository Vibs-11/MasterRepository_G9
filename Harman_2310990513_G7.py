import tkinter as tk
from tkinter import ttk
import math

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            expression = display.get().replace("^", "**")
            result = str(eval(expression))
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except ZeroDivisionError:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error: Division by zero")
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error: Invalid expression")
    elif text == "C":
        display.delete(0, tk.END)
    elif text == "<--":
        current_text = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, current_text[:-1])
    elif text == "sin":
        try:
            value = float(display.get())
            result = math.sin(math.radians(value))
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except ValueError:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error: Invalid input")
    elif text == "cos":
        try:
            value = float(display.get())
            result = math.cos(math.radians(value))
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except ValueError:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error: Invalid input")
    elif text == "tan":
        try:
            value = float(display.get())
            result = math.tan(math.radians(value))
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except ValueError:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error: Invalid input")
        except ZeroDivisionError:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error: Tan of 90 or 270 degrees is undefined")
    else:
        display.insert(tk.END, text)

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)

# Style
style = ttk.Style()
style.theme_use('clam')

# Configure style for buttons
style.configure('TButton', font=('Arial', 16), padding=5)

# Create a text entry widget for the display
display = tk.Entry(root, font=("Arial", 24), justify="right", bd=5)
display.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="ew")

# Define the button labels and their positions in the grid
button_labels = [
    ("sin", 1, 0), ("cos", 1, 1), ("tan", 1, 2), ("<--", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("+", 5, 3),
    ("C", 6, 0), ("^0.5", 6, 1), ("^", 6, 2), ("^2", 6, 3),
]

# Create and place the calculator buttons
for label, row, col in button_labels:
    button = ttk.Button(root, text=label, width=4)
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    button.bind("<Button-1>", on_click)

# Configure grid weights to make buttons expandable
for i in range(5):
    root.grid_columnconfigure(i, weight=1)
for i in range(1, 7):
    root.grid_rowconfigure(i, weight=1)

# Run the main loop
root.mainloop()
