print("Calculator to perform operation:: ")
print("Select a number to perform corresponding action: ")

class grandparent():
    def __init__(self,num1):
        self.n1=num1
        
    def square(self):
        sq = self.n1 ** 2
        return sq

    def sq_root(self):
        sqr = self.n1 ** 0.5
        return sqr

    def ar_cir(self):
        if self.n1>0:
            ar=3.14*self.n1*self.n1
            return ar
        else:
            mes1="Radius cannot be negative or zero."
            return mes1
        
    def per_cir(self):
        if self.n1>0:
            per=2*3.14*self.n1
            return per
        else:
            mes1="Radius cannot be negative or zero."
            return mes1
    
    def dec_to_bin(self):
        return bin(self.n1)[2:]

    def dec_to_oct(self):
        return oct(self.n1)[2:]

    def dec_to_hex(self):
        return hex(self.n1)[2:]
    
    def deg_to_rad(self):
        rad=(pi/180)*self.n1
        return "{:.2f}".format(rad)

    def rad_to_deg(self):
        deg=(180/pi)*self.n1
        return "{:.2f}".format(deg)

    def factorial(self):
        fact=1
        if self.n1==0:
            return fact
        
        elif self.n1<0:
            mes="Factorial of negative numbers does not exist"
            return mes
        
        else:
            for i in range(1,self.n1+1):
                fact=fact*i
            return fact
            

    def sin(self):
        result = 0
        terms=10
        for n in range(terms):
            fact=1
            coe = (-1) ** n
            expo = 2 * n + 1
            for i in range(1,expo+1):
                fact=fact*i
            result += coe * (self.n1**expo) / fact
        return result

    def cos(self):
        result = 0
        terms=10
        for n in range(terms):
            fact=1
            coe = (-1) ** n
            expo = 2 * n
            for i in range(1,expo+1):
                fact=fact*i
            result += coe * (self.n1**expo) / fact
        return result

    def tan(self):
        result1 = 0
        result2 = 0
        terms=10
        for n in range(terms):
            fact=1
            coe = (-1) ** n
            expo = 2 * n + 1
            for i in range(1,expo+1):
                fact=fact*i
            result1 += coe * (self.n1**expo) / fact
        
        for n in range(terms):
            fact1=1
            coe = (-1) ** n
            expo1 = 2 * n
            for i in range(1,expo1+1):
                fact1=fact1*i
            result2 += coe * (self.n1**expo1) / fact1
            
        return result1/result2

    def arcsin(self):
        result = 0
        terms=100
        for n in range(terms):
            fact1=1
            fact2=1
            expo=2*n
            for i in range(1,expo+1):
                fact1=fact1*i
            for j in range(1,n+1):
                fact2=fact2*j
            coe = fact1  / ((4**n)*fact2 ** 2 * (2 * n + 1))
            result += coe * (self.n1 ** (2 * n + 1))
        return result

    def arccos(self):
        result = 0
        terms=100
        for n in range(terms):
            fact1=1
            fact2=1
            for i in range(1,2*n+1):
                fact1=fact1*i
            for j in range(1,n+1):
                fact2=fact2*j
            coe = fact1  / ((4**n)*fact2 ** 2 * (2 * n + 1))
            result += coe * (self.n1 ** (2 * n + 1))
            
        return (pi/2) - result

    def arctan(self):
        result = 0
        terms=100
        for n in range(terms):
            coe = (-1) ** n
            expo = 2 * n + 1
            result += coe * (self.n1**expo) / expo
        return result

    def ln(self):
        n = 1000.0
        return n * ((self.n1 ** (1/n)) - 1)
        
        
class parent(grandparent):
    def __init__(self,num2,num1):
        self.n2=num2
        grandparent.__init__(self,num1)
        
    def multiplication(self):
        mul = self.n1 * self.n2
        return mul

    def division(self):
        try:
            div=self.n1/self.n2
            return div
        except:
            er="Division by zero not possible"
            return er

    def subtraction(self):
        sub = self.n1 - self.n2
        return sub

    def addition(self):
        add = self.n1 + self.n2
        return add

    def power(self):
        expo =self.n1**self.n2
        return expo
    
    def percent(self):
        ans=(self.n1/self.n2)*100
        return ans


class child(parent):
    def __init__(self,num3,num2,num1):
        self.n3=num3
        parent.__init__(self,num2,num1)

    def tri(self):
        if self.n1>0 and self.n2>0 and self.n3>0:
            if self.n1+self.n2>self.n3 and self.n2+self.n3>self.n1 and self.n1+self.n3>self.n2:
                per=self.n1+self.n2+self.n3
                if Operation==10:
                    sem=per/2
                    ar=(sem*(sem-self.n1)*(sem-self.n2)*(sem-self.n3))**0.5
                    return ar

                elif Operation == 11:
                    return per
            else:
                mes2="Triangle not formed. Enter valid sides."
                return mes2
        else:
            mes3="Sides cannot be negative or zero."
            return mes3
    

class person():
    def __init__(self,num9):
        self.n9=num9

    def bin_to_dec(self):
        return int(self.n9,2)

    def oct_to_dec(self):
        return int(self.n9,8)

    def hex_to_dec(self):
        return int(self.n9,16)

    def bin_to_oct(self):
        z=int(self.n9,2)
        return oct(z)[2:]

    def oct_to_hex(self):
        z=int(self.n9,8)
        return hex(z)[2:]

    def bin_to_hex(self):
        z=int(self.n9,2)
        return hex(z)[2:]

    def oct_to_bin(self):
        z=int(self.n9,8)
        return bin(z)[2:]

    def hex_to_oct(self):
        z=int(self.n9,16)
        return oct(z)[2:]

    def hex_to_bin(self):
        z=int(self.n9,16)
        return bin(z)[2:]



print("*****************MENU*****************")
print("""1. Multiplication
2. Division
3. Subtraction
4. Addition
5. Exponential
6. Square of a number
7. Square root
8. Area of a circle
9. Perimeter of a circle
10. Area of a triangle
11. Perimeter of a triangle
12. Decimal to Binary
13. Decimal to Octal
14. Decimal to Hexadecimal
15. Binary to Decimal
16. Octal to Decimal
17. Hexadecimal to Decimal
18. Binary to Octal
19. Octal to Hexadecimal
20. Binary to Hexadecimal
21. Octal to Binary
22. Hexadecimal to Octal
23. Hexadecimal to Binary
24. Degree to Radian
25. Radian to Degree 
26. Factorial
27. Sine
28. Cos
29. Tan
30. Sin Inverse
31. Cos Inverse
32. Tan Inverse
33. Logarithm
34. Percentage
"""
      )

pi=3.141592653589793238462643383279502884197

while True:
    Operation = int(input("Select the number from menu:"))


    if Operation in (1,2,3,4,5,34):
        num1 = float(input("Enter the first number::"))
        num2 = float(input("Enter the Second number::"))
        p2=parent(num2,num1)
        if Operation == 1:
            print("Multiplication of",num1,"and",num2,"is",p2.multiplication())

        elif Operation == 2:
            print("Division of",num1,"by",num2,"is",p2.division())

        elif Operation == 3:
            print("Subtraction of",num2,"from",num1,"is",p2.subtraction())

        elif Operation == 4:
            print("Addition of",num1,"and",num2,"is",p2.addition())

        elif Operation == 5:
            print(num1,"raised to power",num2,"is",p2.power())

        elif Operation == 34:
            print(num1,"percent of",num2,"is",p2.percent())

    elif Operation in (6,7,8,9,24,25):

        if Operation == 6:
            num1=float(input("Enter number:"))
            p1=grandparent(num1)
            print("Square of",num1,"is",p1.square())

        elif Operation == 7:
            num1=float(input("Enter number:"))
            p1=grandparent(num1)
            print("Square root of",num1,"is",p1.sq_root())

        elif Operation == 8:
            num1=float(input("Enter radius:"))
            p1=grandparent(num1)
            print("Area of circle with radius",num1,"is",p1.ar_cir())

        elif Operation == 9:
            num1=float(input("Enter radius:"))
            p1=grandparent(num1)
            print("Perimeter of circle with radius",num1,"is",p1.per_cir())

        elif Operation == 24:
            num1=float(input("Enter number in degrees:"))
            p1=grandparent(num1)
            print(num1,"degrees is equal to",p1.deg_to_rad(),"radians")

        elif Operation == 25:
            num1=float(input("Enter number in radians:"))
            p1=grandparent(num1)
            print(num1,"radians is equal to",p1.rad_to_deg(),"degrees")

    elif Operation in (12,13,14,15,16,17,18,19,20,21,22,23,26,33):
        if Operation in(12,13,14,26,33):
            num1=int(input("Enter number:"))
            p1=grandparent(num1)
            if Operation == 12:
                print("Decimal number",num1,"is equal to binary number",p1.dec_to_bin())
            elif Operation == 13:
                print("Decimal number",num1,"is equal to octal number",p1.dec_to_oct())
            elif Operation == 14:
                print("Decimal number",num1,"is equal to hexadecimal number",p1.dec_to_hex())
            elif Operation == 26:
                print("Factorial of",num1,"is",p1.factorial())
            elif Operation == 33:
                print("Natural Logarithm of",num1,"is",p1.ln())

        elif Operation in (15,16,17,18,19,20,21,22,23):
            num9=input("Enter number:")
            p9=person(num9)
            if Operation==15:
                print("Binary number",num9,"is equal to decimal number",p9.bin_to_dec())
            elif Operation==16:
                print("Octal number",num9,"is equal to decimal number",p9.oct_to_dec())
            elif Operation==17:
                print("Hexadecimal number",num9,"is equal to decimal number",p9.hex_to_dec())
            elif Operation==18:
                print("Binary number",num9,"is equal to octal number",p9.bin_to_oct())
            elif Operation==19:
                print("Octal number",num9,"is equal to hexadecimal number",p9.oct_to_hex())
            elif Operation==20:
                print("Binary number",num9,"is equal to hexadecimal number",p9.bin_to_hex())
            elif Operation==21:
                print("Octal number",num9,"is equal to binary number",p9.oct_to_bin())
            elif Operation==22:
                print("Hexadecimal number",num9,"is equal to octal number",p9.hex_to_oct())
            elif Operation==23:
                print("Hexadecimal number",num9,"is equal to binary number",p9.hex_to_bin())

    elif Operation in (10,11):
        num1=float(input("Enter first side:"))
        num2=float(input("Enter second side:"))
        num3=float(input("Enter third side:"))
        p3=child(num3,num2,num1)
        if Operation ==10:
            print("Area of triangle is",p3.tri())
        elif Operation==11:
            print("Perimeter of triangle is",p3.tri())

    elif Operation in (27,28,29,30,31,32):
        num1=float(input("Enter value:"))
        p1=grandparent(num1)
        if Operation ==27:
            print("sin({}):".format(num1), p1.sin())
        elif Operation ==28:
            print("cos({}):".format(num1), p1.cos())
        elif Operation ==29:
            print("tan({}):".format(num1), p1.tan())
        elif Operation==30:
            print("arcsin({}):".format(num1), p1.arcsin())
        elif Operation==31:
            print("arccos({}):".format(num1), p1.arccos())
        elif Operation==32:
            print("arctan({}):".format(num1), p1.arctan())
    
    ch=input("Enter choice(y/n):")
    if ch.lower()=="y":
        continue
    else:
        break