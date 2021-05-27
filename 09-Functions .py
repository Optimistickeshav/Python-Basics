# -*- coding: utf-8 -*-
"""
@author: Keshav
"""
# =============================================================================
# Function - Very Important topic of every prog. lang.
# A Placeholder of certain instruction to use a single code again and again on
# different different places.
# =============================================================================


x=5
y=6

def display():
    print('Value of x is', x, 'and value of y is', y)

x=int(input())
y=int(input())

display()
display()
display()


#-------------------------------------------
# Basic Function

def Robot():
     print('Hello World')
     
Robot()
Robot()
Robot()

# Function with Value...

def Robot2(k):
     print('Hello, I am', k)

     
Robot2('Keshav')
Robot2('Ram')
Robot2(55)

# Function : Input 2 values to get output....

def Stick(x, y):
    print('')
    z=x+y
    print('Sum of', x, 'and', y, '=', z)
   
x=int(input())
y=int(input())

Stick(x, y)

# Function: Multiple Declaration

def newf(a, b, c):
    print('Hello '+a+' and '+b+c)
   
newf('Rahul', 'Mohit', 'ram')

#it will give first priority to given fun value...

newf('Rahul', 'Anand')

# Function : Assigning Value to a Var using Return

def root(q, w):
    return('Value of q is = '+q+' and Value of w is = '+w)

x1 = root('Quality', 'Work')

def variable():
    return(55)
ss = variable()

def asdf():
    return(55.5)
float1 = asdf()

#return statement is used to assign value..
# =============================================================================
# fun() create, fun() inserting values, return, 
# =============================================================================

#Variables - 

# Local Var: A Var that only works inside a function only.
#Limited Scope

# Global Var: A var that can also be used out a functin.
