
# incorrect way to write code
class Student:
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln
        
    def displayName(self):
        print(self.firstName + self.lastName)
        

class Teacher:
    salary = 1000
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln
        
    def displayName(self):
        print(self.firstName + self.lastName)
        
    def displaySalary(self):
        print(self.salary)
        

# Parent constructor , child no construtor
class Student:
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln 
        
    def displayName(self):
        print(self.firstName + self.lastName)
        
class Teacher(Student):
    salary = 1000
    
    def displaySalary(self):
        print(self.salary)
        
amolT = Teacher("amolT","raoT")
print(amolT.firstName)
print(amolT.lastName)
print(amolT.salary)
amolT.displayName()
amolT.displaySalary()

# parent constructor and child also having constructor
# single inheritance
class Student:
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln 
        
    def displayName(self):
        print(self.firstName + self.lastName)

class Teacher(Student):
    def __init__(self, fn,ln,sl):
        super().__init__(fn, ln)
        self.salary = sl

    def displaySalary(self):
        print(self.salary)
        

amolT2 = Teacher("amolT2","raoT2",10000)
print(amolT2.firstName)
print(amolT2.lastName)
print(amolT2.salary)

amolT2.displayName()
amolT2.displaySalary()
print(amolT2.firstName)
print(amolT2.lastName)


# multi-level
# herarchical 
# multiple - inhertance 
# MVC