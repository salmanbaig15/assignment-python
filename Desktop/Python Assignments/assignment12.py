#1
n = int(input("Enter any number: "))
m = n
rev = 0
#print("Reverse of {} is: {}".format(n, int(str(n)[::-1])))
while n!=0:
    d = n % 10
    rev = rev * 10 + d
    n = n // 10
print("Reverse of {} is: {}".format(m, rev))
#2
n = int(input("Enter any number: "))
for i in range(2,n):
    if n % i == 0:
        print("{} is not a prime number".format(n))
        break
else:
    print("{} is a prime number".format(n))
#3
print("Printing all prime numbers under 100")
for i in range(1,100):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i, end = ' ')
print()
#4
n1 = int(input("Enter starting number: "))
n2 = int(input("Enter ending number: "))
print("Prime numbers between {} and {} (both inclusive)".format(n1,n2))
for i in range(n1,n2+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i, end = ' ')
print()
#5
n = int(input("Enter any number: "))
for i in range(n+1, n+50):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print("Next prime number for the given number is {}".format(i))
        break
#6
n = int(input("Enter any number: "))
print("Printing first {} prime numbers".format(n))
cnt = 0
while cnt <= n:
    for i in range(1,3*n):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i, end = ' ')
        cnt+=1
print()
#7
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
# factors of n1
fact_n1 = []
# factors of n2
fact_n2 = []
for i in range(1,n1+1):
    if n1 % i == 0:
        fact_n1.append(i)
for i in range(1,n2+1):
    if n2 % i == 0:
        fact_n2.append(i)
# Finding common factors
res = set(fact_n1).intersection(set(fact_n2))
# highest common factor
hcf = max(res)
if hcf == 1:
    print("{} and {} are co-prime numbers".format(n1,n2))
else:
    print("{} and {} are NOT co-prime numbers".format(n1,n2))
#8
n = int(input("Enter any number: "))
print("Printing first {} terms of a fibonacci series".format(n))
a,b = 0,1
for i in range(1,n+1):
    print(a, end=' ')
    a,b=b,a+b
print()
#9
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
# factors of n1
fact_n1 = []
# factors of n2
fact_n2 = []
for i in range(1,n1+1):
    if n1 % i == 0:
        fact_n1.append(i)
for i in range(1,n2+1):
    if n2 % i == 0:
        fact_n2.append(i)
# Finding common factors
res = set(fact_n1).intersection(set(fact_n2))
# highest common factor or greatest common factor/divisor 
hcf = max(res)
lcm = (n1*n2)/hcf
print("LCM of {} and {} is {}".format(n1,n2,lcm))
#10
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
# factors of n1
fact_n1 = []
# factors of n2
fact_n2 = []
for i in range(1,n1+1):
    if n1 % i == 0:
        fact_n1.append(i)
for i in range(1,n2+1):
    if n2 % i == 0:
        fact_n2.append(i)
# Finding common factors
res = set(fact_n1).intersection(set(fact_n2))
# highest common factor or greatest common factor/divisor 
hcf = max(res)
print("HCF of {} and {} is {}".format(n1,n2,hcf))
