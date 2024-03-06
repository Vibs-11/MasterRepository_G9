import math

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
  return num1 * num2

def divide(num1, num2):
  if num2 == 0:
        return "Error! Division by zero is not allowed."
  else:
        return num1 / num2

def square_root(num1):
  return math.sqrt(num1)

def exponentiate(num1,num2):
  return num1 ** num2

def factorial(num1):
  return math.factorial(num1)

def log(num1):
  return math.log(num1)

def sin(num1):
    return math.sin(num1)

def cos(num1):
    return math.cos(num1)

def tan(num1):
    return math.tan(num1)

def main():
  print("Calculator to perform operation:: ")
print(" Select a number to perform corresponding action: ")
print("1 for addition")
print("2 for subtraction")
print("3 for multiplication")
print("4 for division")
print("5 for square root")
print("6 for exponent")
print("7 for factorail")
print("8 for log with base 2")
print("9 for sin")
print("10 for cos")
print("11 for tan :: ")

Operation = int(input("Select the number from 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ::"))

num1 = int(input("Enter the first number::"))
num2 = int(input("Enter the Second number::"))
if(Operation ==1):
   print("Addition of num1 and num2 : ",add(num1, num2))

elif(Operation ==2):
   print("Subtration og num1 and num2 : ",subtract(num1,num2))

elif (Operation == 3):
 print("Multiplication : ",multiplication(num1, num2))

elif(Operation==4):
   print("Division of num1 and num2 gives : ",divide(num1,num2))

elif (Operation == 5):
  print("Square root of num1 : ",square_root(num1))
  print("Square root of num2 : ",square_root(num2))

elif (Operation == 6):
  print("Exponential : ",exponentiate(num1,num2))

elif (Operation == 7):
  print("Factorial of num1 : ",factorial(num1))
  print("Factorial of num2 : ",factorial(num2))

elif(Operation ==8):
  print("Log with base 2 of num1 : ",log(num1))
  print("Log with base 2 of num2 : ",log(num2))

elif(Operation ==9):
  print("Sin of num1 : ",sin(num1))
  print("Sin of num2 : ",sin(num2))

elif(Operation ==10):
  print("Cos of num1 : ",cos(num1))
  print("Cos of num2 : ",cos(num2))

elif(Operation ==11):
  print("Tan of num1 : ",tan(num1))
  print("Tan of num2 : ",tan(num2))

else:
  print("Invalid Input")

if __name__ == "main":
    main()