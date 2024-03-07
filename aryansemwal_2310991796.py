import tkinter as tk
import math

def on_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text in ["sin", "cos", "tan", "log"]:
        try:
            if text == "sin":
                sin_result = math.sin(math.radians(float(entry.get())))
                entry.delete(0, tk.END)
                entry.insert(tk.END, str(sin_result))
            elif text == "cos":
                cos_result = math.cos(math.radians(float(entry.get())))
                entry.delete(0, tk.END)
                entry.insert(tk.END, str(cos_result))
            elif text == "tan":
                tan_result = math.tan(math.radians(float(entry.get())))
                entry.delete(0, tk.END)
                entry.insert(tk.END, str(tan_result))
            elif text == "log":
                log_result = math.log10(float(entry.get()))
                entry.delete(0, tk.END)
                entry.insert(tk.END, str(log_result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Graphical Calculator")

entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+",
    "√", "sin", "cos", "tan", "log"
]

row = 1
col = 0

for button in buttons:
    btn = tk.Button(root, text=button, padx=20, pady=10)
    btn.grid(row=row, column=col)
    btn.bind("<Button-1>", on_click)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
