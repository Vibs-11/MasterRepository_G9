import tkinter as tk

def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(expression)
            expression = str(result)
        except:
            expression = "Error"
    elif text == "C":
        expression = ""
    else:
        expression += text
    display_var.set(expression)

root = tk.Tk()
root.title("Simple Calculator")

expression = ""
display_var = tk.StringVar()
display_var.set(expression)

display = tk.Entry(root, textvariable=display_var, font=("Arial", 20))
display.grid(row=0, column=0, columnspan=4)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0), ("(", 5, 1), (")", 5, 2)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 20), padx=10, pady=10)
    button.grid(row=row, column=col, sticky="nsew")
    button.bind("<Button-1>", click)

root.mainloop()
