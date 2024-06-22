#Concept of Hierarchical Inheritance
class Father(object): #Base Class
    def __init__(self,fs):
        self.fathershopes=fs
        self.fathercars=5
        self.fatherhomes=3
        print("Total Numbers of Father:",self.fathershopes+self.fathercars+self.fatherhomes)
        print()
    def view(self):
        print("Father Distribute his Property among his son and daughter")    
class Son(Father): #Derived Class 
    def __init__(self,fs,ss):
        super().__init__(fs)
        self.sonshopes=ss+self.fathershopes
        self.soncars=1+self.fathercars
        self.sonhomes=2+self.fatherhomes
        print("Total Numbers of Father:",self.fathershopes+self.fathercars+self.fatherhomes)
        print("Total Numbers of Son:",self.sonshopes+self.soncars+self.sonhomes)
    def disp(self):
        print("Father shops:",self.fathershopes)
        print("Father cars:",self.fathercars)
        print("Father homes:",self.fatherhomes)
        print()
        print("Son shops:",self.sonshopes)
        print("Son cars:",self.soncars)
        print("Son homes:",self.sonhomes)
class Daughter(Father): #Derived Class
    def __init__(self,fs,ds):
        super().__init__(fs)
        self.dshopes=ds
        self.dcars=1
        self.dhomes=1
        print("Total Numbers of Father:",self.fathershopes+self.fathercars+self.fatherhomes)
        print("Total Numbers of Daughter:",self.dshopes+self.dcars+self.dhomes)
    def show(self):
        print("Father shops:",self.fathershopes)
        print("Father cars:",self.fathercars)
        print("Father homes:",self.fatherhomes)
        print()
        print("Dauhter shops:",self.fathershopes+self.dshopes)
        print("Daughter cars:",self.fathercars+self.dcars)
        print("Daughter homes:",self.fatherhomes+self.dhomes)


a=Son(3,2) #Object of First Derived Class that is Son class 
print()
a.view() #Run Base Class Instance Method by Son Class Object
print()
a.disp() #Run Derived Class Instance Method by Son Class Object
print()
b=Daughter(3,1) #Object of Second Derived Class that is Daughter Class
print()
b.view()  #Run Base Class Instance Method by Daughter Class Object
print()
b.show()  #Run Derived Class Instance Method by Daughter Class Object
