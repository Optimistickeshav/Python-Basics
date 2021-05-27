# -*- coding: utf-8 -*-
"""
@author: Keshav
"""

# =============================================================================
# Loops 
# =============================================================================

# to print anything in a loop

# For Loop

for great in range(11):
    print(great, ' This is a  Loop')


#to print hello 30 times
for num in range(30):
	print('Hello', num)

#to print no. 3 times because string size is 3
for num in 'THIS IS SOMETHING':
	print(num)

#to print sum of set/tuple[]

x2 = 0
for num in [1, 2, 3, 4, 5]:
	x2=x2+num
   
print (x2)
'''
0+1 = 1
1+2 = 3
3+3 = 6
6+4 =10
10+5 = 15

0+1 = 1=x2
x2 = 1
    1+2= 3
x2 = 3
 3+4 = 7
 7+5


'''    

#to print dict key
dict1 = {'k1':5, 'k2':2, 'k3':7}
for x in dict1:
	print (x)
    
#to print dict value
dict1 = {'k1':5, 'k2':2, 'k3':7}
for x in dict1.values():
	print (x)

#to print no. of values in dict
dict1 = {'k1':5, 'k2':2, 'k3':7}
for x, values in dict1:
	print (values)

#to print whole dictionary
dict1 = {'k1':5, 'k2':2, 'k3':7}
for x in dict1.items():
	print (x)

# =============================================================================
# Loop with Indexing
# =============================================================================

#to run loop 5 times
for x in range(1, 6):
    print (x, "THIS IS LOOP")

#to start loop from 1 and end on 11, it will show output 1-10
for kite in range(1, 11):
    print(kite, 'this is kite')

#to start loop from 1 and end on 10,
#and show each 2nd value, it will show output 1, 3, 5, 7, 9

# 1 3 5 7 9

for x in range(1, 10, 2):
    print ("THIS IS LOOP", x)


# Table

for t in range(1, 11):
    print ('2 X', t, '=', 2*t)

#for square and cube
x=5
s=x**2
print (s)

y=3
cube=3**3
print(cube)


#customized table    
table=int(input())
for u in range(1, 11):
    print (table, 'x', u, '=', table*u)
    
'''

HOMEWORK

- Create table of 9 from 1 to 20.
- Create a Loop to print squares from 2 to 20.

'''