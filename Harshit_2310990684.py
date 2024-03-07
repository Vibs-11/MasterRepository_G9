import tkinter as tk
import math

# Functions

def button_click(number):
    current = entry_box.get()
    entry_box.delete(0, tk.END)
    entry_box.insert(0, current + str(number))

def button_clear():
    entry_box.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry_box.get())
        entry_box.delete(0, tk.END)
        entry_box.insert(0, str(result))
    except:
        entry_box.delete(0, tk.END)
        entry_box.insert(0, "Error")

def button_square():
    try:
        result = eval(entry_box.get()) ** 2
        entry_box.delete(0, tk.END)
        entry_box.insert(0, str(result))
    except:
        entry_box.delete(0, tk.END)
        entry_box.insert(0, "Error")

def button_log():
    try:
        result = math.log(float(entry_box.get()))
        entry_box.delete(0, tk.END)
        entry_box.insert(0, str(result))
    except:
        entry_box.delete(0, tk.END)
        entry_box.insert(0, "Error")

# Title and color

root = tk.Tk()
root.title("GUI_Calculator_BY_Harshit_2310990684")


root.configure(bg='#1E1E1E')
root.option_add('*foreground', 'white')
root.option_add('*background', '#1E1E1E')

entry_box = tk.Entry(root, width=45, borderwidth=5, font=('Arial', 14))
entry_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Adding Buttons

button_1 = tk.Button(root, text="1", padx=20, pady=10, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=20, pady=10, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=20, pady=10, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=20, pady=10, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=20, pady=10, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=20, pady=10, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=20, pady=10, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=20, pady=10, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=20, pady=10, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=20, pady=10, command=lambda: button_click(0))

button_add = tk.Button(root, text="+", padx=20, pady=10, command=lambda: button_click("+"))
button_subtract = tk.Button(root, text="-", padx=20, pady=10, command=lambda: button_click("-"))
button_multiply = tk.Button(root, text="*", padx=20, pady=10, command=lambda: button_click("*"))
button_divide = tk.Button(root, text="/", padx=20, pady=10, command=lambda: button_click("/"))

button_equal = tk.Button(root, text="=", padx=20, pady=10, command=button_equal)
button_clear = tk.Button(root, text="Clear", padx=20, pady=10, command=button_clear)
button_square = tk.Button(root, text="x^2", padx=18, pady=10, command=button_square)
button_log = tk.Button(root, text="log", padx=19, pady=10, command=button_log)

# Buttons Position

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

button_equal.grid(row=4, column=1)
button_clear.grid(row=4, column=2)
button_square.grid(row=5, column=0)
button_log.grid(row=5, column=1)

root.mainloop()