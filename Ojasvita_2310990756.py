import math
import tkinter as tk
from tkinter import messagebox

def calculate_operation(operation):
    try:
        num1 = float(entry1.get())
        if operation != "Square Root" and operation != "Cube Root":
            num2 = float(entry2.get())
            if operation == "Multiplication":
                result = num1 * num2
                output_text.insert(tk.END, "Multiplication of the two nos. is :: " + str(result) + "\n")
            elif operation == "Division":
                if num2 == 0:
                    messagebox.showerror("Error", "Cannot divide by zero!")
                else:
                    result = num1 / num2
                    output_text.insert(tk.END, "Division of the two nos. is :: " + str(result) + "\n")
            elif operation == "Subtraction":
                result = num1 - num2
                output_text.insert(tk.END, "Subtraction of the two nos. is :: " + str(result) + "\n")
            elif operation == "Addition":
                result = num1 + num2
                output_text.insert(tk.END, "Addition of the two nos. is :: " + str(result) + "\n")
            elif operation == "Exponent":
                result = num1 ** num2
                output_text.insert(tk.END, "Exponent of the two nos. is :: " + str(result) + "\n")
            elif operation == "Logarithm":
                if num1 <= 0 or num1 == 1 or num2 <= 0:
                    messagebox.showerror("Error", "Invalid input! Base and number should be greater than 0 and base should not be equal to 1.")
                else:
                    result = math.log(num1, num2)
                    output_text.insert(tk.END, "Logarithm of the first number with base second number is :: " + str(result) + "\n")
        else:
            if operation == "Square Root":
                if num1 < 0:
                    messagebox.showerror("Error", "Invalid input! Cannot find square root of a negative number.")
                elif entry2.get() != "":
                    messagebox.showerror("Error", "Invalid input! Square root operation requires only one number.")
                else:
                    result = math.sqrt(num1)
                    output_text.insert(tk.END, "Square root of the number is :: " + str(result) + "\n")
            elif operation == "Cube Root":
                if entry2.get() != "":
                    messagebox.showerror("Error", "Invalid input! Cube root operation requires only one number.")
                else:
                    result = num1 ** (1/3)
                    output_text.insert(tk.END, "Cube root of the number is :: " + str(result) + "\n")
    except ValueError:
        messagebox.showerror("Error", "Invalid input!")

root = tk.Tk()
root.title("Calculator")
root.configure(bg="#add8e6")  

label_font = ("Helvetica", 12)

dropdown_label = tk.Label(root, text="Operations:", bg="#add8e6", font=label_font)
dropdown_label.grid(row=2, column=0, pady=10)

options = [
    "Options",
    "Multiplication",
    "Division",
    "Subtraction",
    "Addition",
    "Exponent",
    "Logarithm",
    "Square Root",
    "Cube Root"
]

selected_operation = tk.StringVar()
selected_operation.set(options[0])  

operation_menu = tk.OptionMenu(root, selected_operation, *options[1:], command=lambda operation: calculate_operation(operation))
operation_menu.config(bg="white", fg="black", font=label_font)
operation_menu.grid(row=2, column=1, pady=10)

output_text = tk.Text(root, height=5, width=50, bg="white", fg="black")
output_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

label1 = tk.Label(root, text="Number 1:", bg="#add8e6", font=label_font)
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Number 2:", bg="#add8e6", font=label_font)
label2.grid(row=1, column=0)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

root.mainloop()
