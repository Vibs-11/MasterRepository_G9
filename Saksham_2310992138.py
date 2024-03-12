import tkinter as tk
import math

# Function definitions
def clear():
    for entry in entry_fields:
        entry.delete(0, tk.END)
    result_label.config(text="Result:", fg="black")

def calculate():
    try:
        nums = [float(entry.get()) for entry in entry_fields]

        if operation_var.get() in ["Add", "Subtract", "Multiply", "Divide"]:
            if operation_var.get() == "Add":
                result = sum(nums)
            elif operation_var.get() == "Subtract":
                result = nums[0] - sum(nums[1:])
            elif operation_var.get() == "Multiply":
                result = 1
                for num in nums:
                    result *= num
            elif operation_var.get() == "Divide":
                if 0 in nums[1:]:
                    result_label.config(text="Error: Division by zero", fg="red")
                    return
                else:
                    result = nums[0] / math.prod(nums[1:])
        elif operation_var.get() == "Square Root":
            result = math.sqrt(nums[0])
        elif operation_var.get() == "Cube Root":
            result = nums[0] ** (1/3)
        elif operation_var.get() == "Sine":
            result = math.sin(math.radians(nums[0]))
        elif operation_var.get() == "Cosine":
            result = math.cos(math.radians(nums[0]))
        elif operation_var.get() == "Tangent":
            result = math.tan(math.radians(nums[0]))

        result_label.config(text=f"Result: {result}", fg="black")
    except ValueError:
        result_label.config(text="Error: Invalid input", fg="red")

def update_inputs(*args):
    operation = operation_var.get()

    for entry in entry_fields:
        entry.destroy()
    entry_fields.clear()

    if operation in ["Add", "Subtract", "Multiply", "Divide"]:
        num_inputs = int(num_inputs_var.get())
        for i in range(num_inputs):
            entry = tk.Entry(window)
            entry.grid(row=i+6, column=1, padx=5, pady=5)
            entry_fields.append(entry)
    else:
        entry = tk.Entry(window)
        entry.grid(row=6, column=1, padx=5, pady=5)
        entry_fields.append(entry)

    clear()
    if operation in ["Square Root", "Cube Root", "Sine", "Cosine", "Tangent"]:
        window.config(bg="lightblue")
    else:
        window.config(bg="white")

# Create main window
window = tk.Tk()
window.title("Dynamic Calculator")
window.config(bg="white")

# Operation selection
label_operation = tk.Label(window, text="Select operation:", bg="white")
label_operation.grid(row=0, column=0, padx=5, pady=5)
operation_var = tk.StringVar()
operation_var.set("Add")
operations = ["Add", "Subtract", "Multiply", "Divide", "Square Root", "Cube Root", "Sine", "Cosine", "Tangent"]
option_menu_operation = tk.OptionMenu(window, operation_var, *operations, command=update_inputs)
option_menu_operation.grid(row=0, column=1, padx=5, pady=5)

# Number of inputs selection
label_num_inputs = tk.Label(window, text="Number of inputs:", bg="white")
label_num_inputs.grid(row=1, column=0, padx=5, pady=5)
num_inputs_var = tk.StringVar()
num_inputs_var.set("2")
option_menu_num_inputs = tk.OptionMenu(window, num_inputs_var, *map(str, range(1, 11)), command=update_inputs)
option_menu_num_inputs.grid(row=1, column=1, padx=5, pady=5)
num_inputs_var.trace_add("write", update_inputs)

# Create widgets
entry_fields = []
for i in range(2):
    entry = tk.Entry(window)
    entry.grid(row=i+6, column=1, padx=5, pady=5)
    entry_fields.append(entry)

button_clear = tk.Button(window, text="Clear", command=clear)
button_clear.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

button_calculate = tk.Button(window, text="Calculate", command=calculate)
button_calculate.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

result_label = tk.Label(window, text="Result:", bg="white")
result_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Run the main event loop
window.mainloop()