import tkinter as tk

def on_click(event):
    current_text = entry.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for displaying the current input and result
entry = tk.Entry(root, font=("Helvetica", 16), justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Define buttons and their positions
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0), ("(", 5, 1), (")", 5, 2), ("**", 5, 3),  # Use "**" for exponentiation
]

# Create and place buttons
for (text, row, column) in buttons:
    button = tk.Button(root, text=text, font=("Helvetica", 16), padx=20, pady=20)
    button.grid(row=row, column=column, sticky="nsew")
    button.bind("<Button-1>", on_click)

# Configure row and column weights so that they expand proportionally
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Start the Tkinter event loop
root.mainloop()
