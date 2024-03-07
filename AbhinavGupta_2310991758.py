from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("300x400")

def button_click(number):
    if number == 'sin':
        try:
            theta = float(field.get("1.0", "end-1c"))
            result = math.sin(math.radians(theta))
            field.delete(1.0, tk.END)
            field.insert(tk.END, str(result))
        except ValueError:
            field.delete(1.0, tk.END)
            field.insert(tk.END, "Error")
    elif number == 'cos':
        try:
            theta = float(field.get("1.0", "end-1c"))
            result = math.cos(math.radians(theta))
            field.delete(1.0, tk.END)
            field.insert(tk.END, str(result))
        except ValueError:
            field.delete(1.0, tk.END)
            field.insert(tk.END, "Error")
    elif number == 'tan':
        try:
            theta = float(field.get("1.0", "end-1c"))
            result = math.tan(math.radians(theta))
            field.delete(1.0, tk.END)
            field.insert(tk.END, str(result))
        except ValueError:
            field.delete(1.0, tk.END)
            field.insert(tk.END, "Error")
    elif number == '√':
        try:
            number = float(field.get("1.0", "end-1c"))
            result = math.sqrt(number)
            field.delete(1.0, tk.END)
            field.insert(tk.END, str(result))
        except ValueError:
            field.delete(1.0, tk.END)
            field.insert(tk.END, "Error")
    elif number == "log":
        try:
            number = float(field.get("1.0", "end-1c"))
            result = math.log10(number)
            field.delete(1.0, tk.END)
            field.insert(tk.END, str(result))
        except ValueError:
            field.delete(1.0, tk.END)
            field.insert(tk.END, "Error")
    else:
        current = field.get("1.0", "end-1c")
        field.delete(1.0, END)
        field.insert(END, str(current) + str(number))

def clear_field():
    field.delete(1.0, END)

def backspace():
    current = field.get("1.0", "end-1c")
    field.delete(1.0, END)
    field.insert(END, str(current)[1:])

def calculate():
    expression = field.get("1.0", "end-1c")
    try:
        result = eval(expression)
        field.delete(1.0, END)
        field.insert(END, str(result))
    except:
        field.delete(1.0, END)
        field.insert(END, "Error")
        
def scientific_calc():
    root.geometry("390x400")
    sin = Button(root, text="sin", width=5, height=2, command=lambda: button_click("sin"), font=('Calibri', 12))
    sin.place(x=320, y=60)
    cos = Button(root, text="cos", width=5, height=2, command=lambda: button_click("cos"), font=('Calibri', 12))
    cos.place(x=320, y=130)
    tan = Button(root, text="tan", width=5, height=2, command=lambda: button_click("tan"), font=('Calibri', 12))
    tan.place(x=320, y=200)
    sqrt = Button(root, text="√", width=5, height=2, command=lambda: button_click("√"), font=('Calibri', 12))
    sqrt.place(x=320, y=270)
    log = Button(root, text="log", width=5, height=2, command=lambda: button_click("log"), font=('Calibri', 12))
    log.place(x=320, y=340)

field = Text(root, width=35, height=2)
field.place(x=10, y=20)
clear = Button(root, text="CE", width=5, height=2, command=clear_field, font=('Calibri', 12))
clear.place(x=85, y=60)
divide = Button(root, text="÷", width=5, height=2, command=lambda: button_click("/"), font=('Calibri', 12))
divide.place(x=165, y=60)
multiply = Button(root, text="×", width=5, height=2, command=lambda: button_click("*"), font=('Calibri', 12))
multiply.place(x=240, y=60)
bspace = Button(root, text="⌫", width=5, height=2, command=backspace, font=('Calibri', 12))
bspace.place(x=240, y=130)
sub = Button(root, text="-", width=5, height=2, command=lambda: button_click("-"), font=('Calibri', 12))
sub.place(x=240, y=200)
add = Button(root, text="+", width=5, height=2, command=lambda: button_click("+"), font=('Calibri', 12))
add.place(x=240, y=270)
equal = Button(root, text="=", width=5, height=2, command=calculate, font=('Calibri', 12))
equal.place(x=240, y=340)
seven = Button(root, text="7", width=5, height=2, command=lambda: button_click("7"), font=('Calibri', 12))
seven.place(x=10, y=130)
four = Button(root, text="4", width=5, height=2, command=lambda: button_click("4"), font=('Calibri', 12))
four.place(x=10, y=200)
one = Button(root, text="1", width=5, height=2, command=lambda: button_click("1"), font=('Calibri', 12))
one.place(x=10, y=270)
eight = Button(root, text="8", width=5, height=2, command=lambda: button_click("8"), font=('Calibri', 12))
eight.place(x=85, y=130)
five = Button(root, text="5", width=5, height=2, command=lambda: button_click("5"), font=('Calibri', 12))
five.place(x=85, y=200)
two = Button(root, text="2", width=5, height=2, command=lambda: button_click("2"), font=('Calibri', 12))
two.place(x=85, y=270)
nine = Button(root, text="9", width=5, height=2, command=lambda: button_click("9"), font=('Calibri', 12))
nine.place(x=165, y=130)
six = Button(root, text="6", width=5, height=2, command=lambda: button_click("6"), font=('Calibri', 12))
six.place(x=165, y=200)
three = Button(root, text="3", width=5, height=2, command=lambda: button_click("3"), font=('Calibri', 12))
three.place(x=165, y=270)
zero = Button(root, text="0", width=16, height=2, command=lambda: button_click("0"), font=('Calibri', 12))
zero.place(x=10, y=340)
decimal = Button(root, text=".", width=5, height=2, command=lambda: button_click("."), font=('Calibri', 12))
decimal.place(x=165, y=340)
scientific_button = Button(root, text="SC", width=5, height=2, command=scientific_calc, font=('Calibri', 12))
scientific_button.place(x=10, y=60)
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)
root.mainloop()