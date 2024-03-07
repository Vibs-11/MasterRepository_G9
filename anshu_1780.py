import tkinter as tk
import math


def calculate():
  try:
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(result))
  except Exception as e:
    entry.delete(0, tk.END)
    entry.insert(tk.END, "Error")


def clear():
  entry.delete(0, tk.END)


def add_to_expression(char):
  entry.insert(tk.END, char)


def log_operation():
  entry.insert(tk.END, "math.log(")


def trig_operation(trig_func):
  entry.insert(tk.END, trig_func + "(")


root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', 'AC',
    '+', 'log', 'sin', 'cos', 'tan'
]

row = 1
col = 0

for button in buttons:
  if button == 'AC':
    tk.Button(root, text=button, width=5, command=clear).grid(row=row,
                                                              column=col)
  elif button in ['log', 'sin', 'cos', 'tan']:
    tk.Button(root,
              text=button,
              width=5,
              command=lambda b=button: trig_operation(b)).grid(row=row,
                                                               column=col)
  else:
    tk.Button(root,
              text=button,
              width=5,
              command=lambda b=button: add_to_expression(b)).grid(row=row,
                                                                  column=col)

  col += 1
  if col > 3:
    col = 0
    row += 1

tk.Button(root, text='(', width=5,
          command=lambda: add_to_expression('(')).grid(row=5, column=2)
tk.Button(root, text=')', width=5,
          command=lambda: add_to_expression(')')).grid(row=5, column=3)
tk.Button(root, text='=', width=5, command=calculate).grid(row=5, column=0)

root.mainloop()
