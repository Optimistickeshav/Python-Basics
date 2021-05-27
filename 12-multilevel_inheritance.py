# -*- coding: utf-8 -*-
"""
@author: Keshav
"""

# =============================================================================
# multilevel inheritance
# =============================================================================

class grandfather(): #meth1 meth2
    def meth1(self):
        print("meth1")
    def meth2(self):
        print("meth2")
        
class father(grandfather): #meth3 meth4 - meth1 meth2
    def meth3(self):
        print("meth3")
    def meth4(self):
        print("meth4")

class son(father): #meth5 meth6 - meth3 meth4 - meth1 meth2
    def meth5(self):
        print("meth5")
    def meth6(self):
        print("meth6")
        
sec=son()
sec.meth6()

rob=father()
rob.meth4()

bob=grandfather()
bob.meth2()

xg = grandfather()
xg.meth2()

xf = father()
xf.meth4()

x = son()
x.meth5()

