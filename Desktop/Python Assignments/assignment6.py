#1
a = int(input("Enter any number: "))
if a > 0:
    print("{} is a positive number".format(a))
else:
    print("{} is a non-positive number".format(a))
#2
a = int(input("Enter any number: "))
if a % 5 == 0:
    print("{} is divisible by 5".format(a))
else:
    print("{} is not divisible by 5".format(a))
#3
a = int(input("Enter any number: "))
if a % 2 == 0:
    print("{} is even".format(a))
else:
    print("{} is odd".format(a))
#4
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a>b:
    print("{} is greater".format(a))
else:
    print("{} is greater".format(b))
#5
a = input("Enter first word: ")
b = input("Enter second word: ")
if a>b:
    print("In dictionary order, {} is greater than {}".format(b, a))
else:
    print("In dictionary order, {} is greater than {}".format(a, b))
#6
a = int(input("Enter a 3 digit number: "))
if len(str(a)) != 3:
    print("{} is not a 3 digit number".format(a))
else:
    print("{} is a 3 digit number".format(a))
#7
a = int(input("Enter any number: "))
if a > 0:
    print("{} is positive".format(a))
elif a < 0:
    print("{} is negative".format(a))
else:
    print("{} is zero".format(a))
#8
print("Enter values a,b,c of a quadratic equation")
a,b,c = int(input("a: ")), int(input("b: ")), int(input("c: "))
d = b**2 - 4*a*c
if d > 0:
    print("Real and Distinct Roots")
elif d == 0:
    print("Real and Equal Roots")
else:
    print("Imaginary Roots")
#9
a = int(input("Enter any year: "))
if a%100==0 and a%400==0:
    print("{} is a leap year".format(a))
elif a%100!=0 and a%4==0:
    print("{} is a leap year".format(a))
else:
    print("{} is not a leap year".format(a))
#10
a,b,c = int(input("Enter number 1: ")), int(input("Enter number 2: ")), int(input("Enter number 3: "))
if a>b and a>c:
    print("{} is greater than {} and {}".format(a,b,c))
elif b>a and b>c:
    print("{} is greater than {} and {}".format(b,a,c))
else:
    print("{} is greater than {} and {}".format(c,a,b))
#11
a = int(input("Enter any month in numeric (1-12): "))
if a in (1,3,5,7,8,10,12):
    print("Month - {} has 31 days".format(a))
elif a == 2:
    print("Month - {} has 28 or 29 days".format(a))
else:
    print("Month - {} has 30 days".format(a))
#12
a = complex(input("Enter any complex number: "))
if a.real > a.imag:
    print("Real part is greater than Imaginary")
else:
    print("Real part is less than Imaginary")