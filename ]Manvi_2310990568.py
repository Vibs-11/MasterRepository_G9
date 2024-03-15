import tkinter as tk

# Function to evaluate the expression and display result
def evaluate_expression():
    try:
        result.set(eval(entry.get()))
    except:
        result.set("Error")

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Function to clear the result field
def clear_result():
    result.set("")

# Function to add a character to the entry field
def add_to_entry(char):
    entry.insert(tk.END, char)

# Function to create and configure buttons
def create_button(root, text, row, column, command=None):
    button = tk.Button(root, text=text, padx=10, pady=5, command=command)
    button.grid(row=row, column=column, padx=5, pady=5)
    return button

# Main tkinter window
root = tk.Tk()
root.title("Calculator")

# Entry field for expression
entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Result field
result = tk.StringVar()
result.set("")
result_label = tk.Label(root, textvariable=result, width=30, borderwidth=5, relief=tk.SUNKEN, anchor="e")
result_label.grid(row=1, column=0, columnspan=4, padx=10, pady=5)

# Buttons
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
]

for (text, row, column) in buttons:
    create_button(root, text, row, column, lambda text=text: add_to_entry(text))

# Clear and evaluate buttons
create_button(root, "Clear", 6, 0, clear_entry)
create_button(root, "Clear All", 6, 1, clear_result)
create_button(root, "Evaluate", 6, 2, evaluate_expression)

root.mainloop()
