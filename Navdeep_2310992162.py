import tkinter as tk
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("300x400")
        self.config(bg="#f0f0f0")  # Background color
        
        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.create_widgets()

    def create_widgets(self):
        # Entry for displaying the result
        self.result_entry = tk.Entry(self, textvariable=self.result_var, font=('Helvetica', 20), bd=0, insertwidth=4, width=15, justify='right', relief=tk.FLAT)
        self.result_entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

        # Buttons
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("sin", 5, 0), ("cos", 5, 1), ("tan", 5, 2), ("sqrt", 5, 3),
            ("π", 6, 0), ("(", 6, 1), (")", 6, 2), ("C", 6, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self, text=text, font=('Helvetica', 15), command=lambda t=text: self.on_button_click(t), bg="#009688", fg="#ffffff", bd=1, padx=10, pady=10, relief=tk.RAISED, highlightthickness=0)
            button.grid(row=row, column=col, sticky='nsew')

        # Adjust row and column weights
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
            self.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == "=":
            try:
                result = eval(self.result_var.get())
                self.result_var.set(str(result))
            except Exception as e:
                self.result_var.set("Error")
        elif char == "C":
            self.result_var.set("0")
        elif char == "π":
            self.result_var.set(str(math.pi))
        elif char == "sin":
            try:
                result = math.sin(eval(self.result_var.get()))
                self.result_var.set(str(result))
            except Exception as e:
                self.result_var.set("Error")
        elif char == "cos":
            try:
                result = math.cos(eval(self.result_var.get()))
                self.result_var.set(str(result))
            except Exception as e:
                self.result_var.set("Error")
        elif char == "tan":
            try:
                result = math.tan(eval(self.result_var.get()))
                self.result_var.set(str(result))
            except Exception as e:
                self.result_var.set("Error")
        elif char == "sqrt":
            try:
                result = math.sqrt(eval(self.result_var.get()))
                self.result_var.set(str(result))
            except Exception as e:
                self.result_var.set("Error")
        else:
            if self.result_var.get() == "0":
                self.result_var.set(char)
            else:
                self.result_var.set(self.result_var.get() + char)


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
