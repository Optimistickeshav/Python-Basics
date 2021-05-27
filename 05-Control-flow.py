# -*- coding: utf-8 -*-
"""
@author: Keshav
"""
# =============================================================================
# Control Flow = if, else, elif, loops, 
# =============================================================================

'''
Control Flow is flow of control that we are setting in the program


'''

k = 'kevin'
aa = "kevin11"

j = '''This is a multi line string
this is a mnfafasfasf
asdfasdfafasdf
asdfadsf'''

t=510

if t != 50:
    print("Cake")
    
#else:
#    print('Apple')


# != NOT EQUAL TO - to check it is not equal to
# == to check - it is equal or not

#---------------------------------------------------------

#input() = to take input from user, we have to assign input in a var.
#input() function always take all variables as string..

tim = input()

tim = int(input())
tim=float(input())

#--------------------------------------------------------------

x = int(input())

if x < 5:
    print('x is less than 5')
    y=9+10
    print('value of y is =', y)
else:
    print("x is greater than 5")

#-----------------------------------------------------------

# =============================================================================
# elif = else if
# =============================================================================

a = 20

if a < 10:
    print('a is less than 10')
elif a == 10 or a == 20:
    print('a is greater than 10 and smaller than 20')
else:
    print('a is greater than 20')

'''
Operators 

= - TO ASSIGN A VALUE (ASSIGNMENT OPERATOR)
!= - (NOT EQUAL TO)
== - TO CHECK EQUAL TO

LOGICAL OPERATORS

and = 'cake' and 'apple' and 'banana'
or = 'cake' or 'apple' or 'banana'

'''
    for kite in range(1, 11):
    print(kite)
#----------------------------------------------------------