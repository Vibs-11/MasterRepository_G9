import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "sqrt":
        entry.insert(tk.END, "math.sqrt(")
    elif text == "^2":
        entry.insert(tk.END, "**2")
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")

# Set background color of the root window to black
root.config(bg="black")

entry = tk.Entry(root, font=("Digital-7", 35), justify="right", bg="Dark Green", fg="white")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

buttons = [
    ("C", 1, 0), ("%", 1, 1), ("/", 1, 2), 
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), 
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), 
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), 
    ("0", 5, 0), (".", 5, 1), ("^2", 5, 2), 
    ("=", 5, 3), ("+", 2, 3), ("-", 3, 3), ("*", 4, 3)
]

for (text, row, column) in buttons:
    button = tk.Button(root, text=text, font=("Consolas", 20), width=5 if text not in ["0", "="] else 2, height=2, bg="black", fg="white", borderwidth=5, relief=tk.RIDGE)
    if text == "=":
        button.config(bg="orange", fg="black")
    button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
    button.bind("<Button-1>", on_click)

root.mainloop()
