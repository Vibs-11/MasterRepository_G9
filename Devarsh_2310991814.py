import tkinter as tk
import math

def evaluate(event):
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear(event):
    entry.delete(0, tk.END)

def add_to_display(character):
    entry.insert(tk.END, character)

def square_root():
    try:
        num = float(entry.get())
        if num < 0:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
        else:
            result = math.sqrt(num)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Scientific Calculator")

entry = tk.Entry(root, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('sin', 1, 4), ('cos', 2, 4), ('tan', 3, 4), ('^', 4, 4),
    ('(', 5, 0), (')', 5, 1), ('√', 5, 2), ('clr', 5, 3)
]

for (text, row, column) in buttons:
    button = tk.Button(root, text=text, font=('Arial', 12))
    button.grid(row=row, column=column, padx=5, pady=5)
    button.bind('<Button-1>', lambda e, t=text: add_to_display(t))
    if text == '=':
        button.bind('<Button-1>', evaluate)
    elif text == 'clr':
        button.bind('<Button-1>', clear)
    elif text == '√':
        button.bind('<Button-1>', lambda e: square_root())

root.mainloop()
