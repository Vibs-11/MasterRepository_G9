import tkinter as tk
from tkinter import ttk
import math

def on_button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_trig(func):
    try:
        angle = eval(entry.get())
        if angle_unit.get() == "Degrees":
            angle = math.radians(angle)
        result = func(angle)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

window = tk.Tk()
window.title("Scientific Calculator")
window.geometry("400x600")
window.configure(bg='#303030')

entry = ttk.Entry(window, width=20, font=('Arial', 20), justify='right')
entry.grid(row=0, column=0, columnspan=5, pady=10, padx=10, ipady=10, sticky='news')

style = ttk.Style()
style.configure("TButton", font=('Arial', 14), background='#404040', foreground='#FFFFFF')
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'sin', 'cos', 'tan', '^2', 'sqrt'
]
row_val = 1
col_val = 0

for button in buttons:
    if button in ['sin', 'cos', 'tan', '^2', 'sqrt']:
        ttk.Button(window, text=button, style="TButton", command=lambda btn=button: calculate_trig(getattr(math, btn) if btn in ['sin', 'cos', 'tan'] else lambda x: eval(f"x**2") if btn == '^2' else lambda x: eval(f'math.{btn}(x)'))).grid(row=row_val, column=col_val, padx=5, pady=5)
    else:
        ttk.Button(window, text=button, style="TButton", command=lambda btn=button: on_button_click(btn)).grid(row=row_val, column=col_val, padx=5, pady=5)

    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

ttk.Button(window, text='C', style="TButton", command=clear_entry).grid(row=row_val, column=0, columnspan=2, padx=5, pady=5, sticky='news')
ttk.Button(window, text='=', style="TButton", command=calculate).grid(row=row_val, column=2, columnspan=3, padx=5, pady=5, sticky='news')

angle_unit = tk.StringVar()
angle_unit.set("Radians")
angle_menu = ttk.OptionMenu(window, angle_unit, "Radians", "Degrees")
angle_menu.config(style="TButton", width=8)
angle_menu.grid(row=row_val + 1, column=0, columnspan=2, pady=5, padx=5, sticky='news')

window.mainloop()
