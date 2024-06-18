#Concept of Multiple Inheritance
#Concept of MRO----> Method Resolution Order 
class Father(object): #First Base Class
    def __init__(self,fi):
        #super().__init__()
        self.fincome=fi
        print("Father Income:",self.fincome)
    def show(self):
        print("Father Total Income is:",self.fincome+20000)
class Mother(object): #Second Base Class
    def __init__(self,mi):
        #super().__init__()
        self.mincome=mi
        print("Mother Income:",self.mincome)
    def disp(self):
        print("Total Mother Income is:",self.mincome+20000)
class Son(Father,Mother): #Derived Class From Two Base Classes
    def __init__(self,fi,mi,si):
        #super().__init__()
        Father.__init__(self,fi) #Call the Constructor of Father Class
        Mother.__init__(self,mi) #Call the Constructor of Mother Class
        self.sincome=si
        print("Father Income is:",self.fincome)
        print("Mother Income is:",self.mincome)
        print("Son Income is:",self.sincome)
    def view(self):
        print("Total Son Income is:",self.fincome+self.mincome+self.sincome)

a=Son(100000,70000,50000)   #Object of Derived Class
print()
a.disp() #Run Instance Method of Daughter Class by Son Class Object
print()
a.show()  #Run Instance Method of Father Class by Son Class Object
print()
a.view()  #Run Instance Method of Son Class by Son Class Object