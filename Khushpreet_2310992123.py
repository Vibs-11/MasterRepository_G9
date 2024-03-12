import tkinter as tk
import math

def button_click(symbol):
    current = display.get()
    if current == 'Error':
        display.delete(0, tk.END)
        current = ''
    display.delete(0, tk.END)
    display.insert(tk.END, current + symbol)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, 'Error')

def clear():
    display.delete(0, tk.END)

def sin():
    try:
        result = math.sin(math.radians(float(display.get())))
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, 'Error')

def cos():
    try:
        result = math.cos(math.radians(float(display.get())))
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, 'Error')

def tan():
    try:
        result = math.tan(math.radians(float(display.get())))
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, 'Error')

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create the display
display = tk.Entry(root, width=30, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('sin', 1, 4), ('cos', 2, 4), ('tan', 3, 4),
]

# Add buttons to the window
for (text, row, column) in buttons:
    if text in ('sin', 'cos', 'tan'):
        button = tk.Button(root, text=text, padx=10, pady=10)
        if text == 'sin':
            button.config(command=sin)
        elif text == 'cos':
            button.config(command=cos)
        elif text == 'tan':
            button.config(command=tan)
    else:
        button = tk.Button(root, text=text, padx=20, pady=10, command=lambda t=text: button_click(t))
    button.grid(row=row, column=column, padx=5, pady=5)

# Add clear button
clear_button = tk.Button(root, text="Clear", padx=20, pady=10, command=clear)
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Run the main loop
root.mainloop()
