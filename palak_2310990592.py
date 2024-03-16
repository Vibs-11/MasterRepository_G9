import tkinter as tk
import math

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")

# Entry widget to display input and results
entry = tk.Entry(root, width=80, borderwidth=5)
entry.grid(row=0, column=0, columnspan=6)

# Function to update the entry widget
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

# Function to delete the last character
def delete_last():
    current = entry.get()[:-1]  # Get the current entry text excluding the last character
    entry.delete(0, tk.END)
    entry.insert(0, current)

# Function to evaluate the expression and display result
def eval_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the entry widget
def clear_entry():
    entry.delete(0, tk.END)

# Function for trigonometric functions
def trig_function(func):
    try:
        if func == 'sin':
            result = math.sin(math.radians(float(entry.get())))
        elif func == 'cos':
            result = math.cos(math.radians(float(entry.get())))
        elif func == 'tan':
            result = math.tan(math.radians(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function for inverse trigonometric functions
def inverse_trig_function(func):
    try:
        if func == 'sin':
            result = math.asin(float(entry.get()))
        elif func == 'cos':
            result = math.acos(float(entry.get()))
        elif func == 'tan':
            result = math.atan(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, math.degrees(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function for other functions like square, exponentiation, factorial, logarithm, and x raised to y
def other_function(func):
    try:
        if func == 'square':
            result = float(entry.get()) ** 2
        elif func == 'exp':
            result = math.exp(float(entry.get()))
        elif func == 'pi':
            result = math.pi
        elif func == 'factorial':
            result = math.factorial(int(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(0, result)
            return
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create buttons for numbers, operations, and functions
buttons = [
    'C', '(', ')', '/','*', '-',
    '7', '8','9', '+', 'square', 'pi',
    '4', '5', '6','sin','cos', 'tan',
    '1', '2','3', 'factorial','exp', 'DEL',
    '0', '.', '='
]

row = 1
col = 0

sin_cos_tan_var = tk.StringVar()
sin_cos_tan_var.set('sin')  # Default to sin function

button_width = 25
button_height = 5

# Creating a grid layout with four buttons in each row
for button in buttons:
    if col == 6:
        col = 0
        row += 1

    if button == 'DEL':
        # Create a frame to group the delete button
        frame = tk.Frame(root)
        frame.grid(row=row, column=col)
        
        # Create delete button inside the frame
        delete_button = tk.Button(frame, text=button, command=delete_last, padx=button_width, pady=button_height)
        delete_button.pack()
    elif button in ['=', 'C']:
        tk.Button(root, text=button, command=lambda b=button: eval_expression() if b == '=' else clear_entry(), padx=button_width, pady=button_height).grid(row=row, column=col)
    elif button in ['sin', 'cos', 'tan']:
        tk.Button(root, text=button, command=lambda b=button: trig_function(b), padx=button_width, pady=button_height).grid(row=row, column=col)
    elif button in ['square', 'exp', 'pi', 'factorial', 'log', 'x^y', 'inv']:
        tk.Button(root, text=button, command=lambda b=button: other_function(b), padx=button_width, pady=button_height).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, command=lambda num=button: button_click(num), padx=button_width, pady=button_height).grid(row=row, column=col)

    col += 1

root.mainloop()
