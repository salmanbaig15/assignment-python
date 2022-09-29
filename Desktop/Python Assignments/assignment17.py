#1
s = {'SQL', 'Python', 'Java'}
print(s, type(s))
#2
s1 = {'Salman', 29, 'Male'}
print(s1, type(s1))
#3
print("Getting data types of the above set")
for i in s1:
    print(i, type(i))
#4
thisset = {"Java","Python", "Django"}
for i in thisset:
    if i == 'Python':
        print('Yes, {} is available in {}'.format(i,thisset))
        break
#5
thisset = {"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}
print(thisset.union(secondset))
#6
thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
print("Adding {} to set {}: {}".format(mylist,thisset,thisset.union(set(mylist))))
#7
thisset = {"Python", "Django", "JavaScript", "SQL"}
print("Removing last item from set: {}".format(thisset.pop()))
#8
del thisset
#9
thisset = {"Python", "Django", "JavaScript", "SQL"}
for i in thisset:
    print(i)
#10
print(max(thisset), min(thisset))