#1
n = int(input("Enter the number of items you want to input: "))
l = [eval(input("Enter item {}: ".format(i))) for i in range(1,n+1)]
print("Printing the list")
print(l)
#2
print("Getting datatypes of the above list")
for i in l:
    print(type(i), end=' ')
#3
print()
print("Getting the last item from the above list")
print(l[-1])
#4
print("Existing list")
mylist = ['Java', 'SQL', 'C', 'Reactnative', 'Javascript', 'Python']
print(mylist)
print("Updated list")
mylist[1]='NoSQL'
mylist[3]='Flutter'
print(mylist)
#5
print()
print("Adding a new item \'Test\' to the above list")
mylist.append('Test')
print(mylist)
#6
print()
firstlist = ['Java', 'Python', 'SQL']
secondlist = ['C', 'Cpp', 'NoSQL']
print("First list: ",firstlist)
print("Second List: ",secondlist)
print("Appending both")
print(firstlist + secondlist)
#7
print("Printing all the items from the below list")
print(firstlist)
for i in range(len(firstlist)):
    print(firstlist[i])
#8
print("Sorting the below list alphanumerically")
print(mylist)
print("Sorted: ", sorted(mylist))
#9
n = int(input("Enter the number of cities you want to input: "))
l = [input("Enter city {}: ".format(i)) for i in range(1,n+1)]
print("Printing the list")
print(l)
#10
n = int(input("Enter the count of numbers you want to input: "))
l = [int(input("Enter number {}: ".format(i))) % 10 for i in range(1,n+1)]
print(l)