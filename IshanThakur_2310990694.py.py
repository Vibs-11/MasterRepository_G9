import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def logarithm(x, base):
    return math.log(x, base)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def main():
    print("Welcome to Calculator!")

    while True:
        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Logarithm")
        print("6. Trigonometric Functions")
        print("7. Exit")

        choice = input("Enter choice (1/2/3/4/5/6/7): ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))

        elif choice == '5':
            num = float(input("Enter a number: "))
            base = float(input("Enter the base for logarithm: "))
            print("Result:", logarithm(num, base))

        elif choice == '6':
            angle = float(input("Enter the angle in degrees: "))
            print("Sin:", sin(angle))
            print("Cos:", cos(angle))
            print("Tan:", tan(angle))

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid input!")

if __name__ == "__main__":
    main()
