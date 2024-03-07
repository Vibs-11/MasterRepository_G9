import tkinter as tk
import math

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

    elif text == "AC":
        entry.delete(0, tk.END)

    elif text == "log":
        try:
            value = float(entry.get())
            result = math.log10(value)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif text == "sin":
        try:
            value = float(entry.get())
            result = math.sin(math.radians(value))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif text == "cos":
        try:
            value = float(entry.get())
            result = math.cos(math.radians(value))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif text == "tan":
        try:
            value = float(entry.get())
            result = math.tan(math.radians(value))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("/", 4, 3),
    ("AC", 5, 0), ("log", 5, 1), ("sin", 5, 2), ("cos", 5, 3),
    ("tan", 6, 2)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20)
    button.grid(row=row, column=col)
    button.bind("<Button-1>", on_click)

root.mainloop()
