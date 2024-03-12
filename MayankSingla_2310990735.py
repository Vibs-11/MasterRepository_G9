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

def exponentiate(x, y):
    return x ** y

def calculator():
    print("Advanced Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice not in ['1', '2', '3', '4', '5']:
        print("Invalid input")
        return

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")
    elif choice == '5':
        result = exponentiate(num1, num2)
        print(f"{num1} ^ {num2} = {result}")

if __name__ == "__main__":
    calculator()
