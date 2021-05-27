# -*- coding: utf-8 -*-
"""
@author: Keshav
"""

# =============================================================================
# While loop
# =============================================================================

'''
Stock of a product

stock 99 books

books = 10 - email(getbooks)

99,98,97...........50.............20.......12....11..10

_______________________________________________________________
DOUBTS

books = 1

while books>=110:
    books=books+1
    print('Books are getting out of stock !', books)
    

num+=1
    
    
'''



i = 1 #initialize

while i<=5: #condition
	print ("value of i is ", i)
	i=i+1 #increment


# =============================================================================
# While and while else
# =============================================================================
num=1

while num<10:
	print('Hello', num)
	num=num+1 # num+=1
else:
    print('num is greater than or equal to 10')
    
# =============================================================================
#  While TRUE / False
# =============================================================================

while True:
    print ('this is run infinite')
else:
    print('this is something else')
    
# =============================================================================
# break = it break the loop on point.
# continue = it will keep continue the while loop and will not print the below
#            statement.
# pass = if no need of output.
#        it will pass the loop completly with it's final value.
# =============================================================================

# Break
num=0
while True:
    num=num+1
    if num==4:
        break
    print('Hello', num)
    
# Continue
num=0
while num<10:
    num=num+1 # shorthand = num+=1 / num-=1
    if num==4:
        print('This is saperatly 4')
        continue
    print('Hello', num)

# Pass

num = 0
while True:
    pass

for x in range(10):
    pass
print('this is something')
    

# =============================================================================
# % Modulas Operator
# =============================================================================



'''
While loop - it runs until the condition is true
           - (limited data type)

For Loop - it runs in a range
         - (support maximum data type)
         
         
Python Library - Mediapipe = watch for just interest.....
         
'''
    