#1
n = int(input("Enter any number: "))
s = tuple([input("Enter element {}: ".format(i)) for i in range(1,n+1)])
print(s)
#2
s1 = tuple([input("Enter anything: ")])
print(s1)
#3
print("Reversing the above tuple {}".format(s[::-1]))
#4
print("Swapping two tuples")
s,s1 = s1,s
#5
t = (100,200,300,400)
print("Checking if all items in the tuple {} are same: {}".format(t,all(t)))
#6 unpacking
t = (100,200,300,400)
a,b,c,d = t
print(a,b,c,d)
#7
tuple1 = (1,2,3,4,5,6)
l = []
for i in range(len(tuple1)):
    if tuple1[i] == 4 or tuple1[i] == 5:
        l.append(tuple1[i])

print(tuple(l))
#8
tuple1 = (('a', 21), ('b', 37), ('c', 11), ('d',29))
print("Sorted tuple by second item: {}".format(sorted(tuple1, key=lambda x:x[1])))
#9
tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
print("Printing a value from the nested tuple {}".format(tuple1[1][1]))
#10
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print("Updated tuple: {}".format(tuple1))