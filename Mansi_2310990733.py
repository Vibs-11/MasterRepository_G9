import tkinter as tk
from tkinter import messagebox
import math

def multiplication():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 * num2
    label_result.config(text="Result: " + str(result))

def division():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    if num2 != 0:
        result = num1 / num2
        label_result.config(text="Result: " + str(result))
    else:
        messagebox.showerror("Error", "Division by zero is not allowed")

def subtraction():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 - num2
    label_result.config(text="Result: " + str(result))

def exponent():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 ** num2
    label_result.config(text="Result: " + str(result))

def logarithm():
    num = float(entry_num1.get())
    result = math.log(num)
    label_result.config(text="Result: " + str(result))

def square_root():
    num = float(entry_num1.get())
    result = math.sqrt(num)
    label_result.config(text="Result: " + str(result))

def cube_root():
    num = float(entry_num1.get())
    result = num ** (1/3)
    label_result.config(text="Result: " + str(result))

# Create main window
root = tk.Tk()
root.title("Calculator")

# Create input fields
label_num1 = tk.Label(root, text="Enter the first number:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Enter the second number:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

# Create buttons for operations
button_multiply = tk.Button(root, text="Multiplication", command=multiplication)
button_multiply.pack()

button_divide = tk.Button(root, text="Division", command=division)
button_divide.pack()

button_subtract = tk.Button(root, text="Subtraction", command=subtraction)
button_subtract.pack()

button_exponent = tk.Button(root, text="Exponent", command=exponent)
button_exponent.pack()

button_logarithm = tk.Button(root, text="Logarithm", command=logarithm)
button_logarithm.pack()

button_square_root = tk.Button(root, text="Square Root", command=square_root)
button_square_root.pack()

button_cube_root = tk.Button(root, text="Cube Root", command=cube_root)
button_cube_root.pack()

# Create label for result
label_result = tk.Label(root, text="")
label_result.pack()

# Run the main event loop
root.mainloop()
