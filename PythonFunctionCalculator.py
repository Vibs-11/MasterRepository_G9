import tkinter as tk
import math

class ScientificCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scientific Calculator")
        self.geometry("325x447")
        self.resizable(False, False)  # Disable resizing
        self.configure(bg="#1a1a1a")  # Set dark mode background color
        self.display = tk.Entry(self, font=("Arial", 20), justify="right", bg="#333333", fg="white")  # Set dark mode color for display
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")
        self.create_buttons()
        self.functions = {
            "sqrt": math.sqrt,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log10,
            "ln": math.log,
            "factorial": math.factorial
        }
        self.last_function = None

    def create_buttons(self):
        buttons = [
            "C", "DEL", "sqrt", "/", "(",
            "7", "8", "9", "*", ")",
            "4", "5", "6", "-", "^",
            "1", "2", "3", "+", "!",
            "0", ".", "±", "=", "sin",
            "cos", "tan", "log", "ln",
            "π"
        ]
        row = 1
        col = 0
        for button_text in buttons:
            button = tk.Button(self, text=button_text, width=4, height=2, font=("Arial", 14),
                               command=lambda x=button_text: self.button_click(x), bg="#404040", fg="white")  # Set dark mode colors for buttons
            button.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
            col += 1
            if col > 4:
                col = 0
                row += 1

    def button_click(self, button_text):
        if button_text == "C":
            self.display.delete(0, tk.END)
            self.last_function = None
        elif button_text == "DEL":
            self.display.delete(len(self.display.get()) - 1)
            if self.display.get().endswith("("):
                self.last_function = None
        elif button_text in self.functions:
            if self.display.get():
                try:
                    result = self.functions[button_text](float(self.display.get()))
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, result)
                except ValueError:
                    self.display.insert(tk.END, f"{self.functions[button_text]}(")
            else:
                self.display.insert(tk.END, f"{self.functions[button_text]}(")
            self.last_function = self.functions[button_text]
        elif button_text == "π":
            self.display.insert(tk.END, str(math.pi))
        elif button_text == "±":
            self.display.insert(tk.END, "-")
        elif button_text == "^":
            self.display.insert(tk.END, "**")
        elif button_text == "=":
            try:
                expression = self.display.get()
                for func_name, func in self.functions.items():
                    expression = expression.replace(f"{func_name}(", f"{func}(")
                result = str(eval(expression))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
                self.last_function = None
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, button_text)

if __name__ == "__main__":
    calculator = ScientificCalculator()
    calculator.mainloop()
