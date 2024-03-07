import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")

        self.result_var = tk.StringVar()
        self.result_var.set("")

        # Entry field to display results
        self.result_entry = tk.Entry(root, textvariable=self.result_var, font=('Helvetica', 20), bd=5, insertwidth=4, width=15, justify='right')
        self.result_entry.grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('√', 5, 0), ('C', 5, 1)
        ]

        for (text, row, col) in buttons:
            b = tk.Button(root, text=text, font=('Helvetica', 14), command=lambda t=text: self.on_button_click(t))
            b.grid(row=row, column=col, sticky='nsew')

    def on_button_click(self, char):
        if char == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Expression")
        elif char == 'C':
            self.result_var.set("")
        elif char == '√':
            try:
                value = float(self.result_var.get())
                if value < 0:
                    messagebox.showerror("Error", "Cannot compute square root of a negative number")
                else:
                    result = math.sqrt(value)
                    self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Expression")
        else:
            self.result_var.set(self.result_var.get() + char)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
