oo# -*- coding: utf-8 -*-
"""
@author: Keshav
"""

# =============================================================================
# multiple inheritance
# =============================================================================

class grandfather:
    def meth1(self):
        print("meth1")
    def meth2(self):
        print("meth2")
        
class father(grandfather, son): 
    def meth3(self):
        print("meth3")
    def meth4(self):
        print("meth4")

class son:
    def meth5(self):
        print("meth5")
    def meth6(self):
        print("meth6")
        
sec = father()

sec.meth1()
