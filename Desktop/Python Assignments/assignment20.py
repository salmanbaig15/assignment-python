#1
def my_func(lst):
    l2 = list(set(lst))
    return l2
print(my_func([1,1,2,3,4,4,5,5,5]))
#2
def my_func(num):
    for i in range(2,num):
        if num % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")
my_func(4)
my_func(5)
my_func(11)
#3
l = [1,2,3,4,5,6,7,8,9]
l1 = []
def my_func(lst):
    for i in lst:
        if i % 2 == 0:
            l1.append(i)
    print(l1)
my_func(l)
#4
def chk_pallindrome(s):
    if s.lower() == s[::-1].lower():
        print('Yes')
    else:
        print('No')
chk_pallindrome('Salman')
chk_pallindrome('Civic')
#5
def my_func(lst):
    print(min(lst))
my_func([1,2,3])
#6
def my_func(a,b):
    l = []
    for i in range(a,b+1):
        l.append(i**2)
    print(l)
my_func(1,30)
#7
def new_func(a,b):
    my_func(a,b)
new_func(1,10)
#8
def my_func(s):
    u_cnt = 0
    l_cnt = 0
    for i in s:
        if i == i.upper():
            u_cnt+=1
        else:
            l_cnt+=1
    print("In the string {}, count of upper-case letters is {} and lower-case letters is {}".format(s,u_cnt,l_cnt))
my_func('SalmanBaig')
#9
def is_pangram(s):
    s = len(set(s.replace(' ', '').lower()))
    if s == 26:
        print('Pangram', s)
    else:
        print('Not a Pangram', s)
is_pangram('Salman ')
is_pangram('The Quick Brown Fox jumps over the lazy dog')
#10
def is_anagram(s1,s2):
    if sorted(s1.lower()) == sorted(s2.lower()):
        print("{} and {} are anagrams".format(s1,s2))
    else:
        print("{} and {} are not anagrams".format(s1,s2))
is_anagram('Salman', 'Namlas')
is_anagram('Salman', 'Baig')