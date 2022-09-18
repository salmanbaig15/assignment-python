#1
n = int(input("Enter a number: "))
i = 0
while i<n:
    print("MySirG")
    i+=1
#2
n = int(input("Enter a number: "))
i = 1
print("Printing first {} natural numbers".format(n))
while i<=n:
    print(i, end=' ')
    i+=1
print()
#3
n = int(input("Enter a number: "))
i = n
print("Printing first {} natural numbers in reverse order".format(n))
while i>0:
    print(i, end=' ')
    i-=1
print()
#4
n = int(input("Enter a number: "))
i = 1
cnt = n
print("Printing first {} odd natural numbers".format(n))
while cnt>0:
    if i%2!=0:
        print(i, end=' ')
        cnt-=1
    i+=1
print()
#5
n = int(input("Enter a number: "))
i = 2*n
cnt = 1
print("Printing first {} odd natural numbers in reverse order".format(n))
while cnt<=n:
    if i%2!=0:
        print(i, end=' ')
        cnt+=1
    i-=1
print()
#6
n = int(input("Enter a number: "))
i = 1
cnt = n
print("Printing first {} even natural numbers".format(n))
while cnt>0:
    if i%2==0:
        print(i, end=' ')
        cnt-=1
    i+=1
print()
#7
n = int(input("Enter a number: "))
i = 2*n
cnt = 1
print("Printing first {} even natural numbers in reverse order".format(n))
while cnt<=n:
    if i%2==0:
        print(i, end=' ')
        cnt+=1
    i-=1
print()
#8
n = int(input("Enter a number: "))
i=1
print("Printing squares of first {} natural numbers".format(n))
while i<=n:
    print(i**2, end=' ')
    i+=1
print()
#9
n = int(input("Enter a number: "))
i=1
print("Printing cubes of first {} natural numbers".format(n))
while i<=n:
    print(i**3, end=' ')
    i+=1
print()
#10
n = int(input("Enter a number: "))
i=1
print("Printing first 10 multiples of {}".format(n))
while i<=10:
    print(n*i, end=' ')
    i+=1
print()