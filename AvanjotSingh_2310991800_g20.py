import tkinter as tk

def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


def button_click(symbol):
    entry.insert(tk.END, symbol)


root = tk.Tk()
root.title("Simple Calculator")


entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for symbol, row, col in buttons:
    if symbol == '=':
        button = tk.Button(root, text=symbol, padx=40, pady=20, command=evaluate_expression)
    else:
        button = tk.Button(root, text=symbol, padx=40, pady=20, command=lambda s=symbol: button_click(s))
    button.grid(row=row, column=col)

root.mainloop()
