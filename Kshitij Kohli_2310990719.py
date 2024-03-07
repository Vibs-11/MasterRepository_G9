import math

def main():
    print("Welcome to the Calculator with Logarithm and Angle Calculator\n")
    while True:
        print("Select operation:")
        print("1. Basic Calculator")
        print("2. Logarithm Calculator")
        print("3. Angle Calculator")
        print("4. Exit")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            basic_calculator()
        elif choice == '2':
            logarithm_calculator()
        elif choice == '3':
            angle_calculator()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid input. Please enter a valid choice.")

def basic_calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    operation = input("Enter choice (1/2/3/4): ")

    if operation == '1':
        print("Result:", num1 + num2)
    elif operation == '2':
        print("Result:", num1 - num2)
    elif operation == '3':
        print("Result:", num1 * num2)
    elif operation == '4':
        if num2 == 0:
            print("Error! Division by zero.")
        else:
            print("Result:", num1 / num2)
    else:
        print("Invalid operation")

def logarithm_calculator():
    num = float(input("Enter a number: "))
    base = float(input("Enter the base for logarithm calculation: "))

    if num <= 0 or base <= 0:
        print("Error! Number and base must be positive.")
    else:
        result = math.log(num, base)
        print("Result:", result)

def angle_calculator():
    angle_degrees = float(input("Enter angle in degrees: "))

    radians = math.radians(angle_degrees)

    print("Select operation:")
    print("1. Sine")
    print("2. Cosine")
    print("3. Tangent")

    operation = input("Enter choice (1/2/3): ")

    if operation == '1':
        print("Sine of", angle_degrees, "degrees is", math.sin(radians))
    elif operation == '2':
        print("Cosine of", angle_degrees, "degrees is", math.cos(radians))
    elif operation == '3':
        tangent = math.tan(radians)
        if abs(tangent) < 1e10:
            print("Tangent of", angle_degrees, "degrees is", tangent)
        else:
            print("Tangent of", angle_degrees, "degrees is undefined.")
    else:
        print("Invalid operation")

if __name__ == "__main__":
    main()
