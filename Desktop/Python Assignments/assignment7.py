#1
a = int(input("Enter any month in numeric (1-12): "))
match a:
    case a if a in (1,3,5,7,8,10,12):
        print("Month - {} has 31 days".format(a))
    case a if a in (4,6,9,11):
        print("Month - {} has 30 days".format(a))
    case a if a in (2):
        print("Month - {} has 28/29 days".format(a))
    case _:
        print("{} is not between 1-12".format(a))
#2
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
choice = int(input("What would you like to do? 1. Add 2. Subtract 3. Multiply 4. Divide "))
match choice:
    case 1:
        print("{} + {} = {}".format(a,b,a+b))
    case 2:
        print("{} - {} = {}".format(a,b,a-b))
    case 3:
        print("{} * {} = {}".format(a,b,a*b))
    case 4:
        print("{} / {} = {}".format(a,b,a/b))
    case _:
        print("Select an option from 1-4")
#3
print("Enter 3 numbers that denote sides of a triangle: ")
a,b,c = int(input("a: ")), int(input("b: ")), int(input("c: "))
print("Select any of the checks:")
print("1. Check if the sides form an equilateral triangle")
print("2. Check if the sides form an isosceles triangle")
print("3. Check if the sides form a right-angled triangle")
print("4. Exit")
d = int(input("Enter your choice from 1-4: "))
match d:
    case 1 if a==b==c:
        print("Equilateral Triangle")
    case 2 if (a==b and a==c) or (b==c and b==a) or (c==a and c==b):
        print("Isosceles Triangle")
    case 3 if ((a**2 + b**2) == c) or ((b**2 + c**2) == a) or ((a**2 + c**2) == b):
        print("Right-angled Triangle")
    case 4:
        exit()
    case _:
        print("Entered value not in 1-4")
#4
age = int(input("Enter your age: "))
match age:
    case age if age < 10:
        print("Kid")
    case age if age < 20:
        print("Teen")
    case age if age < 40:
        print("Young")
    case age if age < 60:
        print("Experienced")
    case age if age >= 60:
        print("Senior Citizen")
#5
num = int(input("Enter any number: "))
match num:
    case num if num%2==0:
        print("Saurabh Shukla")
    case num if num%2!=0 and num<0:
        print("Prateek Jain")
    case num if num%2!=0 and num>0:
        print("Aditya Choudhary")
#6
s = input("Enter any string: ")
match s:
    case s if len(s.split(' '))>1:
        print("Multi-word string")
    case s if len(s.split(' '))==1:
        print("Single-word string")
#7
n = int(input("Enter any number: "))
match n:
    case n if n>0:
        print("Positive")
    case n if n<0:
        print("Negative")
    case n if n==0:
        print("Zero")
#8
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
match (s1,s2):
    case (s1,s2) if s1==s2:
        print("Identical strings")
    case (s1,s2) if s1 > s2:
        print("{} comes after {}".format(s1,s2))
    case (s1,s2) if s2 > s1:
        print("{} comes after {}".format(s2,s1))
#9
y = int(input("Enter any year: "))
match y:
    case y if y % 100 == 0 and y % 400 == 0:
        print("Century Leap Year")
    case y if y % 100 == 0 and y % 400 != 0:
        print("Century non leap year")
    case y if y % 100 != 0 and y % 4 == 0:
        print("Non-century leap year")
    case y if y % 100 != 0 and y % 4 != 0:
        print("Non-century non leap year")
#10
a = input("Enter your favorite color: ").lower()
match a:
    case a if "yellow" in a:
        print("Monday")
    case a if "blue" in a:
        print("Tuesday")
    case a if "orange" in a:
        print("Wednesday")
    case a if "white" in a:
        print("Thursday")
    case a if "black" in a:
        print("Friday")
    case a if "red" in a:
        print("Saturday")
    case _:
        print("Sunday")