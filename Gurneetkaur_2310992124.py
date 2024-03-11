import tkinter as tk

def add_digit(digit):
    value = calc_entry.get() + str(digit)
    calc_entry.delete(0, tk.END)
    calc_entry.insert(0, value)

def add_operation(operation):
    value = calc_entry.get() + operation
    calc_entry.delete(0, tk.END)
    calc_entry.insert(0, value)

def calculate():
    value = calc_entry.get()
    if value[-1] in '+-*/':
        value = value+value[:-1]
    calc_entry.delete(0, tk.END)
    calc_entry.insert(0, eval(value))

def clear_entry():
    calc_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")

calc_entry = tk.Entry(root, width=15, borderwidth=5)
calc_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1), ('+', 1, 3), ('-', 2, 3),
    ('*', 3, 3), ('/', 4, 3),
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: add_digit(t))
    button.grid(row=row, column=col)

tk.Button(root, text='C', padx=20, pady=20, command=clear_entry).grid(row=4, column=0)
tk.Button(root, text='=', padx=20, pady=20, command=calculate).grid(row=4, column=2)

root.mainloop()