print("**********************************************************************")
print("                :::::::::::::::Calculator:::::::::::::::\n")
print("             ::::Select a number to perform corresponding action:::: ")
print(
  " [1] for multiplication \n [2] for division \n [3] for subtraction \n [4] for exponent \n [5] for addition\n [6] for factorial\n "
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
def factorial(num1):
    fact = 1
    for i in range(1,num1+1):
        fact=fact*i
    print("Factorial of First Number is=", end=" ")
    print(fact)
def factorial2(num2):
    fact1 = 1
    for j in range(1,num2+1):
        fact1=fact1*j
    print("Factorial of First Number is=", end=" ")
    print(fact1)
    
#     fact1 = 1
#     for j in range(1,num2+1):
#         fact2=fact*j
#     print("Factorial of Second Number is=", end=" ")
#     print(fact2)
    


Operation = int(input("Select the number from 1, 2, 3, 4, 5, 6 :: "))

num1 = int(input("Enter the first number:: "))
num2 = int(input("Enter the Second number:: "))

if (Operation == 1):
 multiplication(num1, num2)

elif (Operation == 2):
  division(num1, num2)

elif (Operation == 3):
  subtraction(num1, num2)

elif (Operation == 4):
  exponent(num1, num2)

elif (Operation == 5):
    addition(num1, num2)

else:
  factorial(num1)
  factorial2(num2)

