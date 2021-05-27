# -*- coding: utf-8 -*-
"""
@author: Keshav
"""

'''
# ==========================================================================
# Tuple
# ==========================================================================
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python

(set, lists, dictionary, tuples)


used to store collections of data,
the other 3 are List, Set, and Dictionary,
all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

'''

list1 = ['asdfasf', 334, 5346.556, 2, 2, 2, 2,2 ,2]

list1.append(44) #to add a new value at the end of list

list1.insert(3, 'ram') #to add a new value on an index place
#-----------------------------------------------------------------

tuple1 = ('ram', 'kevin', 2, 3, 9, 5, 2, 2, 2, 2, 2) 

print (tuple1[4])

tup1 = ('one', 1, 2, 'one', 'ram', 'one', 6)

f= tuple1 + tup1

print (tup1[0:6:2])

print (tup1[:2])

#we can't insert a new value in pre-built tuple

tup1[1] = 'ram' #this will not add ram in tuple

tup1.count('one')

tup1.index('ram') #to know to index value of ram

print(tup1[3])

# =============================================================================
# Sets - Unordered Collection of Unique Objects 
# =============================================================================

myset = set()

set1 = {'ram', 'sam'}

set1.add(999)

set1[1] = 'new Value'

list1 = [1,2,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,3,34,4,4,4,5,5,55,5,5]

rock={'name':'ram', 'age':35}

myset2 = set(list1)
myset2 = set(rock)

print(min(myset2))

# =============================================================================
# Question
# =============================================================================

#output ???

nums = set([1,1,2,3,3,3,4,4])

print(len(nums))

'''

Suppose t = (1, 2, 4, 3), which of the following is incorrect?

print(t[3])

t[3] = 45

print(max(t))

print(len(t))

------------------------------



'''