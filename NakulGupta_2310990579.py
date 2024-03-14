import tkinter as tk
from tkinter import messagebox
from math import sqrt
from tkinter import ttk

def perform_operation():
    try:
        num1 = float(entry_num1.get())
        operation = operation_var.get()

        if operation != 5:  
            num2 = float(entry_num2.get())
        else:
            num2 = None

        if operation == 1:
            result = num1 * num2
        elif operation == 2:
            result = num1 / num2
        elif operation == 3:
            result = num1 - num2
        elif operation == 4:
            result = num1 + num2
        elif operation == 5:
            result = sqrt(num1)
        else:
            result = "Invalid Operation"

        result_label.config(text=f"Result: {result}", fg="white")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def show_hide_entry():
    if operation_var.get() == 5:  
        label_num1.config(text="Enter the number:", bg="black", fg="white")
    else:
        label_num1.config(text="Enter the first number:", bg="black", fg="white")

    if operation_var.get() == 5:  
        label_num2.config(text="Enter the number:", bg="black", fg="white")
        label_num2.grid_remove()
        entry_num2.grid_remove()
    else:
        label_num2.config(text="Enter the second number:", bg="black", fg="white")
        label_num2.grid()
        entry_num2.grid()

root = tk.Tk()
root.title("Nakul's Calculator")
root.configure(bg="black") 

label_num1 = tk.Label(root, text="Enter the first number:", bg="black", fg="white")  # Set background to black and font color to white
entry_num1 = tk.Entry(root)

label_num2 = tk.Label(root, text="Enter the second number:", bg="black", fg="white")  # Set background to black and font color to white
entry_num2 = tk.Entry(root)

label_operation = tk.Label(root, text="Select the operation:", bg="black", fg="white")  # Set background to black and font color to white
operation_var = tk.IntVar()
operation_var.set(1)

# Style for Rounded Buttons
style = ttk.Style()
style.configure('TButton', foreground='black', background='light grey', borderwidth=0, relief="flat", padding=10)

# Buttons for Operations
button_multiply = ttk.Button(root, text="Multiplication", command=lambda: [operation_var.set(1), show_hide_entry()], style='TButton')
button_divide = ttk.Button(root, text="Division", command=lambda: [operation_var.set(2), show_hide_entry()], style='TButton')
button_subtract = ttk.Button(root, text="Subtraction", command=lambda: [operation_var.set(3), show_hide_entry()], style='TButton')
button_add = ttk.Button(root, text="Addition", command=lambda: [operation_var.set(4), show_hide_entry()], style='TButton')
button_sqrt = ttk.Button(root, text="Square Root", command=lambda: [operation_var.set(5), show_hide_entry()], style='TButton')

# Themed Rounded Button
button_calculate = ttk.Button(root, text="Calculate", command=perform_operation, style='TButton')

result_label = tk.Label(root, text="Result: ", bg="black", fg="white")  # Set background to black and font color to white

label_num1.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
entry_num1.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

label_num2.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
entry_num2.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

label_operation.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

# Buttons placement
button_multiply.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)
button_divide.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)
button_subtract.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)
button_add.grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)
button_sqrt.grid(row=6, column=1, padx=10, pady=5, sticky=tk.W)

button_calculate.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="ew")  # Use sticky="ew" to make the button fit the horizontal space
result_label.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
