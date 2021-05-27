# -*- coding: utf-8 -*-
"""
@author: Keshav
"""

Name = "Krishna"
name = "Kanha"
n2 = " is "

new = name + n2 + Name

print(new[7])
print(len(new))

# =============================================================================
# loop for showing index value of each char.
# =============================================================================

for ram in range(5):
    print ("something")#this will print 5 times something.

for ram in range(len(new)):
    print(new, ram)#this will print 13 times(length of new) value of new
    
for ram in range(len(new)):
    print(ram)#as this is the name of for loop var, it will print counting
    
for ram in range(len(new)):
    print(new[ram])#this will print each char. in loop
    
for ram in range(len(new)):
    print(new[ram]," ",ram) #this will show each char with it's index value.
    
'''
Create a similar loop as above...



'''