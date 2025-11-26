
# single inheritance

class Student:
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln 
        
    def displayName(self):
        print(self.firstName + self.lastName)
        
        
class Teacher(Student):
    def __init__(self, fn, ln,sl):
        super().__init__(fn, ln)
        self.salary = sl
        
    def displaySalary(self):
        print(self.salary)

amolT  = Teacher("amolT","raoT",12333)
amolT.displayName()
amolT.displaySalary()

# multi-level

# class GrandFather:
#     def __init__(self,fn,ln):
#         self.firstName = fn 
#         self.lastName = ln
        
#     def displayGName(self):
#         print(self.firstName + self.lastName)
        
# class Father(GrandFather):
#     def __init__(self, fn, ln ,ffn):
#         super().__init__(fn, ln)
#         self.fname = ffn
        
#     def displayFName(self):
#         print(self.fname + self.lastName)
        
# class Son(Father):
    
#     def __init__(self, fn, ln, ffn,ssn):
#         super().__init__(fn, ln, ffn)
#         self.sname = ssn
#     def displaySname(self):
#         print(self.sname + self.lastName)
    
# chinmay = Son("manohar","deshpande","shirish","chinmay")   

# print(chinmay.firstName)
# print(chinmay.lastName)
# print(chinmay.fname)
# print(chinmay.sname)

# chinmay.displaySname()
# chinmay.displayFName()
# chinmay.displayGName()


# herarchical  inheritance


class Mother:
    def __init__(self,fn,ln):
        self.fname = fn 
        self.lastName = ln

    def displayMName(self):
        print(self.fname + self.lastName)
        

class Son(Mother):
    def __init__(self, fn, ln,ssn):
        super().__init__(fn, ln)
        self.sname = ssn
    
    def displaySName(self):
        print(self.sname + self.lastName)
        

class Daughter(Mother):
    
    def __init__(self, fn, ln,ddn):
        super().__init__(fn, ln)
        self.dname = ddn
    
    def displayDName(self):
        print(self.dname + self.lastName)



chinmay = Son("Kanchan","Deshpande","Chinmay")
gauri = Daughter("Kanchan","Deshpande","Gauri")

print(chinmay.fname)
print(chinmay.lastName)
print(chinmay.sname)
chinmay.displayMName()
chinmay.displaySName()


print(gauri.fname)
print(gauri.lastName)
print(gauri.dname)
gauri.displayMName()
gauri.displayDName()



# multiple inheritance

class Mother:
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln
        
    def displayName(self):
        print("Mother method called")
        print(self.firstName + self.lastName)
        
        
class Father:
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln
        
    def displayName(self):
        print("Father method called")
        print(self.firstName + self.lastName)
        
class Son(Father,Mother):
    def __init__(self, fn, ln,ssn):
        super().__init__(fn, ln)
        self.sname = ssn
    def displaySname(self):
        print(self.sname + self.lastName)
        

chinmay = Son("Kanchan","Deshpande","Chinmay")
chinmay.displayName()