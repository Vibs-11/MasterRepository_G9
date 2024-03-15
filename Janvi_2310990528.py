import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_add():
    global first_number
    global math_operation
    math_operation = "addition"
    first_number = float(entry.get())
    entry.delete(0, tk.END)

def button_subtract():
    global first_number
    global math_operation
    math_operation = "subtraction"
    first_number = float(entry.get())
    entry.delete(0, tk.END)

def button_multiply():
    global first_number
    global math_operation
    math_operation = "multiplication"
    first_number = float(entry.get())
    entry.delete(0, tk.END)

def button_divide():
    global first_number
    global math_operation
    math_operation = "division"
    first_number = float(entry.get())
    entry.delete(0, tk.END)

def button_equal():
    second_number = float(entry.get())
    entry.delete(0, tk.END)
    if math_operation == "addition":
        entry.insert(0, first_number + second_number)
    elif math_operation == "subtraction":
        entry.insert(0, first_number - second_number)
    elif math_operation == "multiplication":
        entry.insert(0, first_number * second_number)
    elif math_operation == "division":
        entry.insert(0, first_number / second_number)

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = tk.Button(root, text="+", padx=39, pady=20, command=button_add)
button_equal = tk.Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear = tk.Button(root, text="Clear", padx=79, pady=20, command=button_clear)

button_subtract = tk.Button(root, text="-", padx=41, pady=20, command=button_subtract)
button_multiply = tk.Button(root, text="*", padx=41, pady=20, command=button_multiply)
button_divide = tk.Button(root, text="/", padx=41, pady=20, command=button_divide)

# Put buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()
