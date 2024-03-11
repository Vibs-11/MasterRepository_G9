import tkinter as tk

def multiplication():
  num1 = int(entry_num1.get())
  num2 = int(entry_num2.get())
  mul = num1 * num2
  result_label.config(text=f"{num1} * {num2} = {mul}")

def division():
  num1 = int(entry_num1.get())
  num2 = int(entry_num2.get())
  div = num1 / num2
  result_label.config(text=f"{num1} / {num2} = {div}")

def subtraction():
  num1 = int(entry_num1.get())
  num2 = int(entry_num2.get())
  sub = num1 - num2
  result_label.config(text=f"{num1} - {num2} = {sub}")  

def exponent():
  num1 = int(entry_num1.get())
  num2 = int(entry_num2.get())
  exp = num1 ** num2
  result_label.config(text=f"{num1} ^ {num2} = {exp}")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create labels
label_num1 = tk.Label(window, text="Enter the first number:")
label_num1.pack()

# Create entry fields
entry_num1 = tk.Entry(window)
entry_num1.pack()

label_num2 = tk.Label(window, text="Enter the second number:")
label_num2.pack()

entry_num2 = tk.Entry(window)
entry_num2.pack()

# Create buttons
button_multiply = tk.Button(window, text="Multiply", command=multiplication)
button_multiply.pack()

button_divide = tk.Button(window, text="Divide", command=division)
button_divide.pack()

button_subtract = tk.Button(window, text="Subtract", command=subtraction)
button_subtract.pack()

button_exponent = tk.Button(window, text="Exponent", command=exponent)
button_exponent.pack()

# Create a label to display the result
result_label = tk.Label(window, text="")
result_label.pack()

# Start the main loop
window.mainloop()
