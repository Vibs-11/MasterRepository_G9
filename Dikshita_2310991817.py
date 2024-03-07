import tkinter as tk

# Function to handle button clicks
def button_click(symbol):
    if symbol == '=':
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif symbol == 'C':
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, symbol)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Set background color
root.configure(bg='black')

# Create entry widget
entry = tk.Entry(root, font=('Arial', 20), bd=5, bg='black', fg='white')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='ew')

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create buttons
row, col = 1, 0
for button in buttons:
    tk.Button(root, text=button, font=('Arial', 15), width=5, height=2, bg='black', fg='white', bd=5,
              command=lambda b=button: button_click(b)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the application
root.mainloop()
