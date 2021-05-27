# -*- coding: utf-8 -*-


list1=[1, 2, 3, 4, 5, 6, 984466, 23452684349]

list2=["Infinite", "StrongestAvenger21", 7, 3.14]

# =============================================================================
# Length
# =============================================================================

print(len(list2))

# =============================================================================
# Concatenation
# =============================================================================

list3 = list1 + list2
print(list3)

list4=list2 + list1
print(list4)

# =============================================================================
# Mutable and Unmutable
# Mutable means = Changable 
# =============================================================================

list1[2]=33

list1[5]="Six"

list1[0]=55

#this is called mutable

# =============================================================================
# Indexing and Slicing
# =============================================================================

print(list1[1])

newlist= [1, 2, 3, 4, 5, "ram", "sam", "ravi", 3.14]

#list[start:stop:step] = index Value

print(newlist[0:5])

#this will jump each 1 digit and show 2nd digit in output

newlist[0:5:2]
newlist[0:7:3]

newlist[::]

#Expolre this as much as you can, practice a lot, this is an Important thing.

# =============================================================================
# List Functions
# =============================================================================

#to add value in list
newlist.append("Keshav")

newlist.append(99999)

#to insert Seven on 7th index value of list
newlist.insert(7, "Seven")

#to delete 6th index value
newlist.pop(6)

#to remove something by it's name
newlist.remove('Keshav')

#to Count how many times a Value is in a list by it's name
newlist.count("Keshav")
newlist.count(3)

#New List
num=[45,65,968,3,684,11,30,1,9,44]

#sortlist
num.sort()

#reverse sort list
num.reverse()

#clear whole list
num.clear()

# =============================================================================
# :)
# =============================================================================
