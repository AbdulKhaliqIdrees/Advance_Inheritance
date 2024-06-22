#Concept of Constructor in Single Inheritance
#Concept of super() method
#Learn How we Run Constructor of Both Base and Derived Class
class Father(object): #Base  Class
    def __init__(self,agef,namef): #Constructor of Base Class
        self.ageF=agef
        self.nameF=namef
        print("Father Name:",self.nameF)
        print("Father age:",self.ageF)
class Son(Father): #Derived Class
    def __init__(self,ages,names,agef,namef): #Constructor of Derived Class
        super().__init__(agef,namef)
        self.ages=ages
        self.names=names
        print("Son Name:",self.names)
        print("Son age:",self.ages)
        print()
        print("Father Name is:",self.nameF)
        print("Father age is:",self.ageF)
        #super().__init__(namef,agef)

a=Father(79,"M.Idrees") #Create Object Father Class and Run Constructor of Father Class ByDefault
print()
b=Son(23,"Abdul Khaliq",79,"M.Idrees") #Create Object Son Class and Run Constructor of Father Class ByDefault
