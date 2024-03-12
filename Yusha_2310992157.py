import tkinter as tk

def on_button_click(event):
    button_text = event.widget.cget("text")

    if button_text == "C":
        display_var.set("")
        return

    if button_text == "=":
        try:
            result = eval(display_var.get())
            display_var.set(result)
        except Exception as e:
            display_var.set("Error")
        return

    display_var.set(display_var.get() + button_text)

root = tk.Tk()
root.title("Calculator")

display_var = tk.StringVar()

display_entry = tk.Entry(root, textvariable=display_var, font=("Arial", 18), justify="right")
display_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row = 1
col = 0
for button_text in buttons:
    button = tk.Button(root, text=button_text, font=("Arial", 18), padx=10, pady=10)
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    button.bind("<Button-1>", on_button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()