# -*- coding: utf-8 -*-
"""
@author: Keshav
"""

# =============================================================================
# Loops with lists.. (Add chars in a list using loop)
# =============================================================================

list=[]

s="ram verma"

for x in s:
    list.append(x)
    
# =============================================================================
# Shorthand of above program... (To add chars in a list using loop)
# =============================================================================

k = 'KING Keshav'

list2 = [tt for tt in k]

# =============================================================================
# a for loop to print sq from 2 to 10
# =============================================================================

num=1
k=[num**2 for num in range(0, 11)]

# num**2 will make the sq of num,
# num to the power of 2, as num is not defined
# it's value will be considered as 0

# To print Square from 2 to 20 in a list

Squarelist=[s**2 for s in range(1, 21)]

# =============================================================================
# for loop to print sq of odd numbers and cube of even numbers (if else)
# =============================================================================

# % Modulas Operator = 
'''

this is basic divide
x=2
y=5
z=y/x

modulas operator

z=y%x

'''


slist21=[num**2 if num%2==0 else num**3 for num in range(0, 11)]
