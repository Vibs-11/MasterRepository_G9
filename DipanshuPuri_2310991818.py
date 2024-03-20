import tkinter as tk
from tkinter import messagebox
import math

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Calculator", font=("Helvetica", 16)).grid(row=0, columnspan=4)

        self.result_label = tk.Label(self.master, text="", font=("Helvetica", 12))
        self.result_label.grid(row=1, column=0, columnspan=4, sticky=tk.W)  # Adjusted column span and sticky property

        # Input_frame
        input_frame = tk.Frame(self.master, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        input_frame.grid(row=2, columnspan=4)

        # Input_field inside frame
        self.input_text = tk.StringVar()
        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=24, bg="#eee", bd=0, justify=tk.RIGHT)
        input_field.pack(ipady=10) # 'ipady' is internal padding to increase the height of input field

        # Btns_frame
        btns_frame = tk.Frame(self.master, width=312, height=272.5, bg="grey")
        btns_frame.grid(row=3, columnspan=4)

        # First row
        clear = tk.Button(btns_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2", command=self.clear_input)
        clear.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
        divide = tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.btn_click("/"))
        divide.grid(row=0, column=3, padx=1, pady=1)

        # Second row
        seven = tk.Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(7))
        seven.grid(row=1, column=0, padx=1, pady=1)
        eight = tk.Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(8))
        eight.grid(row=1, column=1, padx=1, pady=1)
        nine = tk.Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(9))
        nine.grid(row=1, column=2, padx=1, pady=1)
        multiply = tk.Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.btn_click("*"))
        multiply.grid(row=1, column=3, padx=1, pady=1)

        # Third row
        four = tk.Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(4))
        four.grid(row=2, column=0, padx=1, pady=1)
        five = tk.Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(5))
        five.grid(row=2, column=1, padx=1, pady=1)
        six = tk.Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(6))
        six.grid(row=2, column=2, padx=1, pady=1)
        minus = tk.Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.btn_click("-"))
        minus.grid(row=2, column=3, padx=1, pady=1)

        # Fourth row
        one = tk.Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(1))
        one.grid(row=3, column=0, padx=1, pady=1)
        two = tk.Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(2))
        two.grid(row=3, column=1, padx=1, pady=1)
        three = tk.Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(3))
        three.grid(row=3, column=2, padx=1, pady=1)
        plus = tk.Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.btn_click("+"))
        plus.grid(row=3, column=3, padx=1, pady=1)

        # Fourth row
        zero = tk.Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.btn_click(0))
        zero.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
        point = tk.Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.btn_click("."))
        point.grid(row=4, column=2, padx=1, pady=1)
        equals = tk.Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=self.bt_equal)
        equals.grid(row=4, column=3, padx=1, pady=1)

    def btn_click(self, item):
        self.expression = self.input_text.get()
        self.expression = self.expression + str(item)
        self.input_text.set(self.expression)

    def clear_input(self):
        self.expression = ""
        self.input_text.set(self.expression)

    def bt_equal(self):
        try:
            result = str(eval(self.input_text.get()))
            self.input_text.set(result)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
