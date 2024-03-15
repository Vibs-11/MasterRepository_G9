import tkinter as tk
import math

# Function to perform basic arithmetic calculation
def calculate():
    try:
        result = eval(entry.get())  # Evaluate the expression entered by the user
        entry.delete(0, tk.END)     # Clear the entry widget
        entry.insert(tk.END, str(result))  # Display the result in the entry widget
    except:
        entry.delete(0, tk.END)     # Clear the entry widget
        entry.insert(tk.END, "Error")     # Display "Error" if there's an exception

# Function to clear the entry widget
def clear():
    entry.delete(0, tk.END)         # Clear the entry widget

# Function to calculate square root
def square_root():
    try:
        result = math.sqrt(float(entry.get()))   # Calculate square root of the number entered by the user
        entry.delete(0, tk.END)     # Clear the entry widget
        entry.insert(tk.END, str(result))  # Display the result in the entry widget
    except:
        entry.delete(0, tk.END)     # Clear the entry widget
        entry.insert(tk.END, "Error")     # Display "Error" if there's an exception

# Function to calculate exponent
def exponent():
    try:
        result = eval(entry.get()) ** 2    # Calculate square of the number entered by the user
        entry.delete(0, tk.END)     # Clear the entry widget
        entry.insert(tk.END, str(result))  # Display the result in the entry widget
    except:
        entry.delete(0, tk.END)     # Clear the entry widget
        entry.insert(tk.END, "Error")     # Display "Error" if there's an exception

# Function to perform trigonometric calculations
def trigonometry(func):
    try:
        result = eval('math.' + func + '(math.radians(' + entry.get() + '))')   # Calculate trigonometric function of the number entered by the user
        entry.delete(0, tk.END)     # Clear the entry widget
        entry.insert(tk.END, str(result))  # Display the result in the entry widget
    except:
        entry.delete(0, tk.END)     # Clear the entry widget
        entry.insert(tk.END, "Error")     # Display "Error" if there's an exception

# Create main window
root = tk.Tk()
root.title("Calculator")
root.configure(bg="#f0f0f0")

# Create entry widget for input and output
entry = tk.Entry(root, width=30, borderwidth=5, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons for the calculator
buttons = [
    ("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("4", 2, 0),
    ("5", 2, 1), ("6", 2, 2), ("7", 3, 0), ("8", 3, 1),
    ("9", 3, 2), ("0", 4, 1), ("+", 1, 3), ("-", 2, 3),
    ("*", 3, 3), ("/", 4, 3), ("=", 4, 2), (".", 4, 0),
    ("C", 4, 4), ("√", 5, 0), ("x^2", 5, 1), ("sin", 5, 2),
    ("cos", 5, 3), ("tan", 5, 4)
]

# Define button styles
button_styles = {
    "default": {"bg": "#D3D3D3", "fg": "black"},
    "operator": {"bg": "#87CEEB", "fg": "white"},
    "special": {"bg": "#FFA07A", "fg": "black"},
    "clear": {"bg": "#FF6347", "fg": "white"},
    "result": {"bg": "#87CEEB", "fg": "white"},
    "function": {"bg": "#90EE90", "fg": "black"}
}

# Create buttons and assign styles and commands based on their functions
for (text, row, column) in buttons:
    button_style = button_styles.get(text, button_styles["default"])
    button = tk.Button(root, text=text, padx=40, pady=20, font=("Arial", 12, "bold"), **button_style)
    
    # Assign commands based on button text
    if text == "=":
        button.config(command=calculate)
    elif text == "C":
        button.config(command=clear)
    elif text == "√":
        button.config(command=square_root)
    elif text == "x^2":
        button.config(command=exponent)
    elif text in ("sin", "cos", "tan"):
        button.config(command=lambda t=text: trigonometry(t))
    else:
        button.config(command=lambda t=text: entry.insert(tk.END, t))
    
    button.grid(row=row, column=column)

root.mainloop()  # Start the event loop
