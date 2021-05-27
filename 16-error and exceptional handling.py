# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 07:37:57 2021

@author: Keshav
"""

#how to bypass errors

try:
#write whole program
    
except:
        
#it ignores the error and runs the program
#if error occors this will excute
finally:

#it run even if their is error...

# =============================================================================
# error example
# =============================================================================

try:
    sum=10+'20'
    
except:
    print("You have write different data types in addition...")
    
finally:
    sum=10+20
    print(sum)