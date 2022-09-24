#1
for i in range(1,11):
    print(5*i, end=' ')
print()
#2
n = int(input("Enter a number whose table you wanna print: "))
for i in range(1,11):
    print(n*i, end=' ')
print()
#3
n = int(input("Enter a number whose table you wanna print: "))
m = int(input("Enter till where you wanna print: "))
for i in range(1,m+1):
    print(n*i, end=' ')
print()
#4
n = int(input("Enter a number whose table you wanna print in reverse order: "))
for i in range(10,0,-1):
    print(n*i, end=' ')
print()
#5
n = int(input("Enter the table you wanna print: "))
print("Printing table of {} until 10".format(n))
for i in range(1,11):
    print(n*i, end = ' ')
print()
#6
n = int(input("Enter any number: "))
print("Printing first {} even natural numbers".format(n))
for i in range(1,2*n+1):
    if i%2==0:
        print(i, end=' ')
print()
#7
n = int(input("Enter any number: "))
print("Printing first {} odd natural numbers".format(n))
for i in range(1,2*n+1):
    if i%2!=0:
        print(i, end=' ')
print()
#8
n = int(input("Enter any number: "))
print("Printing squares of first {} natural numbers".format(n))
for i in range(1,n+1):
    print(i**2, end=' ')
print()
#9
n = int(input("Enter any number: "))
print("Printing cubes of first {} natural numbers".format(n))
for i in range(1,n+1):
    print(i**3, end=' ')
print()
#10
print("Printing prime numbers between 15 and 45")
for i in range(15,45):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i, end=' ')
print()