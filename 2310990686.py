import math

print("Calculator to perform operations: ")
print("Select a number to perform the corresponding action: ")
print("1 for multiplication, 2 for division, 3 for subtraction, 4 for exponentiation, 5 for square root, 6 for factorial, 7 for logarithm (base 10): ")

def multiplication(num1, num2):
    mul = num1 * num2
    print("Multiplication of the two numbers is:", mul)

def division(num1, num2):
    if num2 != 0:
        div = num1 / num2
        print("Division of the two numbers is:", div)
    else:
        print("Error: Cannot divide by zero")

def subtraction(num1, num2):
    sub = num1 - num2
    print("Subtraction of the two numbers is:", sub)

def exponent(num1, num2):
    exp = num1 ** num2
    print("Exponentiation of the two numbers is:", exp)

def square_root(num):
    if num >= 0:
        sqrt_result = math.sqrt(num)
        print("Square root of the number is:", sqrt_result)
    else:
        print("Error: Cannot calculate square root of a negative number")

def factorial(num):
    if num >= 0:
        fact_result = math.factorial(int(num))
        print("Factorial of the number is:", fact_result)
    else:
        print("Error: Cannot calculate factorial of a negative number")

def logarithm(num):
    if num > 0:
        log_result = math.log10(num)
        print("Logarithm (base 10) of the number is:", log_result)
    else:
        print("Error: Cannot calculate logarithm of zero or a negative number")

def calculator():
    Operation = int(input("Select the number from 1 to 7: "))
    num1 = float(input("Enter the first number: "))

    if Operation in {1, 2, 3, 4, 6, 7}:
        num2 = float(input("Enter the Second number: "))

    if Operation == 1:
        multiplication(num1, num2)
    elif Operation == 2:
        division(num1, num2)
    elif Operation == 3:
        subtraction(num1, num2)
    elif Operation == 4:
        exponent(num1, num2)
    elif Operation == 5:
        square_root(num1)
    elif Operation == 6:
        factorial(num1)
    elif Operation == 7:
        logarithm(num1)
    else:
        print("Invalid operation")

# Run the calculator
calculator()
