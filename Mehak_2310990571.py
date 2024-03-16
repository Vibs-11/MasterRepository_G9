from tkinter import *
import math

def button_click(char):
    global calc_operator
    if char == 'DEL':
        button_delete()
    elif char == 'AC':
        button_clear_all()
    elif char == '=':
        button_equal()
    elif char == 'sin':
        calculate_trig(math.sin)
    elif char == 'cos':
        calculate_trig(math.cos)
    elif char == 'tan':
        calculate_trig(math.tan)
    elif char == 'cot':
        calculate_trig(lambda x: 1 / math.tan(x))
    elif char == 'sqrt':
        calculate_square_root()
    elif char == 'x!':
        calculate_factorial()
    elif char == 'e':
        button_click(math.e)
    elif char == 'π':
        button_click(math.pi)
    elif char == 'log':
        calculate_log()
    elif char == 'ln':
        calculate_ln()
    elif char == 'abs':
        calculate_abs()
    elif char == 'mod':
        calculate_mod()
    elif char == 'div':
        calculate_division()
    elif char == 'x^n':
        calculate_exponential()
    elif char == 'x^2':
        calculate_square()
    elif char == 'x^3':
        calculate_cube()
    elif char == '+/-':
        change_sign()
    elif char == '%':
        calculate_percentage()
    else:
        calc_operator += str(char)
        text_input.set(calc_operator)

def button_clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set("")

def button_delete():
    global calc_operator
    text = calc_operator[:-1]
    calc_operator = text
    text_input.set(text)

def calculate_factorial():
    global calc_operator
    try:
        result = str(math.factorial(int(calc_operator)))
    except ValueError:
        result = "ERROR"
    calc_operator = result
    text_input.set(result)

def calculate_trig(func):
    global calc_operator
    try:
        result = str(func(math.radians(float(calc_operator))))
    except ValueError:
        result = "ERROR"
    calc_operator = result
    text_input.set(result)

def calculate_square_root():
    global calc_operator
    try:
        result = str(math.sqrt(float(calc_operator)))
    except ValueError:
        result = "ERROR"
    calc_operator = result
    text_input.set(result)

def change_sign():
    global calc_operator
    if calc_operator:
        calc_operator = str(-1 * float(calc_operator))
        text_input.set(calc_operator)

def calculate_percentage():
    global calc_operator
    try:
        temp = str(float(calc_operator) / 100)
    except ValueError:
        temp = "ERROR"
    calc_operator = temp
    text_input.set(temp)

def calculate_log():
    global calc_operator
    try:
        result = str(math.log10(float(calc_operator)))
    except ValueError:
        result = "ERROR"
    calc_operator = result
    text_input.set(result)

def calculate_ln():
    global calc_operator
    try:
        result = str(math.log(float(calc_operator)))
    except ValueError:
        result = "ERROR"
    calc_operator = result
    text_input.set(result)

def calculate_abs():
    global calc_operator
    try:
        result = str(abs(float(calc_operator)))
    except ValueError:
        result = "ERROR"
    calc_operator = result
    text_input.set(result)

def calculate_mod():
    global calc_operator
    try:
        result = str(math.fmod(float(calc_operator), 1))
    except ValueError:
        result = "ERROR"
    calc_operator = result
    text_input.set(result)

def calculate_division():
    global calc_operator
    try:
        result = str(1 / float(calc_operator))
    except ZeroDivisionError:
        result = "ERROR"
    except ValueError:
        result = "ERROR"
    calc_operator = result
    text_input.set(result)

def calculate_exponential():
    global calc_operator
    try:
        result = str(math.exp(float(calc_operator)))
    except ValueError:
        result = "ERROR"
    calc_operator = result
    text_input.set(result)

def calculate_square():
    global calc_operator
    try:
        result = str(float(calc_operator) ** 2)
    except ValueError:
        result = "ERROR"
    calc_operator = result
    text_input.set(result)

def calculate_cube():
    global calc_operator
    try:
        result = str(float(calc_operator) ** 3)
    except ValueError:
        result = "ERROR"
    calc_operator = result
    text_input.set(result)

def button_equal():
    global calc_operator
    try:
        temp_op = str(eval(calc_operator))
    except ZeroDivisionError:
        temp_op = "ERROR"
    except Exception as e:
        temp_op = "ERROR"
    text_input.set(temp_op)
    calc_operator = temp_op

# Initialize Tkinter
tk_calc = Tk()
tk_calc.title("Scientific Calculator")

# Set background color to black
tk_calc.configure(bg="black")

# Initialize variables
calc_operator = ""
text_input = StringVar()

# Create display entry
text_display = Entry(tk_calc, font=('Times new roman', 20), textvariable=text_input, bd=5, insertwidth=5, justify='right')
text_display.grid(columnspan=5, padx=10, pady=15)

# Define button parameters
button_params = {'font': ('Arial', 16), 'width': 5, 'height': 2, 'bg': 'black', 'fg': 'white'}

# Create buttons
buttons = [
    ('abs', 'mod', 'div', 'x!', 'e'),
    ('sin', 'cos', 'tan', 'cot', 'π'),
    ('x^2', 'x^3', 'x^n', '+/-', '%'),
    ('sqrt', 'log', 'ln', '(', ')'),
    ('7', '8', '9', 'DEL', 'AC'),
    ('4', '5', '6', '*', '/'),
    ('1', '2', '3', '+', '-'),
    ('0', '.', 'EXP', '=', '=')
]

for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        btn_text = buttons[i][j]
        btn_command = lambda char=btn_text: button_click(char)
        btn = Button(tk_calc, text=btn_text, command=btn_command, **button_params)
        btn.grid(row=i + 1, column=j)

# Start Tkinter event loop
tk_calc.mainloop()
