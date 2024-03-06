print("**********************************************************************")
print("                :::::::::::::::Calculator:::::::::::::::\n")
print("             ::::Select a number to perform corresponding action:::: ")
print(
  " [1] for multiplication \n [2] for division \n [3] for subtraction \n [4] for exponent \n [5] for addition\n "
)


def multiplication(num1, num2):
  mul = num1 * num2
  print("Multiplication of the two nos. is ::", mul)
def division(num1, num2):
    div = num1/num2
    print("Division of the two nos. is ::", div)
def subtraction(num1, num2):
    sub = num1 - num2
    print("Subraction of the two nos. is ::", sub)
def exponent(num1, num2):
    expo = num1**num2
    print("Exponent of the two nos. is ::", expo)
def addition(num1, num2):
    add = num1 + num2
    print("Addition of the two nos. is ::", add)


Operation = int(input("Select the number from 1, 2, 3, 4, 5 :: "))

num1 = int(input("Enter the first number:: "))
num2 = int(input("Enter the Second number:: "))

if (Operation == 1):
  multiplication(num1, num2)

elif (Operation == 2):
  division(num1, num2)

elif (Operation == 3):
  subtraction(num1, num2)

else:
  exponent(num1, num2)
