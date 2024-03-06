import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Graphical Calculator")

        self.result_var = tk.StringVar()
        self.result_var.set("")

        self.result_label = tk.Label(master, textvariable=self.result_var, font=("Arial", 14))
        self.result_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('(', 5, 1), (')', 5, 2), ('^', 5, 3)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(master, text=text, font=("Arial", 14), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column, sticky="nsew")

    def on_button_click(self, text):
        if text == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(str(result))
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif text == 'C':
            self.result_var.set("")
        else:
            self.result_var.set(self.result_var.get() + text)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
