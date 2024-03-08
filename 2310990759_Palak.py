import tkinter as tk
from math import sqrt, sin, cos, tan, radians

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.result_var = tk.StringVar()

        entry = tk.Entry(root, textvariable=self.result_var, font=('Helvetica', 18), justify='right', bd=10, relief='ridge')
        entry.grid(row=0, column=0, columnspan=6, sticky='nsew')

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'sqrt', 'sin', 'cos', 'tan', 'C'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(root, text=button, command=lambda b=button: self.button_click(b)).grid(row=row_val, column=col_val, sticky='nsew', padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
            root.grid_rowconfigure(i + 1, weight=1)

        self.set_button_color('sqrt', 'orange')
        self.set_button_color('sin', 'lightblue')
        self.set_button_color('cos', 'lightgreen')
        self.set_button_color('tan', 'lightcoral')

    def set_button_color(self, button_text, color):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button) and widget.cget('text') == button_text:
                widget.configure(bg=color)

    def button_click(self, button):
        current_text = self.result_var.get()

        if button == 'C':
            self.result_var.set('')
        elif button == '=':
            try:
                result = eval(current_text)
                self.result_var.set(result)
            except:
                self.result_var.set('Error')
        elif button == 'sqrt':
            try:
                result = sqrt(eval(current_text))
                self.result_var.set(result)
            except:
                self.result_var.set('Error')
        elif button in ['sin', 'cos', 'tan']:
            try:
                angle_in_deg = eval(current_text)
                if button == 'sin':
                    result = sin(radians(angle_in_deg))
                elif button == 'cos':
                    result = cos(radians(angle_in_deg))
                elif button == 'tan':
                    result = tan(radians(angle_in_deg))
                self.result_var.set(result)
            except:
                self.result_var.set('Error')
        else:
            self.result_var.set(current_text + button)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

