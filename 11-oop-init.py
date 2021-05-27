# -*- coding: utf-8 -*-
"""
@author: Keshav
"""

#step 1 - Create Blueprint with it's method
class s: #Blueprint 
    def meth(self, name, age): #Method
        self.naam=name #It will become a global / Local Var.
        self.umer=age 
        pass 

#step 2 - Assign Blueprint to a new Var
#When we assign a blueprint to a Var, then the var is called Object.

obj_1 = s() 

#step 3 - Provide values to the method of blueprint
obj_1.meth("ram", 21)

#step 4 output or check...
print(obj_1.naam, obj_1.umer)

#-----------------------------------------------------------------

box =s()
box.meth('Rohit', 99)

#This shows naam is a global var...
print (box.naam)

#---------------------------------------------------------------

obj_2 = s()
obj_2.meth("jack", 33)

print(obj_2.umer)
print (age) 

# =============================================================================
# above is a normal program
# =============================================================================

# =============================================================================
# __init__ = initiated
# All the Input Values will come first in __init__ method then those value 
# will go somewhere else...
# =============================================================================

class new:
    
    def __init__(self, x, y):
       print('THis is Initialize Method')
    
    def a(self, x, y):
        print ('This is method A')
    
    def b(self, x, y):
        print ('This is method B')
    
    def c(self, x, y):
        print ('This is method C')

    def d(self, x, y):
        print ('This is method D')

#Direct Input
indo = new('ram', 22)

ram = new()
ram.a('ram', 44)

Bro = new()
Bro.b('Binod', 88)


#----------------------------------------------------------------

class z:
    def __init__(self, ram, kit):
        print("This code is working", ram, kit)
        
    def rock(self, ki, boss):
        print("new values are = ", "ki =", ki, "boss =", boss)

#as we haven't name the function, we used __init__(Initializing) that's why
#we don't have to mention the name of function..

obj1 = z ("ghost", 74)

obj2 = z.rock("oalien", 89)
obj3=z("ghosst", 714)
#it is used create custom and simple obj.

obj1.rock("kiiii", "bossssss")
#we have to tell the name with out __init__


# =============================================================================
# Global var or local var...
# =============================================================================






























