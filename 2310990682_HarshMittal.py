import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def exponentiate(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def logarithm(x, base=math.e):
    return math.log(x, base)

def sine(x):
    return math.sin(x)

def cosine(x):
    return math.cos(x)

def tangent(x):
    return math.tan(x)

def main():
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exponentiate")
        print("6. Square root")
        print("7. Logarithm")
        print("8. Sine")
        print("9. Cosine")
        print("10. Tangent")
        print("11. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8/9/10/11): ")

        if choice in ['11', '12']:
            break

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
            print(num1, "^", num2, "=", exponentiate(num1, num2))
        elif choice == '6':
            print("Square root of", num1, "=", square_root(num1))
        elif choice == '7':
            print("Logarithm of", num1, "base", num2, "=", logarithm(num1, num2))
        elif choice == '8':
            print("Sine of", num1, "=", sine(num1))
        elif choice == '9':
            print("Cosine of", num1, "=", cosine(num1))
        elif choice == '10':
            print("Tangent of", num1, "=", tangent(num1))

if __name__ == "__main__":
    main()