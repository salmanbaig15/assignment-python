#1
def printN(n):
    if n>0:
        printN(n-1)
        print(n, end=' ')
printN(5)
print()
#2
def printN(n):
    if n>0:
        print(n, end=' ')
        printN(n-1)
printN(5)
print()
#3
def odd(n):
    if n==1:
        print(n, end=' ')
    else:
        odd(n-1)
        print((2*n)-1, end=' ')
odd(5)
print()
#4
def odd(n):
    if n==1:
        print(n, end=' ')
    else:
        print((2*n)-1, end=' ')
        odd(n-1)
odd(5)
print()
#5
def even(n):
    if n==0:
        return
    else:
        even(n-1)
        print((2*n), end=' ')
even(5)
print()
#6
def even(n):
    if n==0:
        return
    else:
        print((2*n), end=' ')
        even(n-1)
even(5)
print()
#7
def squares(n):
    if n == 1:
        print(n ** 2, end=' ')
    else:
        squares(n-1)
        print(n ** 2, end=' ')
squares(5)
print()
#8
def cubes(n):
    if n == 1:
        print(n ** 3, end=' ')
    else:
        cubes(n-1)
        print(n ** 3, end=' ')
cubes(5)
print()
#9
def printMultiples(num, n):
    if n > 0:
        printMultiples(num, n-1)
        print(num * n, end=' ')
printMultiples(5,10)
print()
#10
def printReverseOfNum(n):
    if len(str(n)) == 1:
        print(n, end='')
    else:
        print(n % 10, end='')
        printReverseOfNum(n//10)
printReverseOfNum(1593)
print()