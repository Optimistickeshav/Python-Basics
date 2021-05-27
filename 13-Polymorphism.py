# -*- coding: utf-8 -*-
"""
@author: Keshav
"""
def add(a, b):
    print(a+b)
    
def add1(a, b, c):
    print(a+b+c)
    
add(5,6,5)

#-------------------


class rectangle:
    def __init__(self, length, breadth):
        self.len=length
        self.breadth=breadth
        print('These values are now in __init__')
        
    def area(self):
        print(self.len*self.breadth)
        
    def perimeter(self):
        print(2*(self.len + self.breadth))
        
class square:
    def __init__(self, side):
        self.side=side
        print(side, 'This is in __init__')
        
    def area(self):
        print(self.side**2)
        
    def perimeter(self):
        print(self.side*4)
        
rec = rectangle(10, 15)

rectangle(2, 5) #???

sq = square(10)

rec.area()
rec.perimeter()


for shape in (rec, sq):
    shape.area()
    shape.perimeter()

#same name of method with different properties... is called polymorphism