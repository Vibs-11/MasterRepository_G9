from tkinter import *
import math
def button_click(char):
    global calc_operator
    calc_operator+=str(char)
    text_input.set(calc_operator)
def button_clear():
    global calc_operator
    calc_operator=""
    text_input.set(calc_operator)
def delete_one():
    global calc_operator
    text=calc_operator[:-1]
    calc_operator=text 
    text_input.set(calc_operator)  
def trig_sin():
    global calc_operator
    res=str(math.sin(math.radians(int(calc_operator))))  
    calc_operator=res
    text_input.set(res) 
def trig_cos():
    global calc_operator
    res=str(math.cos(math.radians(int(calc_operator)))  )   
    calc_operator=res
    text_input.set(calc_operator)   
def trig_tan():
    global calc_operator
    res=str(math.tan(math.radians(int(calc_operator)))  )   
    calc_operator=res
    text_input.set(calc_operator)        
def trig_cot():
    global calc_operator
    res=str(1/math.tan(math.radians(int(calc_operator)))  )   
    calc_operator=res
    text_input.set(calc_operator)  
def trig_sec():
    global calc_operator
    res=str(1/math.cos(math.radians(int(calc_operator)))  )   
    calc_operator=res
    text_input.set(calc_operator) 
def trig_cosec():
    global calc_operator
    res=str(1/math.sin(math.radians(int(calc_operator)))  )   
    calc_operator=res
    text_input.set(calc_operator)
def button_equal():
    global calc_operator
    temp_op = str(eval(calc_operator))
    text_input.set(temp_op)
    calc_operator = temp_op                     

sin,cos,tan=math.sin,math.cos,math.tan
log=math.log10

tk_calc=Tk()
text_input=StringVar()
tk_calc.configure(bg="#000000",bd=15)
tk_calc.title("Calculator")
calc_operator = ""
text_input = StringVar()

text_display = Entry(tk_calc, font=('sans-serif', 20, 'bold'), textvariable=text_input,
                       bd=5, insertwidth = 5, bg='#FFEFDB', justify='right').grid(columnspan=5, padx = 10, pady = 15)

font_function = {'bd':5, 'fg':'white', 'bg':'grey', 'font':('sans-serif', 20, 'bold')}
font_button = {'bd':5, 'fg':'white', 'bg':'grey', 'font':('sans-serif', 20, 'bold')}
mod=Button(tk_calc,font_function,text='%',
  command=lambda:button_click('%')).grid(row=1,column=0,sticky=NSEW)
div=Button(tk_calc,font_function,text='/',
           command=lambda:button_click('/')).grid(row=1,column=1,sticky=NSEW)
add=Button(tk_calc,font_function,text='+',
           command=lambda:button_click('+')).grid(row=1,column=2,sticky=NSEW)
add=Button(tk_calc,font_function,text='+',
   command=lambda:button_click('+')).grid(row=3,column=3,sticky=NSEW)
sub=Button(tk_calc,font_function,text='-',
           command=lambda:button_click('-')).grid(row=1,column=3,sticky=NSEW)
sub=Button(tk_calc,font_function,text='-',
   command=lambda:button_click('-')).grid(row=3,column=4,sticky=NSEW)
mul=Button(tk_calc,font_function,text='*',
           command=lambda:button_click('*')).grid(row=1,column=4,sticky=NSEW)
sine=Button(tk_calc,font_function,text='sin',
           command=trig_sin).grid(row=2,column=0,sticky=NSEW)
cosine=Button(tk_calc,font_function,text='cos',
           command=trig_cos).grid(row=2,column=1,sticky=NSEW)
tangent=Button(tk_calc,font_function,text='tan',
           command=trig_tan).grid(row=2,column=2,sticky=NSEW)
cosec=Button(tk_calc,font_function,text='cosec',
           command=trig_cosec).grid(row=2,column=3,sticky=NSEW)
sec=Button(tk_calc,font_function,text='sec',
           command=trig_sec).grid(row=2,column=4,sticky=NSEW)
cot=Button(tk_calc,font_function,text='sin',
           command=trig_cot).grid(row=3,column=0,sticky=NSEW)
power=Button(tk_calc,font_function,text='x^n',
             command=lambda:button_click('**')).grid(row=3,column=1,sticky=NSEW)
log1=Button(tk_calc,font_function,text='log10',
            command=lambda:button_click('log(')).grid(row=3,column=2,sticky=NSEW)
button_7=Button(tk_calc,font_button,text='7',
                command=lambda:button_click('7')).grid(row=4,column=0,sticky=NSEW)
button_8=Button(tk_calc,font_button,text='8',
                command=lambda:button_click('8')).grid(row=4,column=1,sticky=NSEW)
button_9=Button(tk_calc,font_button,text='9',
                command=lambda:button_click('9')).grid(row=4,column=2,sticky=NSEW)
delete=Button(tk_calc,font_button,text='Del',
              command=delete_one).grid(row=4,column=3,sticky=NSEW)
clear=Button(tk_calc,font_button,text='AC',
                command=button_clear).grid(row=4,column=4,sticky=NSEW)
button_6=Button(tk_calc,font_button,text='6',
                command=lambda:button_click('6')).grid(row=5,column=0,sticky=NSEW)
button_5=Button(tk_calc,font_button,text='5',
                command=lambda:button_click('5')).grid(row=5,column=1,sticky=NSEW)
button_4=Button(tk_calc,font_button,text='4',
                command=lambda:button_click('4')).grid(row=5,column=2,sticky=NSEW)
button_3=Button(tk_calc,font_button,text='3',
                command=lambda:button_click('3')).grid(row=5,column=3,sticky=NSEW)
button_2=Button(tk_calc,font_button,text='2',
                command=lambda:button_click('2')).grid(row=5,column=4,sticky=NSEW)
button_1=Button(tk_calc,font_button,text='1',
                command=lambda:button_click('1')).grid(row=6,column=0,sticky=NSEW)
button_0=Button(tk_calc,font_button,text='0',
                command=lambda:button_click('0')).grid(row=6,column=1,sticky=NSEW)
equal=Button(tk_calc,font_button,text='=',
             command=button_equal).grid(row=6,columnspan=3,column=2,sticky=NSEW)
tk_calc.mainloop()
