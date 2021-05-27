# -*- coding: utf-8 -*-
"""
@author: Keshav
"""

class dog():
    def __init__(self1, breed): #breed here is a local var.
        self1.breed_1=breed #breed_1 is a global var.
        print("Working...", breed)

    def meth(self, name, age):
        self.name_1=name #^^^^^^
        self.age_1=age
        print(self.name_1, self.age_1)
    
    def meth2(self):
        self.meth("keshav", 21) #to send values from 1 function to other in a
        print("hi, this is meth 2")#class
        
obj_1 = dog("Labrador") #assigning objects
obj_2 = dog("Wild")

print ('Value of Global Keyword obj_1.breed_1 =', obj_1.breed_1)

#calling object
obj_1.meth("kevin11", 19) #^^^^^^

obj_1.meth2()

obj_2.meth("ben10", 18)
obj_2.meth2()

print(obj_1.name_1)
