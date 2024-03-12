import tkinter as tk

def evaluate_expression():
    try:
        result.set(eval(entry.get()))
    except Exception as e:
        result.set("Error")

def clear_entry():
    entry.delete(0, tk.END)

def append_to_entry(value):
    current_entry = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_entry + value)

def create_button(root, text, command, row, column, colspan=1):
    button = tk.Button(root, text=text, command=command, padx=10, pady=5)
    button.grid(row=row, column=column, columnspan=colspan, padx=5, pady=5, sticky="nsew")

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

result = tk.StringVar()
result.set("")

result_label = tk.Label(root, textvariable=result, width=30, anchor="e", borderwidth=5)
result_label.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', lambda: append_to_entry('7')),
    ('8', lambda: append_to_entry('8')),
    ('9', lambda: append_to_entry('9')),
    ('/', lambda: append_to_entry('/')),
    ('4', lambda: append_to_entry('4')),
    ('5', lambda: append_to_entry('5')),
    ('6', lambda: append_to_entry('6')),
    ('*', lambda: append_to_entry('*')),
    ('1', lambda: append_to_entry('1')),
    ('2', lambda: append_to_entry('2')),
    ('3', lambda: append_to_entry('3')),
    ('-', lambda: append_to_entry('-')),
    ('C', clear_entry),
    ('0', lambda: append_to_entry('0')),
    ('=', evaluate_expression),
    ('+', lambda: append_to_entry('+')),
]

for i, (text, command) in enumerate(buttons):
    row = i // 4 + 2
    column = i % 4
    create_button(root, text, command, row, column)

root.mainloop()
