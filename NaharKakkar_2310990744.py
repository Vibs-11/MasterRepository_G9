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
        return x ** 0.5
    else:
        return "Invalid input for square root"

def exponent(x, y):
    return x ** y

def natural_log(x, terms=10):
    if x <= 0:
        return "Invalid input for natural logarithm"

    result = 0
    for n in range(1, terms + 1):
        result += ((-1) ** (n - 1)) * ((x - 1) ** n) / n
    return result

def factorial(n):
    if n < 0:
        return "Invalid input for factorial"

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def sin(x, terms=10):
    angle_radians = x
    result = 0
    for n in range(terms):
        result += ((-1) ** n) * (angle_radians ** (2 * n + 1)) / factorial(2 * n + 1)
    return result

def cos(x, terms=10):
    angle_radians = x
    result = 0
    for n in range(terms):
        result += ((-1) ** n) * (angle_radians ** (2 * n)) / factorial(2 * n)
    return result

def tan(x, terms=10):
    angle_radians = x
    sin_val = sin(x, terms)
    cos_val = cos(x, terms)
    if cos_val != 0:
        return sin_val / cos_val
    else:
        return "Undefined (cosine is zero)"

def arcsin(x, terms=10):
    result = 0
    for n in range(terms):
        result += factorial(2 * n) * (x ** (2 * n + 1)) / ((4 ** n) * (factorial(n) ** 2) * (2 * n + 1))
    return result

def arccos(x, terms=10):
    result = 0
    for n in range(terms):
        result += factorial(2 * n) * (x ** (2 * n)) / ((4 ** n) * (factorial(n) ** 2))
    return result

def arctan(x, terms=10):
    result = 0
    for n in range(terms):
        result += ((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)
    return result

def convert_base(num, from_base, to_base):
    
    decimal_num = int(str(num), from_base)

    
    if to_base == 2:
        return bin(decimal_num)[2:]
    elif to_base == 8:
        return oct(decimal_num)[2:]
    elif to_base == 10:
        return int(decimal_num)
    elif to_base == 16:
        return hex(decimal_num)[2:]

used_once = False

while not used_once:
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square")
    print("6. Square Root")
    print("7. Exponentiation")
    print("8. Natural Logarithm (ln)")
    print("9. Factorial")
    print("10. Sine (sin)")
    print("11. Cosine (cos)")
    print("12. Tangent (tan)")
    print("13. Arcsine (arcsin)")
    print("14. Arccosine (arccos)")
    print("15. Arctangent (arctan)")
    print("16. Convert Numeral System")

    choice = input("Enter choice (1-16): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")

    elif choice == '5':
        num = float(input("Enter the number: "))
        print(f"Square of {num} = {square(num)}")

    elif choice == '6':
        num = float(input("Enter the number: "))
        print(f"Square root of {num} = {square_root(num)}")

    elif choice == '7':
        base = float(input("Enter the base: "))
        exponent_val = float(input("Enter the exponent: "))
        print(f"{base} ^ {exponent_val} = {exponent(base, exponent_val)}")

    elif choice == '8':
        num = float(input("Enter the number for ln: "))
        print(f"Natural Logarithm of {num} = {natural_log(num)}")

    elif choice == '9':
        num = int(input("Enter a non-negative integer for factorial: "))
        print(f"Factorial of {num} = {factorial(num)}")

    elif choice == '10':
        angle = float(input("Enter the angle in radians for sin: "))
        print(f"Sine of {angle} radians = {sin(angle)}")

    elif choice == '11':
        angle = float(input("Enter the angle in radians for cos: "))
        print(f"Cosine of {angle} radians = {cos(angle)}")

    elif choice == '12':
        angle = float(input("Enter the angle in radians for tan: "))
        print(f"Tangent of {angle} radians = {tan(angle)}")

    elif choice == '13':
        num = float(input("Enter the value for arcsin (between -1 and 1): "))
        print(f"Arcsine of {num} = {arcsin(num)} radians")

    elif choice == '14':
        num = float(input("Enter the value for arccos (between -1 and 1): "))
        print(f"Arccosine of {num} = {arccos(num)} radians")

    elif choice == '15':
        num = float(input("Enter the value for arctan: "))
        print(f"Arctangent of {num} = {arctan(num)} radians")

    elif choice =='16':
        num = input("Enter the number: ")
        from_base = int(input("Enter the base of the number: "))
        to_base = int(input(f"Enter the base to convert: "))

        result = convert_base(num, from_base, to_base)
        print(f"Conversion: {num} in base {from_base} is equivalent to {result} in base {to_base}")

    else:
        print("Invalid input. Please enter a valid choice.")

    used_once = True


