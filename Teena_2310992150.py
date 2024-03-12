import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        # Entry widget to display the input and results
        self.display = tk.Entry(root, width=20, font=('Arial', 16), justify="right")
        self.display.grid(row=0, column=0, columnspan=4)

        # Buttons for digits and operations
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '+', '=', 'C',
            '//', '%'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(root, text=button, width=5, height=2, command=lambda b=button: self.button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def button_click(self, value):
        current_text = self.display.get()

        if value == '=':
            try:
                result = eval(current_text)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif value == 'C':
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, value)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
