import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y

def exponent(x, y):
    return x ** y

def logarithm(x, base):
    if x <= 0 or base <= 0:
        return "Error! Logarithm base and number must be positive."
    else:
        return math.log(x, base)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def sqrt(x):
    if x < 0:
        return "Error! Square root of negative number is not allowed."
    else:
        return math.sqrt(x)

def main():
    print("Select operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exponent")
    print("6.Logarithm")
    print("7.Sin")
    print("8.Cos")
    print("9.Tan")
    print("10.Square Root")

    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10): ")

    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
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
            print(num1, "^", num2, "=", exponent(num1, num2))
        elif choice == '6':
            base = float(input("Enter base: "))
            print(num1, "log base", base, "=", logarithm(num1, base))

    elif choice in ('7', '8', '9', '10'):
        num = float(input("Enter number: "))

        if choice == '7':
            print("sin", num, "=", sin(num))
        elif choice == '8':
            print("cos", num, "=", cos(num))
        elif choice == '9':
            print("tan", num, "=", tan(num))
        elif choice == '10':
            print("sqrt", num, "=", sqrt(num))

    else:
        print("Invalid input")

if __name__ == "main":
    main()