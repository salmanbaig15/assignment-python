#1
from random import sample


d = {'name':'salman', 'age':29, 'gender':'male'}
print(d, type(d))
#2
print("Accessing the dictionary items using its key")
print(d['name'])
#3
print("Printing list of values in a dictionary - {}".format(d.values()))
#4
print("Updating the name to Sam")
d['name'] = 'Sam'
print(d)
#5
print("Printing all the key names in the dictionary")
for i in d.keys():
    print(i)
#6
print("Nested dictionary")
master_dict = {'Name':{'Name':'Salman'},'Profile':{'Job': 'BA', 'Company':'Amazon'},'Tenure':{'Tenure':7}}
print(master_dict)
#7
d1 = {'Name':'Salman'}
d2 = {'Age':29}
d3 = {'Gender':'Male'}
d = {'Name':d1, 'Age':d2, 'Gender':d3}
print(d)
#8
l1 = ['Name', 'Age', 'Gender']
l2 = ['Salman', 29, 'Male']
d1 = {}
for i in range(len(l1)):
    d1[l1[i]] = l2[i]
print(d1)
#9
d1 = {'Name':'Salman'}
d2 = {'Age':29}
d1.update(d2)
print(d1)
#10
sample_dict = {'C':92, 'Python':66, 'Java':85}
m = min(sample_dict.values())
res = [key for key in sample_dict if sample_dict[key]==m]
print(str(res))