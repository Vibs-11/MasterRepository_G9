import tkinter as tk

def button_click(symbol):
    current = display_var.get()
    if current == "Error":
        clear_display()
        current = ""
    if symbol == "=":
        try:
            result = eval(current)
            display_var.set(result)
        except:
            display_var.set("Error")
    elif symbol == "C":
        clear_display()
    else:
        display_var.set(current + symbol)

def clear_display():
    display_var.set("")

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.configure(bg='black')

# Create and configure the display
display_var = tk.StringVar()
display_var.set("")
display = tk.Label(root, textvariable=display_var, font=('Arial', 18), bg='black', fg='white', width=20)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define the button symbols and their positions
button_symbols = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

# Create and place the buttons
for symbol, row, col in button_symbols:
    button = tk.Button(root, text=symbol, font=('Arial', 14), bg='black', fg='white', width=5, height=2, command=lambda sym=symbol: button_click(sym))
    button.grid(row=row, column=col, padx=5, pady=5)

# Start the main event loop
root.mainloop()
