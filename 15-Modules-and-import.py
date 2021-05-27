# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 23:05:26 2021

@author: Keshav
"""

import square
print(square.area(10))
print(square.perimeter(10))

# =============================================================================
# one more style for writing the same as above
# =============================================================================


from square import area as a #area as a, 
print(a(5))
#print(perimeter(10))


# =============================================================================
# we can also write square as sq
# =============================================================================

import square as sq
print(sq.area(10))
print(sq.perimeter(10))

# =============================================================================
# importing list and dict.
# =============================================================================

import square as sq
print(sq.list1[3])
print(sq.dict1["Name"])

# =============================================================================
# we can import a particular single function from a sinle file also...
# =============================================================================

from square import dict1
#print(area(20))#it will not detect area as area is a different
#file in same function....

import square
dir(square) #it shows all the methods used in square file....

#like if we will use numpy library/module, 

import numpy
dir(numpy)#it will show the whole list of methods used in numpy