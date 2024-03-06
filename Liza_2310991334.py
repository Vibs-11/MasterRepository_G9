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

def square_root(x):
    return math.sqrt(x)

def power(x, y):
    return x ** y

def logarithm(x, base):
    return math.log(x, base)

def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def calculator():
    print("Advanced Calculator")
    while True:
        print("\nOperations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square Root")
        print("6. Power")
        print("7. Logarithm")
        print("8. Factorial")
        print("9. Sine")
        print("10. Cosine")
        print("11. Tangent")
        print("0. Exit")

        choice = input("Enter operation (0-11): ")

        if choice == '0':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4', '6'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = add(num1, num2)
                print("Result: {}".format(result))
            elif choice == '2':
                result = subtract(num1, num2)
                print("Result: {}".format(result))
            elif choice == '3':
                result = multiply(num1, num2)
                print("Result: {}".format(result))
            elif choice == '4':
                result = divide(num1, num2)
                print("Result: {}".format(result))
            elif choice == '6':
                result = power(num1, num2)
                print("Result: {}".format(result))

        elif choice in ('5', '7', '8', '9', '10', '11'):
            num = float(input("Enter the number: "))

            if choice == '5':
                result = square_root(num)
                print("Result: {}".format(result))
            elif choice == '7':
                base = float(input("Enter the base for logarithm: "))
                result = logarithm(num, base)
                print("Result: {}".format(result))
            elif choice == '8':
                result = factorial(num)
                print("Result: {}".format(result))
            elif choice == '9':
                result = sin(num)
                print("Result: {}".format(result))
            elif choice == '10':
                result = cos(num)
                print("Result: {}".format(result))
            elif choice == '11':
                result = tan(num)
                print("Result: {}".format(result))

        else:
            print("Invalid choice. Please enter a valid operation (0-11).")

if __name__ == "__main__":
    calculator()
