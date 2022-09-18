#1
print("Hello, {}!".format(input("Enter your name: ")))
#2
print("Entered number is : {}".format(int(input("Enter any number: "))))
#3
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = a + b
print("Sum of {} and {} is {}".format(a,b,c))
#4
a = int(input("Enter the radius: "))
print("Area of circle is {}".format(22.17*a**2))
#5
a = int(input("Enter any number: "))
print("Square of {} is {}".format(a, a**2))
#6
base = int(input("Enter the base value: "))
height = int(input("Enter the height value: "))
print("Area of the triangle is {}".format(0.5*base*height))
#7
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Average of {}, {}, {} is {}".format(a,b,c,(a+b+c)/3))
#8
r = 0.1
t = 5
p = int(input("Enter principal amount: "))
print("Final amount with simple interest is {}".format(p*(1+r*t)))
#9 
a = int(input("Enter length of cuboid: "))
b = int(input("Enter width of cuboid: "))
c = int(input("Enter height of cuboid: "))
print("Volume of cuboid is {}".format(a*b*c))
#10
l = int(input("Enter the length of rectangle: "))
b = int(input("Enter the breadth of rectangle: "))
print("Area of rectangle is {}".format(l*b))