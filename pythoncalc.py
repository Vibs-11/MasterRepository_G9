import math
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def square(x):
    return x ** 2

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Cannot calculate square root of a negative number"

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def modulo(x, y):
    if y != 0:
        return x % y
    else:
        return "Cannot calculate modulo with zero divisor"

def log(x, base):
    if x > 0 and base > 0 and base != 1:
        return math.log(x, base)
    else:
        return "Invalid input for logarithm"


def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square")
    print("6. Square Root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Modulo")
    print("11. Logarithm")

    choice = input("Enter choice (1/2/3/4/5/6/7/8/9/10/11): ")

    num1 = float(input("Enter first number: "))

    if choice in ('1', '2', '3', '4', '5') :
        num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    elif choice == '5':
        print(num1, "squared =", square(num1))
    elif choice == '6':
        print("Square root of", num1, "=", square_root(num1))
    elif choice == '7':
        print("Sin(", num1, ") =", sin(num1))
    elif choice == '8':
        print("Cos(", num1, ") =", cos(num1))
    elif choice == '9':
        print("Tan(", num1, ") =", tan(num1))
    elif choice == '10':
        print(num1, "mod", num2, "=", modulo(num1, num2))
    elif choice == '11':
        base = float(input("Enter the logarithm base: "))
        print("Log base", base, "of", num1, "=", log(num1, base))
    else:
        print("Invalid input. Please enter a valid operator.")

calculator()
