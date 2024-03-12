import tkinter as tk
import math

# Function to add text to the input field
def add_to_input(value):
    entry.insert(tk.END, value)

# Function to calculate the result
def calculate_result():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to calculate trigonometric functions
def trig_function(func):
    try:
        value = float(entry.get())
        result = func(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to calculate exponential function
def calculate_exp():
    try:
        value = float(entry.get())
        result = math.exp(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display input and output
entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('sin', 1, 4), ('cos', 2, 4), ('tan', 3, 4),
    ('^', 5, 0), ('exp', 5, 1)
]

# Create buttons with respective commands
for (text, row, column) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, padx=30, pady=20, command=calculate_result)
    elif text in ['sin', 'cos', 'tan']:
        func = getattr(math, text)
        btn = tk.Button(root, text=text, padx=30, pady=20, command=lambda f=func: trig_function(f))
    elif text == '^':
        btn = tk.Button(root, text=text, padx=30, pady=20, command=lambda: add_to_input('**'))
    elif text == 'exp':
        btn = tk.Button(root, text=text, padx=30, pady=20, command=calculate_exp)
    else:
        btn = tk.Button(root, text=text, padx=30, pady=20, command=lambda t=text: add_to_input(t))
    btn.grid(row=row, column=column, padx=5, pady=5)

root.mainloop()
