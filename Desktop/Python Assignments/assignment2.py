#1
# Statement to display "Learning Python" on screen
print("Learning Python")
#2
'''
This
is a 
multi line comment
'''
a,b,c,d = 5,2.5,"abc",True
print(a,b,c,d)
#3
a,b,c,d,e = 35, True, "MySirG", 5.46, 3+4j
print(type(a), type(b), type(c), type(d), type(e))
#4
a,b = 5,5
print(id(a), id(b))
#5
a,b,c,d = 35, 5.5, "Salman", True
print("Value = {}, Type = {}, ID = {}".format(a,type(a),id(a)))
print("Value = {}, Type = {}, ID = {}".format(b,type(b),id(b)))
print("Value = {}, Type = {}, ID = {}".format(c,type(c),id(c)))
print("Value = {}, Type = {}, ID = {}".format(d,type(d),id(d)))
#6
from datetime import date
from keyword import kwlist
from sqlite3 import Date, Time
print(kwlist)
#7
# help() and then keywords
#8
from assignment1 import a,b,c
print(a,b,c)
#10
from datetime import datetime
print(datetime.now().strftime("%d-%m-%Y"))
print(datetime.now().strftime("%I:%M %p"))