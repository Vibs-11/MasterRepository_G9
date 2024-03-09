import tkinter as tk
from tkinter import messagebox
from math import sqrt

def perform_operation():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == 1:
            result = num1 * num2
        elif operation == 2:
            result = num1 / num2
        elif operation == 3:
            result = num1 - num2
        elif operation == 4:
            result = num1 ** num2
        elif operation == 5:
            result = sqrt(num1)
        elif operation == 6:  # Addition
            result = num1 + num2
        else:
            result = "Invalid Operation"

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Enhanced Calculator")

# Labels and Entry Widgets
label_num1 = tk.Label(root, text="Enter the first number:")
entry_num1 = tk.Entry(root)

label_num2 = tk.Label(root, text="Enter the second number:")
entry_num2 = tk.Entry(root)

# Operation Frame
operation_frame = tk.LabelFrame(root, text="Select the operation:")
operation_var = tk.IntVar()
operation_var.set(1)

radio_multiply = tk.Radiobutton(operation_frame, text="Multiplication", variable=operation_var, value=1)
radio_divide = tk.Radiobutton(operation_frame, text="Division", variable=operation_var, value=2)
radio_subtract = tk.Radiobutton(operation_frame, text="Subtraction", variable=operation_var, value=3)
radio_exponent = tk.Radiobutton(operation_frame, text="Exponent", variable=operation_var, value=4)
radio_sqrt = tk.Radiobutton(operation_frame, text="Square Root", variable=operation_var, value=5)
radio_add = tk.Radiobutton(operation_frame, text="Addition", variable=operation_var, value=6)

# Buttons and Labels
button_calculate = tk.Button(root, text="Calculate", command=perform_operation)
result_label = tk.Label(root, text="Result: ")

# Grid layout
label_num1.grid(row=0, column=0, padx=10, pady=10)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2.grid(row=1, column=0, padx=10, pady=10)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

operation_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
radio_multiply.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
radio_divide.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
radio_subtract.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
radio_exponent.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
radio_sqrt.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
radio_add.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)

button_calculate.grid(row=3, column=0, columnspan=2, pady=10)
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
