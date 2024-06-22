#Concept of Multi-level Inheritance
class GrandFather(object):
    def __init__(self,pg):
        self.nameG="M.Ishaq"
        self.propertyG=pg
        print("GrandFather Balance",self.propertyG)
    def show(self):
        print("GrandFather Name:",self.nameG)
        print("GrandFather Property:",self.propertyG,"Rs.")
class Father(GrandFather):
    def __init__(self,pf,pg):
        super().__init__(pg)
        self.nameF="M.Idrees"
        self.propertyF=pf+self.propertyG
        print("Father Balance:",self.propertyF)
    def disp(self):
        print("GrandFather Name:",self.nameG)
        print("GrandFather Property:",self.propertyG,"Rs.")
        print("Father Name:",self.nameF)
        print("Father Property:",self.propertyF,"Rs.")
class Son(Father):
    def __init__(self,ps,pf,pg):
        super().__init__(pf,pg)
        self.nameS="Abdul Khaliq"
        self.propertyS=ps+self.propertyF
        print("Son Balance:",self.propertyS)
    def view(self):
        print("GrandFather Name:",self.nameG)
        print("GrandFather Property:",self.propertyG,"Rs.")
        print("Father Name:",self.nameF)
        print("Father Property:",self.propertyF,"Rs.")
        print("Son Name:",self.nameS)
        print("Son property:",self.propertyS,"Rs.")

c=Son(25000,50000,75000) #Create Object of Son Class that has the Access to all members of Father and GrandFather Classes 
print()
c.view() #Run Son class Instance method using Son Class Constructor
print()
c.disp()  #Run Father class Instance method using Son Class Constructor
print()
c.show()  #Run GrandFather class Instance method using Son Class Constructor


    
