import tkinter as tk

def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + symbol)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create an entry widget to display input/output
entry = tk.Entry(window, width=30, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create and place the buttonsss
row = 1
col = 0
for button in buttons:
    if button == '=':
        tk.Button(window, text=button, width=8, height=2, command=calculate).grid(row=row, column=col, padx=5, pady=5)
    elif button == 'C':
        tk.Button(window, text=button, width=8, height=2, command=clear).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(window, text=button, width=8, height=2, command=lambda button=button: button_click(button)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the application
window.mainloop()