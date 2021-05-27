# -*- coding: utf-8 -*-
"""
@author: Keshav
"""

# =============================================================================
# Basic Add Function
# =============================================================================

def add(x, y):
    return x+y

sum=add(2, 32)

print (sum)

# =============================================================================
# Recurrsion (it will print the sum of 1 to 10 digits)
# =============================================================================

'''n = 10


10+(10-1)= 9 it go back to the loop
10+9=19

n = 9
19+8 = 27
27+7 = 34
34+6 = 40
40+5 = 45
45+4 = 49
49+3 = 52
52+2 = 54
54+1 = 55
loop stops here as n = 1

9+(9-1)=8
'''

# return 1 = it is called stopping point

def sum(n):
    if n==1:
        return 1 #STOPPING POINT
    else:
        return n+sum(n-1) #END POINT AND RETURMIMG POINT

sum_1=sum(10)

print(sum_1)
# when we define a new Value in a fun with main fun name
# which is also inside a Fun,
# it changes the value of main fun
# Loop of a Function (When we call a fun inside a fun)
# it creates loop
# break continue and pass only works in loops(for and while)

'''
HOMEWORK

Create some functions of 
sum, subtraction, multiplication, square, cube.

'''