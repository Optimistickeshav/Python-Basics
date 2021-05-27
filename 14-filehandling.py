# -*- coding: utf-8 -*-
"""
@author: Keshav
"""
# =============================================================================
# x = creating a file
# w = rewrite a file
# a = appending a file
# r = reading a file
# =============================================================================


f=open("file2.txt", "x")
f.write("new file")
f.close()

f=open("file2.txt", "r")
print(f.read(4))
f.close()

f=open("file2.txt", "a")
f.write("\n this is a new line")
f.close()

f=open("file2.txt", "a")
f.truncate(10) #it will show only 10 chars
f.write("\nnew file 1")
f.close()


f.seek(4)#to take your pointer on a point...
#print(f.read())

f.tell()#to know where the pointer is....

f=open("file2.txt", "r")
f.readline()#to read single line
x=f.readlines()#run line 38 then run this,
#it will convert eaxt line into var of list..