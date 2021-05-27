"""
@author: Keshav
"""

#Dictionary Ex. 

game = {"Name":'Kevin', "age":20, "Height":6.5}




dict2={5:5000, 7:7000}

#each value of dictionary have 2 parts - 1 is key and another is value...

dict1 = { "Car Name": 'R8', "Car Compnary": 'Audi', "Car Engine": "V8" } 

dict2 = {'x': 55, 'y': 100, 'z': 1000}

dict3 = {5:50, 7:700, 8:8000}

'''
game[1] ???
'''



#Assigning Value to a new Var from Dictionary

#we have added the value of dict3 ki key 5 ki value....

h = dict2['y']

t = dict2['z']


dict3 = {5:50, 7:700, 8:8000}

seven = dict3[7]

car = dict1['Car Compnary']

Name = game['Name']

fivek=dict2[5]


d2 = game['age']
 #----------------------------------------------------
 
#Know all the Keys of Dictionary

dict3
dict3.keys()

dict2.keys()

#Know all the Values of Dictionary
dict3.values()

dict2.values()

len(dict3)

#to check the length
len(game)

#Change Value #mutable(changable) or immutable

dict3[7] = "Seven"

#Nested Dict.
myDict = {1:"one", 2:55, 3:"three", 4:"four" }

myDict.pop(2)

myDict[2] = myDict.popitem(2)

myDict[2]

#*****

print myDict

Output
{1: 'one', 2: {3: 'three', 5: 'four'}}


list1 = [44, 44, 545, 34] #we can change any value, more functions

tuple1 = (44, 546, 45, 34) #we can't change any value, all var are fixed

game["age"]=15


dict2['y']=200

#-----------------------------------------Mark......o

#Create new Key
game["State"]="Delhi"
game["State"]="Mumbai"


#list, int and string in dictionary

dict_var1={
       "apple" : 100,
       "Chocolate" : [30,70,120,280],#this is a list in dictionary
       "Chips" : {"Potatochip":30, "Chilli":50}
       }

#assigning value of dictinary's key's value to a new var.

unamedvar1 = dict_var1['Chocolate'][0]*dict_var1['Chips']['Chilli']

unamedvar2 = dict_var1['Chocolate'][1]

unamedvar3 = price["Chips"]["Chilli"]

g1=price["Chocolate"][2]

#Assign index value to a new var from dictionary's value.
new=price["Chocolate"][2]

#delete item by it's name
price.pop("apple")

#it will remove the last item
price.popitem()

price.clear()

game.items()

# =============================================================================
# :) Complete
# =============================================================================
# Set & Tuple - Next Chapter....