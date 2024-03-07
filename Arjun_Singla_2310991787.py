import tkinter as tk
from tkinter import ttk
import math


class ScientificCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scientific Calculator")
        self.geometry("400x500")
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry widget to display input and results
        entry = ttk.Entry(
            self, textvariable=self.result_var, font=("Arial", 14), justify="right"
        )
        entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Buttons for numbers and operations
        buttons = [
            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("/", 1, 3),
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("*", 2, 3),
            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("-", 3, 3),
            ("0", 4, 0),
            (".", 4, 1),
            ("=", 4, 2),
            ("+", 4, 3),
        ]

        for text, row, col in buttons:
            ttk.Button(
                self, text=text, command=lambda t=text: self.on_button_click(t)
            ).grid(row=row, column=col, sticky="nsew")

        # Additional scientific buttons
        ttk.Button(
            self, text="sqrt", command=lambda: self.on_button_click("sqrt")
        ).grid(row=5, column=0, sticky="nsew")
        ttk.Button(self, text="^", command=lambda: self.on_button_click("^")).grid(
            row=5, column=1, sticky="nsew"
        )
        ttk.Button(self, text="log", command=lambda: self.on_button_click("log")).grid(
            row=5, column=2, sticky="nsew"
        )
        ttk.Button(self, text="sin", command=lambda: self.on_button_click("sin")).grid(
            row=5, column=3, sticky="nsew"
        )
        ttk.Button(self, text="cos", command=lambda: self.on_button_click("cos")).grid(
            row=6, column=0, sticky="nsew"
        )
        ttk.Button(self, text="tan", command=lambda: self.on_button_click("tan")).grid(
            row=6, column=1, sticky="nsew"
        )

        # Configure row and column weights
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button_text):
        current_input = self.result_var.get()

        if button_text == "=":
            try:
                result = eval(current_input)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif button_text == "sqrt":
            try:
                result = math.sqrt(float(current_input))
                self.result_var.set(result)
            except ValueError:
                self.result_var.set("Error")
        elif button_text == "^":
            self.result_var.set(current_input + "**")
        elif button_text == "log":
            self.result_var.set("math.log(" + current_input + ", ")
        elif button_text in ("sin", "cos", "tan"):
            self.result_var.set("math." + button_text + "(" + current_input + ")")
        else:
            self.result_var.set(current_input + button_text)


if __name__ == "__main__":
    app = ScientificCalculator()
    app.mainloop()
