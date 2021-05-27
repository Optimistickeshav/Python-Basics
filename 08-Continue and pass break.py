# -*- coding: utf-8 -*-
"""
@author: Keshav
"""

# =============================================================================
# while loop with continue
# =============================================================================
num=0
while num<=10:
        num=num+1
        
        if num==4:
            print('this is 4')
            continue
        print(num)
            
        
'''        if num<=4: #num less then 4 will not printed
            continue #continue se pehle wali statement chlti hai
        print(num)
'''        
        
# =============================================================================
# pass
# =============================================================================

x=50
o=40
if x>o:
    pass
    #if we left it empty it will show error.
    #to ignore the error from the empty line we use pass like below prgoram
else:
    print("yo")


x=55
o=44
if x>o:
    pass
    #this will ignore the error
else:
    print("yo")
    
# =============================================================================
# pass more examples
# =============================================================================

a = 33
b = 200

if b > a:
  pass

def myfunction():
  pass

for x in [0, 1, 2]:
    pass
  

#pass is used just to store value in backend without showing any output...