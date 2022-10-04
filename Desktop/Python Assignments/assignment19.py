#1
def pr():
    print('MySirG')
pr()
#2
def arg(a,b):
    print(a,b)
arg(5,6)
#3
def arg(*a):
    print("arguments passed: {} which are {}".format(len(a),a))
arg(5,6,7,9)
#4
def kw(**kwargs):
    for i in kwargs.values():
        print(i)
kw(a=15,b=20,c=50)
#5
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)
#6
def my_function(a,b,c,d):
    return max(a,b,c,d)
print(my_function(4,2,7,1))
#7
def my_function(lst):
    r = 0
    for i in lst:
        r+=i
    print(r)
my_function([1,2,3,4,5])
#8
def my_function(lst):
    r = 1
    for i in lst:
        r*=i
    print(r)
my_function([1,2,3,4])
#9
def my_function(num):
    if num in range(1,10):
        print('Yes')
    else:
        print('No')
my_function(5)
my_function(11)
#10
def my_function(num):
    if num % 2 == 0:
        print('Even')
    else:
        print('Odd')
my_function(5)