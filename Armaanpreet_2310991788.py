import tkinter as tk
from math import sqrt, pow, sin, cos, tan, log

def perform_operation():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()

    if operation == 1:
        result.set(num1 * num2)
    elif operation == 2:
        result.set(num1 / num2)
    elif operation == 3:
        result.set(num1 - num2)
    elif operation == 4:
        result.set(pow(num1, num2))

def perform_scientific_operation():
    num = float(entry_num1.get())
    scientific_operation = scientific_operation_var.get()

    if scientific_operation == 'sqrt':
        result.set(sqrt(num))
    elif scientific_operation == 'sin':
        result.set(sin(num))
    elif scientific_operation == 'cos':
        result.set(cos(num))
    elif scientific_operation == 'tan':
        result.set(tan(num))
    elif scientific_operation == 'log':
        result.set(log(num))

# Create the main window
window = tk.Tk()
window.title("Scientific Calculator")

# Create variables
operation_var = tk.IntVar()
scientific_operation_var = tk.StringVar()
result = tk.StringVar()

# Create GUI components
label_num1 = tk.Label(window, text="Enter the first number:")
entry_num1 = tk.Entry(window)
label_num2 = tk.Label(window, text="Enter the second number:")
entry_num2 = tk.Entry(window)

label_operation = tk.Label(window, text="Select operation:")
radio_multiply = tk.Radiobutton(window, text="Multiplication", variable=operation_var, value=1)
radio_divide = tk.Radiobutton(window, text="Division", variable=operation_var, value=2)
radio_subtract = tk.Radiobutton(window, text="Subtraction", variable=operation_var, value=3)
radio_exponent = tk.Radiobutton(window, text="Exponent", variable=operation_var, value=4)

btn_calculate = tk.Button(window, text="Calculate", command=perform_operation)


label_scientific = tk.Label(window, text="Scientific Operations:")
combo_scientific = tk.OptionMenu(window, scientific_operation_var, 'sqrt', 'sin', 'cos', 'tan', 'log')
btn_scientific_calculate = tk.Button(window, text="Calculate Scientific", command=perform_scientific_operation)

label_result = tk.Label(window, text="Result:")
entry_result = tk.Entry(window, textvariable=result, state='readonly')


label_num1.pack()
entry_num1.pack()
label_num2.pack()
entry_num2.pack()

label_operation.pack()
radio_multiply.pack()
radio_divide.pack()
radio_subtract.pack()
radio_exponent.pack()

btn_calculate.pack()

label_scientific.pack()
combo_scientific.pack()
btn_scientific_calculate.pack()

label_result.pack()
entry_result.pack()


window.mainloop()
