import math
a= float(input("Enter the value of a "))
b=float(input("Enter the value of b "))
ope=input("Select the operator ")
if ope =='+':
    print("Your answer",a+b)
elif ope =='-':
    print("Your answer",a-b)
elif ope =='*':
    print("Your answer",a*b)
elif ope=='/':
    print("Your answer",a/b)
elif ope == "^":
    output = math.pow(a,b)
    print("Your Answer: "+str(output))
elif ope == "/-":
    output = math.sqrt(a)
    print("Your Answer: "+str(output))
elif ope == "sin":
    if(1>=a>=0):
        output = math.sin(a)
        print("Your Answer: "+str(output))
    elif(a>1):
        print("Out of Range")
elif ope == "cos":
    if(1>=a>=0):
        output = math.cos(a)
        print("Your Answer: "+str(output))
    elif(a>1):
        print("Out of Range")
elif ope == "tan":
    output = math.tan(a)
    print("Your Answer: "+str(output))
elif ope == "log10":
    output = math.log10(a)
    print("Your Answer: "+str(output))
elif ope == "log":
    output = math.log(b,a)
    print("Your Answer: "+str(output))

else:
    print("Invalid")


