import math

print("Calculator to perform operation:: ")
print(" Select a number to perform corresponding action: ")
print(
    " 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, "
    "5 for exponentiation, 6 for square root, 7 for trigonometric functions, "
    "8 for logarithm"
)


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    if num2 == 0:
        print("Error: Division by zero!")
    else:
        return num1 / num2


def exponentiation(num1, num2):
    return num1 ** num2


def square_root(num):
    if num < 0:
        print("Error: Cannot calculate square root of a negative number!")
    else:
        return math.sqrt(num)


def trigonometric_functions(num, func):
    if func == 'sin':
        return math.sin(math.radians(num))
    elif func == 'cos':
        return math.cos(math.radians(num))
    elif func == 'tan':
        return math.tan(math.radians(num))
    elif func == 'asin':
        return math.degrees(math.asin(num))
    elif func == 'acos':
        return math.degrees(math.acos(num))
    elif func == 'atan':
        return math.degrees(math.atan(num))
    else:
        print("Invalid trigonometric function!")


def logarithm(num, base):
    if num <= 0 or base <= 0 or base == 1:
        print("Error: Invalid input for logarithm!")
    else:
        return math.log(num, base)


Operation = int(input("Select the number from 1 to 8: "))

if Operation in [1, 2, 3, 4, 5]:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the Second number: "))
else:
    num = float(input("Enter the number: "))

if Operation == 1:
    print("Addition:", addition(num1, num2))
elif Operation == 2:
    print("Subtraction:", subtraction(num1, num2))
elif Operation == 3:
    print("Multiplication:", multiplication(num1, num2))
elif Operation == 4:
    print("Division:", division(num1, num2))
elif Operation == 5:
    print("Exponentiation:", exponentiation(num1, num2))
elif Operation == 6:
    print("Square Root:", square_root(num))
elif Operation == 7:
    func = input("Enter trigonometric function (sin, cos, tan, asin, acos, atan): ")
    print("Result:", trigonometric_functions(num, func))
elif Operation == 8:
    base = float(input("Enter the base for logarithm: "))
    print("Logarithm:", logarithm(num, base))
else:
    print("Invalid operation selected.")