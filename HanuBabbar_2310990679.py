import tkinter as tk
from tkinter import messagebox

# Function to perform calculation
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == 1:
            result = num1 * num2
            result_label.config(text=f"Result: {result}", fg="white")
        elif operation == 2:
            if num2 != 0:
                result = num1 / num2
                result_label.config(text=f"Result: {result}", fg="white")
            else:
                messagebox.showerror("Error", "Division by zero is not allowed.")
        elif operation == 3:
            result = num1 - num2
            result_label.config(text=f"Result: {result}", fg="white")
        elif operation == 4:
            result = num1 ** num2
            result_label.config(text=f"Result: {result}", fg="white")
        else:
            result = num1 + num2
            result_label.config(text=f"Result: {result}", fg="white")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create main window
window = tk.Tk()
window.title("Calculator by Hanu")
window.configure(bg="#333")

# Create labels for input fields
label_num1 = tk.Label(window, text="Enter number 1:", font=("Arial", 12), fg="white", bg="#333")
label_num1.pack(pady=(10, 0))

entry_num1 = tk.Entry(window, width=20, font=("Arial", 12))
entry_num1.pack(pady=5)

label_num2 = tk.Label(window, text="Enter number 2:", font=("Arial", 12), fg="white", bg="#333")
label_num2.pack()

entry_num2 = tk.Entry(window, width=20, font=("Arial", 12))
entry_num2.pack(pady=5)

# Create radio buttons for operations
operation_var = tk.IntVar()
operation_var.set(1)

operations_frame = tk.Frame(window, bg="#333")
operations_frame.pack()

operations = [("Multiply", 1), ("Divide", 2), ("Subtract", 3), ("Exponent", 4), ("Add", 5)]

for text, value in operations:
    radio_btn = tk.Radiobutton(operations_frame, text=text, variable=operation_var, value=value, font=("Arial", 12), fg="white", bg="#333", selectcolor="#222")
    radio_btn.pack(side="left", padx=5, pady=5)

# Create button to perform calculation
calculate_button = tk.Button(window, text="Calculate", command=calculate, width=10, font=("Arial", 12))
calculate_button.pack(pady=10)

# Create label to display result
result_label = tk.Label(window, text="", font=("Arial", 14), fg="white", bg="#333")
result_label.pack()

# Run the GUI
window.mainloop()
