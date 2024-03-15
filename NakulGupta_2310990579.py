import tkinter as tk
import math

# Function to update the display
def update_display(value):
    display_var.set(value)

# Function to perform arithmetic operation
def calculate():
    try:
        result = eval(display_var.get())
        update_display(result)
    except:
        update_display("Error")

# Function to clear the display
def clear_display():
    update_display("")

# Function to calculate square root
def calculate_sqrt():
    try:
        result = math.sqrt(float(display_var.get()))
        update_display(result)
    except:
        update_display("Error")

# Function to add exponentiation
def calculate_power():
    try:
        result = eval(display_var.get()) ** 2
        update_display(result)
    except:
        update_display("Error")

# Function to add factorial
def calculate_factorial():
    try:
        result = math.factorial(int(display_var.get()))
        update_display(result)
    except:
        update_display("Error")

# Function to add pi value
def add_pi():
    display_var.set(display_var.get() + str(math.pi))

# Function to calculate result when equals button is pressed
def calculate_result():
    calculate()


root = tk.Tk()
root.title("Nakul's Calculator")
root.configure(bg='black')


display_var = tk.StringVar()


display = tk.Entry(root, textvariable=display_var, font=("Arial", 20), bg='black', fg='white', bd=0, justify="right")
display.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Buttons for digits and operations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 3)
]

for (text, row, column) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 20), bg='grey', fg='blue', bd=2, relief="ridge",
                       command=lambda t=text: display_var.set(display_var.get() + t))
    button.grid(row=row, column=column, sticky="nsew")

# Additional scientific calculator buttons
extra_buttons = [
    ('C', clear_display, 1, 4), ('√', calculate_sqrt, 2, 4), ('x^2', calculate_power, 3, 4),
    ('n!', calculate_factorial, 4, 4), ('π', add_pi, 0, 4), ('=', calculate_result, 4, 2)
]

for (text, command, row, column) in extra_buttons:
    button = tk.Button(root, text=text, font=("Arial", 20), bg='grey', fg='blue', bd=2, relief="ridge",
                       command=command)
    button.grid(row=row, column=column, sticky="nsew")

# Configure row and column weights
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(5):
    root.grid_columnconfigure(i, weight=1)


root.mainloop()
