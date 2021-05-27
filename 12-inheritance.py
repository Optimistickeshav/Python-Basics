# -*- coding: utf-8 -*-
"""
@author: Keshav
"""

'''
This concept is called inheritance...


Grandfather >> 

        Father1>>
        
            Son1 >
                Son-son2
            
            Son2
            
        Uncle>>
        
            Son1
            Son2
            Daoughter
        


'''


# =============================================================================
# single inheritance
# =============================================================================

class father:
    def meth1(self):
        print("this is meth1")
        
    def meth2(self):
        print("this is meth2")

r = father()

r.meth1()

r.meth2()

# =============================================================================
# Multiple Inheritance - using a class in another class
# =============================================================================
        
class son(father): # here son is using father's property
    def meth3(self):
        print("this is meth3")
        
    def meth4(self):
        print("this is meth4")

ss=son()

ss.meth4()

ss.meth2()
        
d=son() #blueprint father will work, and output from father will be assigned
           #to d

d.meth2()

