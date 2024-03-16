import tkinter as tk
import math

# Create the main window
root = tk.Tk()
root.title("Jeet Calculator")
root.configure(bg="#333333")  # Dark gray background

# Create a text entry box
entry = tk.Entry(root, width=30, borderwidth=0, font=("Arial", 20), bg="#CCCCCC", fg="#333333", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)  # Increase internal padding

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
button_frame = tk.Frame(root, bg="#333333")  # Frame for buttons
button_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

button_1 = tk.Button(button_frame, text="1", padx=40, pady=20, command=lambda: add_to_expression(1), bg="#555555", fg="#000000", font=("Arial", 14))
button_2 = tk.Button(button_frame, text="2", padx=40, pady=20, command=lambda: add_to_expression(2), bg="#555555", fg="#000000", font=("Arial", 14))
button_3 = tk.Button(button_frame, text="3", padx=40, pady=20, command=lambda: add_to_expression(3), bg="#555555", fg="#000000", font=("Arial", 14))
button_4 = tk.Button(button_frame, text="4", padx=40, pady=20, command=lambda: add_to_expression(4), bg="#555555", fg="#000000", font=("Arial", 14))
button_5 = tk.Button(button_frame, text="5", padx=40, pady=20, command=lambda: add_to_expression(5), bg="#555555", fg="#000000", font=("Arial", 14))
button_6 = tk.Button(button_frame, text="6", padx=40, pady=20, command=lambda: add_to_expression(6), bg="#555555", fg="#000000", font=("Arial", 14))
button_7 = tk.Button(button_frame, text="7", padx=40, pady=20, command=lambda: add_to_expression(7), bg="#555555", fg="#000000", font=("Arial", 14))
button_8 = tk.Button(button_frame, text="8", padx=40, pady=20, command=lambda: add_to_expression(8), bg="#555555", fg="#000000", font=("Arial", 14))
button_9 = tk.Button(button_frame, text="9", padx=40, pady=20, command=lambda: add_to_expression(9), bg="#555555", fg="#000000", font=("Arial", 14))
button_0 = tk.Button(button_frame, text="0", padx=40, pady=20, command=lambda: add_to_expression(0), bg="#555555", fg="#000000", font=("Arial", 14))
button_add = tk.Button(button_frame, text="+", padx=39, pady=20, command=lambda: add_to_expression("+"), bg="#FF9500", fg="#000000", font=("Arial", 14))
button_subtract = tk.Button(button_frame, text="-", padx=41, pady=20, command=lambda: add_to_expression("-"), bg="#FF9500", fg="#000000", font=("Arial", 14))
button_multiply = tk.Button(button_frame, text="*", padx=40, pady=20, command=lambda: add_to_expression("*"), bg="#FF9500", fg="#000000", font=("Arial", 14))
button_divide = tk.Button(button_frame, text="/", padx=41, pady=20, command=lambda: add_to_expression("/"), bg="#FF9500", fg="#000000", font=("Arial", 14))
button_equal = tk.Button(button_frame, text="=", padx=91, pady=20, command=evaluate, bg="#00CC00", fg="#000000", font=("Arial", 14))
button_clear = tk.Button(button_frame, text="Clear", padx=79, pady=20, command=clear, bg="#CC0000", fg="#000000", font=("Arial", 14))
button_sqrt = tk.Button(button_frame, text="√", padx=40, pady=20, command=sqrt, bg="#6600CC", fg="#000000", font=("Arial", 14))
button_exp = tk.Button(button_frame, text="e^x", padx=34, pady=20, command=exp, bg="#6600CC", fg="#000000", font=("Arial", 14))
button_log = tk.Button(button_frame, text="ln", padx=40, pady=20, command=log, bg="#6600CC", fg="#000000", font=("Arial", 14))

# Display buttons
button_1.grid(row=0, column=0)
button_2.grid(row=0, column=1)
button_3.grid(row=0, column=2)

button_4.grid(row=1, column=0)
button_5.grid(row=1, column=1)
button_6.grid(row=1, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=3, column=0)
button_clear.grid(row=3, column=1, columnspan=2)
button_add.grid(row=4, column=0)
button_equal.grid(row=4, column=1, columnspan=2)

button_subtract.grid(row=5, column=0)
button_multiply.grid(row=5, column=1)
button_divide.grid(row=5, column=2)

button_sqrt.grid(row=6, column=0)
button_exp.grid(row=6, column=1)
button_log.grid(row=6, column=2)

# Run the main loop
root.mainloop()
