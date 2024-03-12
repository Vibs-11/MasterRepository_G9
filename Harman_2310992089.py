import tkinter as tk
from tkinter import messagebox
import math

# Define the operations
def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        messagebox.showerror("Error", "Cannot divide by zero")
        return "Error"
    return num1 / num2

def subtraction(num1, num2):
    return num1 - num2

def exponent(num1, num2):
    return num1 ** num2

def sine(num1):
    return math.sin(math.radians(num1))

def cosine(num1):
    return math.cos(math.radians(num1))

def tangent(num1):
    return math.tan(math.radians(num1))

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")

# Set a color theme
root.configure(bg="#333333")

# Create a label
label = tk.Label(root, text="Calculator to perform operation:", bg="#333333", fg="#ffffff")
label.pack()

# Create entry fields for the numbers
entry = tk.Entry(root)
entry.pack()

# Create a label for the result
result_label = tk.Label(root, text="", bg="#333333", fg="#ffffff")
result_label.pack()

# Define the operation function
def perform_operation(operation):
    try:
        num1, num2 = map(float, entry.get().split())
        if operation == "multiplication":
            result = multiplication(num1, num2)
        elif operation == "division":
            result = division(num1, num2)
        elif operation == "subtraction":
            result = subtraction(num1, num2)
        elif operation == "exponent":
            result = exponent(num1, num2)
        elif operation == "sine":
            result = sine(num1)
        elif operation == "cosine":
            result = cosine(num1)
        elif operation == "tangent":
            result = tangent(num1)
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter two numbers separated by a space.")

# Function to update the entry with the button's value
def update_entry(value):
    entry.insert(tk.END, value)

# Create number buttons
for i in range(1, 10):
    button = tk.Button(root, text=str(i), command=lambda i=i: update_entry(str(i)))
    button.pack(side=tk.LEFT)

# Create buttons for each operation
button_mul = tk.Button(root, text="*", command=lambda: perform_operation("multiplication"))
button_mul.pack(side=tk.LEFT)

button_div = tk.Button(root, text="/", command=lambda: perform_operation("division"))
button_div.pack(side=tk.LEFT)

button_sub = tk.Button(root, text="-", command=lambda: perform_operation("subtraction"))
button_sub.pack(side=tk.LEFT)

button_exp = tk.Button(root, text="^", command=lambda: perform_operation("exponent"))
button_exp.pack(side=tk.LEFT)

button_sin = tk.Button(root, text="sin", command=lambda: perform_operation("sine"))
button_sin.pack(side=tk.LEFT)

button_cos = tk.Button(root, text="cos", command=lambda: perform_operation("cosine"))
button_cos.pack(side=tk.LEFT)

button_tan = tk.Button(root, text="tan", command=lambda: perform_operation("tangent"))
button_tan.pack(side=tk.LEFT)

# Run the main loop
root.mainloop()
