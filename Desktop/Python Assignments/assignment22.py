#1
from re import A


def add(n):
    if n == 1:
        return 1
    return n + add(n-1)
print(add(10))
#2
def addOdd(n):
    if n == 1:
        return 1
    return (2*n)-1 + addOdd(n-1)
print(addOdd(5))
#3
def addEven(n):
    if n == 0:
        return 0
    return (2*n) + addEven(n-1)
print(addEven(5))
#4
def addSquares(n):
    if n == 1:
        return 1
    return n**2 + addSquares(n-1)
print(addSquares(5))
#5
def addCubes(n):
    if n == 1:
        return 1
    return n**3 + addCubes(n-1)
print(addCubes(5))
#6
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
print(fact(5))
#7
def addDigits(n):
    if n == 0:
        return 0
    return n % 10 + addDigits(n//10)
print(addDigits(554))
#10
def fib_nth_term(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib_nth_term(n-1) + fib_nth_term(n-2)
print(fib_nth_term(10))