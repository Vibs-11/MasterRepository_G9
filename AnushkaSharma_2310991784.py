import tkinter as tk
import math

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("300x400")

        self.expression = ""
        self.memory = 0

        self.entry = tk.Entry(master, width=30, font=("Arial", 14))
        self.entry.grid(row=0, column=0, columnspan=5)

        buttons = [
            ('7', '8', '9', '/', 'sin'),
            ('4', '5', '6', '*', 'cos'),
            ('1', '2', '3', '-', 'tan'),
            ('0', '.', '=', '+', 'C'),
            ('M+', 'M-', 'MR', 'MC', '')
        ]

        for i in range(len(buttons)):
            for j in range(len(buttons[i])):
                btn = tk.Button(master, text=buttons[i][j], width=5, height=2,
                                command=lambda x=buttons[i][j]: self.button_click(x))
                btn.grid(row=i + 1, column=j, sticky="nsew")

    def button_click(self, symbol):
        if symbol == '=':
            try:
                self.expression = str(eval(self.expression))
                self.update_display()
            except:
                self.expression = "Error"
                self.update_display()
        elif symbol == 'C':
            self.expression = ""
            self.update_display()
        elif symbol == 'M+':
            try:
                self.memory += float(self.expression)
                self.update_display()
            except:
                self.expression = "Error"
                self.update_display()
        elif symbol == 'M-':
            try:
                self.memory -= float(self.expression)
                self.update_display()
            except:
                self.expression = "Error"
                self.update_display()
        elif symbol == 'MR':
            self.expression = str(self.memory)
            self.update_display()
        elif symbol == 'MC':
            self.memory = 0
            self.update_display()
        elif symbol in ['sin', 'cos', 'tan']:
            try:
                if symbol == 'sin':
                    self.expression = str(math.sin(float(self.expression)))
                elif symbol == 'cos':
                    self.expression = str(math.cos(float(self.expression)))
                elif symbol == 'tan':
                    self.expression = str(math.tan(float(self.expression)))
                self.update_display()
            except:
                self.expression = "Error"
                self.update_display()
        else:
            self.expression += symbol
            self.update_display()

    def update_display(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

root = tk.Tk()
app = CalculatorApp(root)
root.mainloop()
