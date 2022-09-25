#1
n = int(input("Enter any number: "))
print("Creating a list of first {} natural numbers".format(n))
l = [i for i in range(1,n+1)]
print(l)
#2
print("Creating a list of first {} odd natural numbers".format(n))
l = [i for i in range(1,2*n+1) if i % 2 != 0]
print(l)
#3
print("Creating a list of first {} even natural numbers".format(n))
l = [i for i in range(1,2*n+1) if i % 2 == 0]
print(l)
#4
print("The greatest number from the list {} is {}".format(l,max(l)))
#5
print("The smallest number from the list {} is {}".format(l,min(l)))
#6
print("Sum of elements in the list {} is {}".format(l, sum(l)))
#7
mylist = ['SQL', 15, 15.6, '3+4j', 25]
print("Removing the non int values from the list {}".format(mylist))
newlist = [i for i in mylist if type(i) == int]
print("Updated list is {}".format(newlist))
#8
l = ['SQL', 'SQL', 'SQL', 'Python', 'Python']
unq_l = list(set(l))
print("Counting elements in the list {}".format(l))
for i in range(len(unq_l)):
    print("Element {} - Count {}".format(unq_l[i], l.count(unq_l[i])))
#9
print("In the list {}, element \'SQL\' appears at indices:".format(l))
for i in range(len(l)):
    if l[i] == 'SQL':
        print(i, end=' ')
print()
#10
l = [5,37,3,4,1,12]
print("Sorted version of the list {} is {}".format(l, sorted(l)))