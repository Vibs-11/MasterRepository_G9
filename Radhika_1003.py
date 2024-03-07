print("Calculator to perform operation:: ")
print(" Select a number to perform corresponding action: ")
print(
  " 1 for multiplication, 2 for division, 3 for subtraction, 4 for exponent:: "
)


def multiplication(num1, num2):
  mul = num1 * num2
  print("Multiplication of the two nos. is ::", mul)


Operation = int(input("Select the number from 1, 2, 3, 4 ::"))

num1 = int(input("Enter the first number::"))
num2 = int(input("Enter the Second number::"))

if (Operation == 1):
  multiplication(num1, num2)

elif (Operation == 2):
  division(num1, num2)

elif (Operation == 3):
  subtraction(num1, num2)

else:
  exponent(num1, num2)
