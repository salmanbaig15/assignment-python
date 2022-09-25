#1
n = int(input("Enter any number: "))
res = 0
for i in range(1,n+1):
    res+=i
print("Sum of first {} natural numbers is: {}".format(n,res))
#2
n = int(input("Enter any number: "))
res = 0
for i in range(1,n+1):
    res+=i**2
print("Sum of squares of first {} natural numbers is: {}".format(n,res))
#3
n = int(input("Enter any number: "))
res = 0
for i in range(1,n+1):
    res+=i**3
print("Sum of cubes of first {} natural numbers is: {}".format(n,res))
#4
n = int(input("Enter any number: "))
res = 0
for i in range(1,2*n+1):
    if i%2!=0:
        res+=i
print("Sum of first {} odd natural numbers is: {}".format(n,res))
#5
n = int(input("Enter any number: "))
res = 0
for i in range(1,2*n+1):
    if i%2==0:
        res+=i
print("Sum of first {} even natural numbers is: {}".format(n,res))
#6
n = int(input("Enter any number: "))
fact = 1
for i in range(1,n+1):
    fact*=i
print("Factorial of {} is: {}".format(n,fact))
#7
n = int(input("Enter any number: "))
cnt = 0
for i in range(len(str(n))):
    cnt+=1
print("Entered number {} has {} digits".format(n,cnt))
#8
n = int(input("Enter any number: "))
sum = 0
for i in range(1,len(str(n))+1):
    sum+=i
print("Sum of digits in {} is: {}".format(n,sum))
#9
n = int(input("Enter any number: "))
res = '0b'
if n==0:
    res = '0b0'
else:
    for i in range(n):
            if 2**i > n:
                p = i-1
                break
            elif 2**i == n:
                p = i
                break
    lst = [0 for i in range(0,p+1)]

    # copying value of n to m
    m = n
    while m > 0:
        for i in range(m):
            if 2**i > m:
                p = i-1
                break
            elif 2**i == m:
                p = i
                break
        high = 2**p
        lst[-(p+1)] = 1
        m = m - high
    # updating the list
    for l in lst:
        res = res + str(l)

# printing final result
print("Binary equivalent of {} is: {}".format(n,res))
print("Does the program result ({}) match with built-in function result ({}): {}".format(res, bin(n), res == bin(n)))
#10
def decimalToOctal(n):
    return "{0:o}".format(int(n))
print("Octal version of the given number is {}".format(decimalToOctal(int(input("Enter any number: ")))))