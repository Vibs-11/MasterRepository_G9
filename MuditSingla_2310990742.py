print("Calculator to perform operation:: ")
print(" Select a number to perform corresponding action: ")
print(
  " 1 for multiplication, 2 for division, 3 for subtraction,4 for addition, 5 for exponent:: "
)


def multiplication(num1, num2):
  mul = num1 * num2
  print("Multiplication of the two nos. is ::", mul)

def division(num1,num2):
  div=num1/num2
  print("Division of two nos. is ::",div)

def subtraction(num1,num2):
  sub=num1-num2
  print("Subtraction of two nos. is ::",sub)

def addition(num1,num2):
  add=num1+num2
  print("Addition of two nos. is ::",add)

def exponent(num1,num2):
  exp=num1**num2
  print("Exponent of two nos. ::",exp)

def square(num1):
  square=num1**2
  print("Square of no. is :: ",square)

def sqaure_root(num1):
  sqaureroot=num1**0.5
  print("Square root is :: ",sqaureroot)  

def log(num1, num2):
  return math.log(num1,num2)
  print("Log is :: ",math.log)


Operation = int(input("Select the number from 1, 2, 3, 4 ::"))

num1 = int(input("Enter the first number::"))
num2 = int(input("Enter the Second number::"))

if (Operation == 1):
  multiplication(num1, num2)

elif (Operation == 2):
  division(num1, num2)

elif (Operation == 3):
  subtraction(num1, num2)

elif(operation==4):
  addition(num1,num2)

elif(operation==5):
  exponent(num1)  

elif(Operation==6):
  square(num1)

elif(Operation==7):
  sqaure_root(num1)

elif(Operation==8):
  log(num1,num2)