import tkinter as tk
from tkinter import ttk
import math

def calculate():
    num1 = float(entry_num1.get())
    operation = dropdown_operation.get()

    if operation == "Multiplication":
        result = num1 * float(entry_num2.get())
    elif operation == "Division":
        num2 = float(entry_num2.get())
        if num2 == 0:
            result = "Error! Division by zero"
        else:
            result = num1 / num2
    elif operation == "Subtraction":
        result = num1 - float(entry_num2.get())
    elif operation == "Exponentiation":
        result = num1 ** float(entry_num2.get())
    elif operation == "Logarithm":
        num2 = float(entry_num2.get())
        if num1 <= 0 or num2 <= 0:
            result = "Error! Logarithm is only defined for positive numbers."
        else:
            result = math.log(num1, num2)
    elif operation == "Square Root":
        if num1 < 0:
            result = "Error! Square root is only defined for non-negative numbers."
        else:
            result = math.sqrt(num1)
    elif operation == "Cube Root":
        result = num1 ** (1/3)
    elif operation == "Sine":
        result = math.sin(num1)
    elif operation == "Cosine":
        result = math.cos(num1)
    elif operation == "Tangent":
        result = math.tan(num1)

    label_result.config(text="Result: " + str(result))

def update_entry_visibility(event):
    if dropdown_operation.get() in ["Square Root", "Cube Root"]:
        entry_num2.grid_remove()
        label_num2.grid_remove()
    else:
        entry_num2.grid()
        label_num2.grid()

def exit_program():
    root.destroy()

root = tk.Tk()
root.title("Calculator")

# Create labels and entry fields for numbers
label_num1 = ttk.Label(root, text="Number 1:")
label_num1.grid(row=0, column=0, padx=5, pady=5)
entry_num1 = ttk.Entry(root)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

label_num2 = ttk.Label(root, text="Number 2:")
label_num2.grid(row=1, column=0, padx=5, pady=5)
entry_num2 = ttk.Entry(root)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

# Create dropdown menu for operations
label_operation = ttk.Label(root, text="Operation:")
label_operation.grid(row=2, column=0, padx=5, pady=5)
dropdown_operation = ttk.Combobox(root, values=["Multiplication", "Division", "Subtraction", "Exponentiation", "Logarithm", "Square Root", "Cube Root", "Sine", "Cosine", "Tangent"])
dropdown_operation.grid(row=2, column=1, padx=5, pady=5)
dropdown_operation.current(0)
dropdown_operation.bind("<<ComboboxSelected>>", update_entry_visibility)

# Create calculate button
button_calculate = ttk.Button(root, text="Calculate", command=calculate)
button_calculate.grid(row=3, column=0, padx=5, pady=5)

# Create exit button
button_exit = ttk.Button(root, text="Exit", command=exit_program)
button_exit.grid(row=3, column=1, padx=5, pady=5)

# Create label to display result
label_result = ttk.Label(root, text="Result:")
label_result.grid(row=4, columnspan=2, padx=5, pady=5)

root.mainloop()
