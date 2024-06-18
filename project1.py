#Concept of Constructor in Single Inheritance
#When Constructor is Present only in Base Clas
class Father(object): #Base  Class
    def __init__(self,age): #Constructor of Super Class
        self.ageF=age
        self.nameF="M.Idrees"
        print("Father Name:",self.nameF)
        print("Father age:",self.ageF)
class Son(Father): #Derived Class
    ageS=23
    nameS="Ali"
    @classmethod
    def disp(cls):
        print("Son Name:",cls.nameS)
        print("Son age:",cls.ageS)
    def show(self):
        print("Father Name is:",self.nameF)
        print("Father age is:",self.ageF)

a=Father(66) #Create Object Father Class and Run Constructor of Father Class ByDefault
print()
b=Son(66) #Create Object Son Class and Run Constructor of Father Class ByDefault
b.disp() #Run Class Method by Son Class Object
print()
b.show() #Run Instance Method by Son Class Object
print()
Son.disp() #Run Class Method by Son Class name
print("Father Class Instance Variable by Son Class Object::Father Name:",b.nameF)
print("Father Class Instance Variable by Son Class Object::Father age:",b.ageF)
print("Son Class class Variable by Son Class Object::Son age:",b.ageS)
print("Son Class class Variable by Son Class Object::Son Name:",b.nameS)




