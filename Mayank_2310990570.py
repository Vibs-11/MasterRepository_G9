import tkinter as tk
from tkinter import ttk

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = int(operation_var.get())

    if operation == 1:
        result.set(num1 * num2)
    elif operation == 2:
        if num2 != 0:
            result.set(num1 / num2)
        else:
            result.set("Error: Cannot divide by zero.")
    elif operation == 3:
        result.set(num1 - num2)
    elif operation == 4:
        result.set(num1 ** num2)
    else:
        result.set("Invalid operation")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Set background color
root.configure(bg="#f0f0f0")

# Create and place widgets
tk.Label(root, text="Enter the first number:", font=('Helvetica', 12), bg="#f0f0f0").grid(row=0, column=0, pady=5)
entry_num1 = tk.Entry(root, font=('Helvetica', 12))
entry_num1.grid(row=0, column=1, pady=5)

tk.Label(root, text="Enter the second number:", font=('Helvetica', 12), bg="#f0f0f0").grid(row=1, column=0, pady=5)
entry_num2 = tk.Entry(root, font=('Helvetica', 12))
entry_num2.grid(row=1, column=1, pady=5)

tk.Label(root, text="Select the operation:", font=('Helvetica', 12), bg="#f0f0f0").grid(row=2, column=0, pady=5)
operation_var = tk.IntVar()
operation_var.set(1)  # Default to multiplication
operations = [("Multiplication", 1), ("Division", 2), ("Subtraction", 3), ("Exponent", 4)]

for i, (text, value) in enumerate(operations):
    tk.Radiobutton(root, text=text, variable=operation_var, value=value, font=('Helvetica', 12), bg="#f0f0f0").grid(row=2, column=i+1, padx=5)

calculate_button = tk.Button(root, text="Calculate", command=calculate, font=('Helvetica', 12), bg="#4caf50", fg="white")
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result = tk.StringVar()
result.set("Result will be shown here")
result_label = tk.Label(root, textvariable=result, font=('Helvetica', 12), bg="#f0f0f0")
result_label.grid(row=4, column=0, columnspan=2, pady=5)

# Start the main loop
root.mainloop()
