import math

print("Calculator to perform operation:: ")

def addition(num1, num2):
    add = num1 + num2
    print("Addition of the two nos. is ::", add)

def multiplication(num1, num2):
    mul = num1 * num2
    print("Multiplication of the two nos. is ::", mul)

def division(num1, num2):
    div = num1 / num2
    print("Division of the two nos. is ::", div)

def subtraction(num1, num2):
    sub = num1 - num2
    print("Subtraction of the two nos. is ::", sub)

def exponent(num1, num2):
    exp = num1 ** num2
    print("Exponent of the two nos. is ::", exp)

def square_root(num):
    sqrt = math.sqrt(num)
    print("Square root of the number is ::", sqrt)

def cosine(num):
    cos_val = math.cos(math.radians(num))
    print("Cosine of the angle in degrees is ::", cos_val)

def sine(num):
    sin_val = math.sin(math.radians(num))
    print("Sine of the angle in degrees is ::", sin_val)

def tangent(num):
    tan_val = math.tan(math.radians(num))
    print("Tangent of the angle in degrees is ::", tan_val)

def logarithm(num):
    log_val = math.log10(num)
    print("Logarithm base 10 of the number is ::", log_val)

def factorial(num):
    fact_val = math.factorial(int(num))
    print("Factorial of the number is ::", fact_val)

operation = input("Select the operation: +, *, /, -, ^, sqrt, cos, sin, tan, log, fact :: ")

try:
    if operation in ['+', '*', '/', '-', '^']:
        num1 = float(input("Enter the first number::"))
        num2 = float(input("Enter the Second number::"))
    elif operation in ['sqrt', 'cos', 'sin', 'tan', 'log', 'fact']:
        num1 = float(input("Enter the number::"))
except ValueError:
    print("Invalid input. Please enter valid numerical values.")
    exit()

if operation == '+':
    addition(num1, num2)

elif operation == '*':
    multiplication(num1, num2)

elif operation == '/':
    division(num1, num2)

elif operation == '-':
    subtraction(num1, num2)

elif operation == '^':
    exponent(num1, num2)

elif operation == 'sqrt':
    square_root(num1)

elif operation == 'cos':
    cosine(num1)

elif operation == 'sin':
    sine(num1)

elif operation == 'tan':
    tangent(num1)

elif operation == 'log':
    logarithm(num1)

elif operation == 'fact':
    factorial(num1)

else:
    print("Invalid input. Please select a valid operation.")
