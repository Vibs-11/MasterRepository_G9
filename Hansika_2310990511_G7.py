import tkinter as tk
import math

# Create the main window
root = tk.Tk()
root.title("Hanshika Calculator")

# Create a text entry box
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Initialize the expression as an empty string
expression = ""

# Function to update the expression
def add_to_expression(value):
    global expression
    expression += str(value)
    entry.delete(0, tk.END)
    entry.insert(0, expression)

# Function to evaluate the expression
def evaluate():
    global expression
    try:
        result = str(eval(expression))
        expression = result
    except:
        result = "Error"
    finally:
        entry.delete(0, tk.END)
        entry.insert(0, result)

# Function to clear the expression
def clear():
    global expression
    expression = ""
    entry.delete(0, tk.END)

# Function to handle square root
def sqrt():
    global expression
    try:
        result = str(math.sqrt(float(expression)))
        expression = result
    except ValueError:
        result = "Error"
    finally:
        entry.delete(0, tk.END)
        entry.insert(0, result)

# Function to handle exponent
def exp():
    global expression
    try:
        result = str(math.exp(float(expression)))
        expression = result
    except ValueError:
        result = "Error"
    finally:
        entry.delete(0, tk.END)
        entry.insert(0, result)

# Function to handle logarithm
def log():
    global expression
    try:
        result = str(math.log(float(expression)))
        expression = result
    except ValueError:
        result = "Error"
    finally:
        entry.delete(0, tk.END)
        entry.insert(0, result)

# Create buttons
button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: add_to_expression(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: add_to_expression(2))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: add_to_expression(3))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: add_to_expression(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: add_to_expression(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: add_to_expression(6))
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: add_to_expression(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: add_to_expression(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: add_to_expression(9))
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: add_to_expression(0))
button_add = tk.Button(root, text="+", padx=39, pady=20, command=lambda: add_to_expression("+"))
button_subtract = tk.Button(root, text="-", padx=41, pady=20, command=lambda: add_to_expression("-"))
button_multiply = tk.Button(root, text="*", padx=40, pady=20, command=lambda: add_to_expression("*"))
button_divide = tk.Button(root, text="/", padx=41, pady=20, command=lambda: add_to_expression("/"))
button_equal = tk.Button(root, text="=", padx=91, pady=20, command=evaluate)
button_clear = tk.Button(root, text="Clear", padx=79, pady=20, command=clear)
button_sqrt = tk.Button(root, text="√", padx=40, pady=20, command=sqrt)
button_exp = tk.Button(root, text="e^x", padx=34, pady=20, command=exp)
button_log = tk.Button(root, text="ln", padx=40, pady=20, command=log)

# Display buttons
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

button_sqrt.grid(row=7, column=0)
button_exp.grid(row=7, column=1)
button_log.grid(row=7, column=2)

# Run the main loop
root.mainloop()
