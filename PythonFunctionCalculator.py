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
    elif text == "SP":
        # handle the special case for "SP" button
        pass
    elif text == "÷":
        entry.insert(tk.END, "/")
    elif text == "X":
        entry.insert(tk.END, "*")
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")

# Set background color of the root window to black
root.config(bg="black")

entry = tk.Entry(root, font=("Digital-7", 35), justify="right", bg="Dark Green", fg="white")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

buttons = [
    ("C", 1, 0), ("%", 1, 1), ("÷", 1, 2), ("X", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("-", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("+", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("=", 4, 3),
    ("SP", 5, 0), ("0", 5, 1), (".", 5, 2)
]

for (text, row, column) in buttons:
    button = tk.Button(root, text=text, font=("Consolas", 20), width=5, height=2, bg="black", fg="white", borderwidth=5, relief=tk.RIDGE)
    button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
    button.bind("<Button-1>", on_click)

root.mainloop()
