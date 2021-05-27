# -*- coding: utf-8 -*-
"""
@author: Keshav
"""

# =============================================================================
# Intro 
# =============================================================================

#This is a Comment, it won't execute...
print ("Hello World") #to print any statement

# =============================================================================
# Variables
# Datatypes - int, floats, string
# =============================================================================

x = "ram" #string
y = 55 #integer
z = 5.6 #float
PI = 3.14
s=11

a, b, c = 44, "boxes", 44.44654

x = y = z = 55

print (x)
print (PI)
PI =44

z=x+y

s=z-10
print(s)
q=w=e=98



x='ram'
ds=55.646
ats=5

type(ats)

print (type(ats))

print(type(x))
#to know the type of var.

h=5

h=5*5

print (h)

# =============================================================================
# Strings
# =============================================================================
s = [55, "This is String", 654.01]

foods = ['banana', 'abc', 5311, 513.614]

print (foods[1])


x1="Rohit"

x2=' Is a Working Hard'

print(x1+x2)

x3 = x1+x2

# garbage value = weird output from computer...

# =============================================================================
# Functions for Strings (upper, lower, split)
# =============================================================================

x3.upper()#to show anything in upper Char

# syntax to use function = varname.functionname()

newx3=x3.lower() #for lower case

x3_1=newx3.split()


#it will split every char and convert each into a list.

print(type(x3_1))

x3_2=newx3.split('i')#it will split on each i, rest remain together

#name age gender
#$

s='keshav 11 male'
s.split()

# =============================================================================
# index values
# =============================================================================

q2 = 'This is a moving car'

#................-3-2-1
# This is a moving car
# 0123456789..............

'''
fadfafafadsf ease = ram@gmail.com adsfadsfadfdf
Regex = Regular Expression
str111@str.str 
There are 2 basic data types in python - 
constant and var
cons = can't be change - like print, continue, break(these are predefined var.)
var = can be changed...
'''
print (q2[0:7:2])




print (q2)
print (q2[0])
print (q2[1])
print (q2[2])

print (q2[:7])
print (q2[8:])
print (q2[8:])
print (q2[0:-10])


print (q2[8:-4]) #starting point:stoping point

r = 'THIS IS MY CAR'
q=r

print (r[8:-4:2])#start:stop:step

print (r[0:4])

q=r[0:2]
w=r[2:4]

# =============================================================================
# Lists
# =============================================================================

cars = ['i20', 'XUV', 'Q8']

print ('Index value of 2 =', cars[2])

#This is a blank list
listnew=[]

#to add a new item in list
listnew.append('Fadsfasdf')

listnew.append(55)

list1=['TH', 'IS']


#This is a moving car
#0123456789

# =============================================================================
# length function (to calculate the length of a var)
# =============================================================================

print (len(q2))

len(r)
