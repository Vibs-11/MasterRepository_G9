
import tkinter as tk
from tkinter import messagebox
import math
print("Hello! welcome to the Calculator World")

print("BY default all are selected ,so select any one operation")
def perform_operation():
    try:
        operation = int(operation_var.get())
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        
        if operation == 1:
            result = num1 * num2
        elif operation == 2:
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed")
                return
            result = num1 / num2
        elif operation == 3:
            result = num1 - num2
        elif operation == 4:
            result = num1 + num2
        elif operation == 5:
            result = num1 ** num2
        elif operation == 6:
            result = math.sqrt(num1)
        elif operation == 7:
            result = math.sqrt(num2)
        elif operation == 8:
            result = num1 ** 2
        elif operation == 9:
            result = num2 ** 2
        elif operation == 10:
            result = math.factorial(int(num1))
        elif operation == 11:
            result = math.factorial(int(num2))
        elif operation == 12:
            result = math.sin(num1)
        elif operation == 13:
            result = math.sin(num2)
        elif operation == 14:
            result = math.cos(num1)
        elif operation == 15:
            result = math.cos(num2)
        elif operation == 16:
            result = math.tan(num1)
        elif operation == 17:
            result = math.tan(num2)
        elif operator == 18:
            result=1/math.cos(num1)
        elif operator ==19:
            result=1/math.cos(num2)
        else:
            messagebox.showerror("Error", "Invalid operation selected")
            return

        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

root = tk.Tk()
root.title("Calculator")

operation_var = tk.StringVar()

tk.Label(root, text="Select Operation:").pack()

operation_options = [
    "Multiplication", "Division", "Subtraction", "Addition", "Exponentiation",
    "Square Root (1st Number)", "Square Root (2nd Number)", "Square (1st Number)",
    "Square (2nd Number)", "Factorial (1st Number)", "Factorial (2nd Number)",
    "Sine (1st Number)", "Sine (2nd Number)", "Cosine (1st Number)", "Cosine (2nd Number)",
    "Tangent (1st Number)", "Tangent (2nd Number)","Sec (1st Number)","Sec (2nd Number)"
]

for idx, option in enumerate(operation_options, start=1):
    tk.Radiobutton(root, text=option, variable=operation_var, value=str(idx)).pack(anchor=tk.W)

tk.Label(root, text="Enter First Number:").pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

tk.Label(root, text="Enter Second Number:").pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

perform_button = tk.Button(root, text="Perform Operation", command=perform_operation)
perform_button.pack()

result_label = tk.Label(root)
result_label.pack()

root.mainloop()
 

