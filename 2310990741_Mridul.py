from tkinter import * 
import math

win = Tk() 
win.title("Functional Calculator") 
win.iconbitmap('calculator.ico')

exp = ""

def button_press(num):
    global exp
    exp= input_text.get()
    exp= str(exp) + str(num)
    input_text.set(exp)
    display.icursor(len(exp))  

def button_oper(opr):
    global exp
    exp = input_text.get()
    exp= str(exp) + str(opr)
    input_text.set(exp)
    display.icursor(len(exp))

def sin():
    global exp
    num = float(input_text.get())
    result = math.sin(num)
    input_text.set(result)
def cos():
    global exp
    num = float(input_text.get())
    result = math.cos(num)
    input_text.set(result)

def tan():
    global exp
    num = float(input_text.get())
    result = math.tan(num)
    input_text.set(result)

def clr_scr():
    global exp
    input_text.set("")
    exp = ""

def equal(event):
    global exp
    exp = input_text.get()
    input_text.set("")
    result = float(eval(exp))
    exp = result
    display.insert(0, result)
    input_text.set(result)


display_frame = LabelFrame(win, padx=2, pady=2, bd=6)
display_frame.grid(row=0, column=0, columnspan=4)

input_text = StringVar()
display = Entry(display_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=22,bg="lightgrey", bd=0, justify=RIGHT)
display.pack(ipady= 12) 

button_0 = Button(win, padx=30, pady=30, text="0", bg="Orange", command=lambda:button_press(0))
button_sin = Button(win, padx=25, pady=25, text="sin", bg="Orange", command=sin)
button_cos = Button(win, padx=25, pady=25, text="cos", bg="Orange", command=cos)
button_tan = Button(win, padx=25, pady=25, text="tan", bg="Orange", command=tan)
button_1 = Button(win, padx=30, pady=30, text="1", bg="Orange", command=lambda: button_press(1))
button_2 = Button(win, padx=30, pady=30, text="2", bg="Orange", command=lambda: button_press(2))
button_3 = Button(win, padx=30, pady=30, text="3", bg="Orange", command=lambda: button_press(3))
button_4 = Button(win, padx=30, pady=30, text="4", bg="Orange", command=lambda: button_press(4))
button_5 = Button(win, padx=30, pady=30, text="5", bg="Orange", command=lambda: button_press(5))
button_6 = Button(win, padx=30, pady=30, text="6", bg="Orange", command=lambda: button_press(6))
button_7 = Button(win, padx=30, pady=30, text="7", bg="Orange", command=lambda: button_press(7))
button_8 = Button(win, padx=30, pady=30, text="8", bg="Orange", command=lambda: button_press(8))
button_9 = Button(win, padx=30, pady=30, text="9", bg="Orange", command=lambda: button_press(9))
button_add = Button(win, padx=30, pady=30, text="+", bg="lightgrey", command=lambda: button_oper("+"))
button_sub = Button(win, padx=30, pady=30, text="- ", bg="lightgrey", command=lambda: button_oper("-"))
button_div = Button(win, padx=30, pady=30, text="/ ", bg="lightgrey", command=lambda: button_oper("/"))
button_mul = Button(win, padx=30, pady=30, text="* ", bg="lightgrey", command=lambda: button_oper("*"))
button_equal = Button(win, padx=30, pady=30, text="=", bg="lightgrey", command=lambda: equal(""))
button_clear = Button(win, padx=30, pady=25, text="C", bg="lightgrey", command=clr_scr)
button_dec = Button(win, padx=30, pady=30, text=" .", bg="lightgrey", command=lambda: button_press("."))
button_tan.grid(row=1, column=0)
button_sin.grid(row=1, column=1)
button_cos.grid(row=1, column=2)
button_clear.grid(row=1, column=3)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)

button_9.grid(row=2, column=2)
button_add.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_sub.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_div.grid(row=4, column=3)

button_equal.grid(row=5, column=0)
button_0.grid(row=5, column=1)
button_dec.grid(row=5, column=2)
button_mul.grid(row=5, column=3)

win.mainloop()
