import tkinter as tk
import math


def calculate(operation):
  try:
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    if operation == "Multiply":
      result = num1 * num2
    elif operation == "Divide":
      if num2 == 0:
        result = "Error: Division by zero"
      else:
        result = num1 / num2
    elif operation == "Subtract":
      result = num1 - num2
    elif operation == "Exponent":
      result = num1**num2
    elif operation == "Logarithm":
      if num1 <= 0 or num2 <= 0:
        result = "Error: Invalid input for logarithm"
      else:
        result = math.log(num1, num2)
    elif operation == "Square Root":
      result = math.sqrt(num1)
    else:
      result = "Unknown operation"
    label_result.config(text="Result: " + str(result))
  except ValueError:
    label_result.config(text="Invalid input")


def clear_input():
  entry1.delete(0, tk.END)
  entry2.delete(0, tk.END)
  label_result.config(text="Result: ")


root = tk.Tk()
root.title("Calculator")
root.configure(bg="#AED6F1")

label1 = tk.Label(root, text="Enter the first number:", bg="#AED6F1")

label1.grid(row=0, column=0, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, pady=5)

label2 = tk.Label(root, text="Enter the second number:", bg="#AED6F1")
label2.grid(row=1, column=0, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, pady=5)

buttons_frame = tk.Frame(root, bg="#AED6F1")
buttons_frame.grid(row=2, column=0, columnspan=2, pady=10)

operations = [
    "Multiply", "Divide", "Subtract", "Exponent", "Logarithm", "Square Root"
]
for i, operation in enumerate(operations):
  button = tk.Button(buttons_frame,
                     text=operation,
                     width=10,
                     command=lambda op=operation: calculate(op),
                     relief=tk.RAISED,
                     borderwidth=4,
                     bg="#F34F1C")
  button.grid(row=i // 3, column=i % 3, padx=5, pady=5)

clear_button = tk.Button(root,
                         text="Clear",
                         width=10,
                         command=clear_input,
                         relief=tk.RAISED,
                         borderwidth=4,
                         bg="#D4D4D2")
clear_button.grid(row=3, column=0, columnspan=2, pady=10)

label_result = tk.Label(root,
                        text="Result: ",
                        font=("Arial", 12, "bold"),
                        bg="#AED6F1")
label_result.grid(row=4, column=0, columnspan=2)

root.mainloop()
