#Concept of Constructor in Single Inheritance
#When Constructor is present in Both Classes Base and Derived Class
class Father(object): #Base  Class
    def __init__(self,age): #Constructor of Base Class
        self.ageF=age
        self.nameF="M.Idrees"
        print("Father Name:",self.nameF)
        print("Father age:",self.ageF)
class Son(Father): #Derived Class
    def __init__(self,age,name): #Constructor of Derived Class
        self.ages=age
        self.names=name
        print("Son Name:",self.names)
        print("Son age:",self.ages)
    def show(self):
        print("Father Name is:",self.nameF)    


a=Father(70) #Create Object Father Class and Run Constructor of Father Class ByDefault
print()
b=Son(23,"Abdul Khaliq") #Create Object Son Class and Run Constructor of Father Class ByDefault

    
