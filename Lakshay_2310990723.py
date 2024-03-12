from tkinter import *
import math
from tkinter import messagebox
win =Tk()
win.title("Calculator.py")
win.iconbitmap('Calculator.ico')
win.maxsize(width=400,height=250)
win.minsize(width=400,height=250)
calc = Frame(win)
l= Label(win,text='My Calculator',fg='red').grid(row=0,column=1,sticky=W)
l1=Label(win,text='First Number',).grid(row=1,column=0,sticky=W)
l2=Label(win,text='Second Number',).grid(row=2,column=0,sticky=W)
l3=Label(win,text='Opeartor',).grid(row=3,column=0,sticky=W)
l4=Label(win,text='Answer',).grid(row=4,column=0,sticky=W)

num1= Entry(win,bd=5)
num1.grid(row=1,column=1)
num2= Entry(win,bd=5)
num2.grid(row=2,column=1)
E1= Entry(win,bd=5)
E1.grid(row=3,column=1)
E2= Entry(win,bd=5)
E2.grid(row=4,column=1)

def proces():
    number1=Entry.get(num1)
    number2=Entry.get(num2)
    operator=Entry.get(E1)
    number1=int(number1)
    number2=float(number2)
    if operator =="+":
        answer=number1+number2
    if operator =="-":
        answer=number1-number2
    if operator=="*":
        answer=number1*number2
    if operator=="/":
        answer=number1/number2
    if operator == "%":
        answer=number1%number2
    if operator == "**":
        answer=number1**number2
    Entry.insert(E2,0,answer)
    print(answer)

but=Button(win, text ="Submit",command = proces,bg='yellow').grid(row=5,column=1,)

win.mainloop()