# -*- coding: utf-8 -*-
"""
@author: Keshav
"""


#Object Oriented Programming - Program...
'''

DataTypes are of 3 types -

Inbuilt - (Int, String, FLoat)
        - (Tuple, Set, Dictionary, Lists)

Custom - Object Orient.

'''

#pokemon, digimon, dragonballz, naruto

# =============================================================================
# Pokemon
# =============================================================================
class pokemon():
    def x1(self, name, power):
        print("Name of this Pokemon is =", name)
        print("His special ability is =", power)

chalizard=pokemon()
chalizard.x1('Chalizard', 'Fire')

pikachu=pokemon()
pikachu.x1('Pikachu', 'Electric')

# =============================================================================
# Main Content
# =============================================================================

'''
There are 2 type of Var.

Global - var that can be used also outside of functions.
Local - var that can only be used inside of function.

'''


class KYC(): #This is called Blueprint...
    def x2(box, name, age): #Function = Method
        print("Name is =", name)
        print("age is =", age)
    
    def smlikes(box, fb, insta, youtube): #social media likes
        print('fb likes -', fb, 'insta likes -', insta, 'youtube likes -', youtube)
    #self is used to access variables that belongs to the class,
    #we can write anything for this, like instead of self we can write hacked
    #or anything....

obj1=KYC() #1
obj1.x2('ram', 55) #2

obj2=KYC()
obj2.smlikes(250, 650, 850)

obj3=KYC().smlikes(0, 1, 2)

obj1=KYC() #1
obj1.smlikes(44,44,44) #2

x=5

print (type(x))
print (type(obj1))






# below this will automatically expect integer, it will not accept string...