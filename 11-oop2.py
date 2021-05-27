class s: #Blueprint
    def meth(other, name, age):#method
        #a new way to assign var. from a class....
        other.naam = name #to use function's value outsite
        other.agee = age
        pass #pass function, is used for not showing error in the case where
        #we didn't put print or return statement...


obj_1=s()
obj_1.meth("ram", 21)

print(obj_1.naam)
print(obj_1.agee)

obj_2=s()
obj_2.meth("jack", 33)

print(obj_2.naam)
print(obj_2.agee)


print ('Write your Name :')
obj_1.name_1=input()
print ('Write your Age :')
obj_1.age=input()

print('Age of',obj_1.name_1,'is', obj_1.age)
