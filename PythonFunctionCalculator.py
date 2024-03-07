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
root.geometry("400x500")
root.configure(bg="#f0f0f0")

# Create and place widgets
tk.Label(root, text="Simple Calculator", font=('Helvetica', 16, 'bold'), bg="#f0f0f0").grid(row=0, column=0, columnspan=4, pady=10)

tk.Label(root, text="Enter the first number:", font=('Helvetica', 12), bg="#f0f0f0").grid(row=1, column=0, pady=5, padx=10, sticky="w")
entry_num1 = tk.Entry(root, font=('Helvetica', 12))
entry_num1.grid(row=1, column=1, pady=5, padx=10, columnspan=3, sticky="we")

tk.Label(root, text="Enter the second number:", font=('Helvetica', 12), bg="#f0f0f0").grid(row=2, column=0, pady=5, padx=10, sticky="w")
entry_num2 = tk.Entry(root, font=('Helvetica', 12))
entry_num2.grid(row=2, column=1, pady=5, padx=10, columnspan=3, sticky="we")

tk.Label(root, text="Select the operation:", font=('Helvetica', 12), bg="#f0f0f0").grid(row=3, column=0, pady=5, padx=10, sticky="w")
operation_var = tk.IntVar()
operation_var.set(1)  # Default to multiplication
operations = [("Multiplication", 1), ("Division", 2), ("Subtraction", 3), ("Exponent", 4)]

for i, (text, value) in enumerate(operations):
    tk.Radiobutton(root, text=text, variable=operation_var, value=value).grid(row=3, column=i+1, padx=10, pady=5, sticky="w")

calculate_button = tk.Button(root, text="Calculate", command=calculate, font=('Helvetica', 12), bg="#4caf50", fg="white", width=15, height=1)
calculate_button.grid(row=4, column=0, columnspan=4, pady=10, padx=10, sticky="we")

result = tk.StringVar()
result.set("Result will be shown here")
result_label = tk.Label(root, textvariable=result, font=('Helvetica', 12), bg="#f0f0f0")
result_label.grid(row=5, column=0, columnspan=4, pady=5, padx=10, sticky="we")

# Add some additional styling to make it more fancy
for widget in [entry_num1, entry_num2, calculate_button, result_label]:
    widget.config(relief="solid", bd=2)

# Start the main loop
root.mainloop()
