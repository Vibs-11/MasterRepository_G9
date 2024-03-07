import tkinter as tk 
 
def evaluate(event): 
    try: 
        result = eval(entry.get()) 
        entry.delete(0, tk.END) 
        entry.insert(tk.END, result) 
    except Exception as e: 
        entry.delete(0, tk.END) 
        entry.insert(tk.END, "Error") 
 
root = tk.Tk() 
root.title("Calculator") 
 
entry = tk.Entry(root, width=30) 
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10) 
 
buttons = [ 
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    '0', '.', '=', '+' 
] 
 
row_num = 1 
col_num = 0 
 
for button in buttons: 
    if button == '=': 
        tk.Button(root, text=button, width=7, command=lambda: evaluate(None)).grid(row=row_num, column=col_num) 
    else: 
        tk.Button(root, text=button, width=7, command=lambda b=button: entry.insert(tk.END, b)).grid(row=row_num, column=col_num) 
    col_num += 1 
    if col_num > 3: 
        col_num = 0 
        row_num += 1 
 
root.bind('<Return>', evaluate) 
 
root.mainloop()
