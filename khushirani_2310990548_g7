import tkinter as tk
from tkinter import ttk
root=tk.Tk()
root.title("Calculator")
def add():
    number1=int(number1_entry.get())
    number2=int(number2_entry.get())
    p=number1+number2
    result_label.set(p)
def sub():
    number1=float(number1_entry.get())
    number2=float(number2_entry.get())
    q=number1-number2
    result_label.set(q)
def product():
    number1=float(number1_entry.get())
    number2=float(number2_entry.get())
    r=number1*number2
    result_label.set(r)
def modulus():
    number1=float(number1_entry.get())
    number2=float(number2_entry.get())
    s=number1%number2
    result_label.set(s)
def divide():
    number1=float(number1_entry.get())
    number2=float(number2_entry.get())
    t=number1/number2
    result_label.set(t)
ttk.Label(root,text='Enter number 1:').pack()
number1=tk.IntVar()
number1_entry=ttk.Entry(root,textvariable=number1)
number1_entry.focus()
number1_entry.pack()
ttk.Label(root,text='Enter number 2:').pack()
number2=tk.IntVar()
number2_entry=ttk.Entry(root,textvariable=number2)
number2_entry.pack()
sum_button=ttk.Button(root,text='+',command=add)
sum_button.pack()
sub_button=ttk.Button(root,text='-',command=sub)
sub_button.pack()
product_button=ttk.Button(root,text='*',command=product)
product_button.pack()
modulus_button=ttk.Button(root,text='%',command=modulus)
modulus_button.pack()
divide_button=ttk.Button(root,text='/',command=divide)
divide_button.pack()
result_label=tk.StringVar()
result_label.set("Result")
l=ttk.Label(root,textvariable=result_label)
l.pack()
root.mainloop()


# import tkinter as tk
# from tkinter import ttk
# z=0

# def sum():
#     global z
#     z = m.get() + n.get()
#     result()

# def sub():
#     global z
#     z = m.get() - n.get()
#     result()

# def div():
#     global z
#     z = m.get() / n.get()
#     result()

# def mul():
#     global z
#     z = m.get() * n.get()
#     result()

# def per():
#     global z
#     z = m.get() % n.get()
#     result()

# def result():
#     global z
#     if operation == '+':
#         result_label.set("Result: " + str(z))
#     elif operation == '-':
#         result_label.set("Result: " + str(z))
#     elif operation == '/':
#         result_label.set("Result: " + str(z))
#     elif operation == '*':
#         result_label.set("Result: " + str(z))
#     else:
#         result_label.set("Result: " + str(z))

# operation=tk.StringVar
# root = tk.Tk()
# # z = tk.IntVar()

# root.geometry("500x500")
# root.title("Calculator")
# root.iconbitmap("rohini.ico")

# ttk.Label(root, text="Enter no.1").pack()
# m = tk.IntVar()
# enter_num1 = ttk.Entry(root, textvariable=m)
# enter_num1.focus()
# enter_num1.pack()

# ttk.Label(root, text="Enter no.2").pack()
# n = tk.IntVar()
# enter_num2 = ttk.Entry(root, textvariable=n)
# enter_num2.focus()
# enter_num2.pack()

# sum_button = ttk.Button(root, text="+", command=sum)
# sum_button.pack()
# sub_button = ttk.Button(root, text="-", command=sub)
# sub_button.pack()
# div_button = ttk.Button(root, text="/", command=div)
# div_button.pack()
# mul_button = ttk.Button(root, text="*", command=mul)
# mul_button.pack()
# per_button = ttk.Button(root, text="%", command=per)

# result_label = tk.StringVar()
# result_label.set("Result")
# l=ttk.Label(root, textvariable=result_label)
# l.pack()

# root.mainloop()
