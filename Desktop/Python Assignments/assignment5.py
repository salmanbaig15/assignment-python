#1
a = int(input("Enter any number: "))
print("You entered {}. The result after removing the last digit is {}".format(a, a//10))
#2
a = int(input("Enter any number: "))
print("You entered {}. The last digit from your number is {}".format(a, a%10))
#3
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
a,b=b,a
print("Swapped Values for a and b are {} and {}".format(a,b))
#4
x = int(input("Enter a number: "))
y = int(input("Enter a number to be used as power: "))
print("{} raised to the power {} is {}".format(x,y,x**y))
#5
a = int(input("Enter any 3 digit number: "))
print("First digit of {} is {}".format(a, a//100))
#6
a = int(input("Enter any 3 digit number: "))
print("Middle digit of {} is {}".format(a, (a%100)//10))
#7
a = int(input("Enter any 3 digit number: "))
print("Last digit of {} is {}".format(a, (a%100)%10))
#8
l = [1,2,3]
a = int(input("Enter any number: "))
print("Checking availability of {} in {} = {}".format(a,l,a in l))
#9
l = [1,2,3,4,5]
a = int(input("Enter any number: "))
print("Checking unavailability of {} in {} = {}".format(a,l,a not in l))
#10
a = 5
b = 5
print(a is b)