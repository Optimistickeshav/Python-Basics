# -*- coding: utf-8 -*-
"""
@author: Keshav
"""

# =============================================================================
# Basic Functions
# =============================================================================

def fun1():
    print("yo yo")
        
fun1()

# =============================================================================
# Functions (A little more deep)
# =============================================================================

def fun2(ironman):
    print(ironman+" is Iron Man")

fun2('Tony Stark')

# =============================================================================
# Getting Multiple Values in a single Var of Functions...
# =============================================================================

def fun3(*name):
    return(name[0]+name[1]+name[2]+name[3])
    
ram=fun3(5, 6, 4, 3)

# =============================================================================
# Priority in Functions
# =============================================================================

def fun4(x1, x2="Ram"):
    print("Hello "+x1+ " and "+x2)
    
fun4("Keshav", "Rohit")

#it will give the first priority to this rohit not ram.
#To send the Output to store data in all stored variables 

# =============================================================================
# What if we don't input a Value...
# =============================================================================

def fun5(x1, x2):
    print("Hello "+x1+ " and "+x2)
    
fun5("Keshav")#it will show the error that x2 is missing.

# =============================================================================
# Creating a String using Function (Earlier Mentioned also)
# =============================================================================

def fun6(x1, x2):
   return("Hello "+x1+ " and "+x2)#this will submit the string
#   return(x1+x2)

#new1=fun6(4,6)
new2=fun6("ram", "kevin")

# =============================================================================
# addition function
# =============================================================================

def fun7(x1, x2):
    return x1+x2
x=fun7(20, 3)
print(x)

