import tkinter as tk
from math import sqrt

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation.get() == "Addition":
            result.set(num1 + num2)

        elif operation.get() == "Subtraction":
            result.set(num1 - num2)

        elif operation.get() == "Multiplication":
            result.set(num1 * num2)

        elif operation.get() == "Division":
            if num2 != 0:
                result.set(num1 / num2)
            else:
                result.set("Error: Cannot divide by zero.")

        elif operation.get() == "Square Root":
            result.set(sqrt(num1))

        elif operation.get() == "Exponent":
            result.set(num1 ** num2)

    except ValueError:
        result.set("Error: Invalid input")


window = tk.Tk()
window.title("Simple Calculator")


entry1 = tk.Entry(window)
entry1.grid(row=0, column=0, padx=10, pady=10)

entry2 = tk.Entry(window)
entry2.grid(row=0, column=1, padx=10, pady=10)


operations = ["Addition", "Subtraction", "Multiplication", "Division", "Square Root", "Exponent"]
operation = tk.StringVar()
operation.set(operations[0])

dropdown = tk.OptionMenu(window, operation, *operations)
dropdown.grid(row=1, column=0, columnspan=2, pady=10)


calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)


result = tk.StringVar()
result_label = tk.Label(window, textvariable=result)
result_label.grid(row=3, column=0, columnspan=2, pady=10)

window.mainloop()
