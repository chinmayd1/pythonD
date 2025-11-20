
# class Person:
#     def __init__(self,fn,ln,age):
#         # instance varibales
#         self.firstName = fn 
#         self.lastName = ln
#         self.age = age
#     # instance method - self
#     def displayName(self):
#         print(self.firstName + self.lastName)
        
#     # instance method for update
#     def updateAge(self,inc):
#         self.age =  self.age + inc

# amol = Person("amol","rao",13)
# chinmay = Person("chinmay","deshpande",34)

# print(amol.firstName)
# print(amol.lastName)
# print(amol.age)
# amol.displayName() 
# amol.updateAge(2)
# chinmay.updateAge()




class Student:
    # class varibale
    country = "india"
    def __init__(self,fn,ln,age):
        # instance varibales 
        self.firstName = fn 
        self.lastName = ln 
        self.age = age
    
    
    @classmethod
    def changeCountry(cls,uc):
        cls.country = uc
        

    # instance method 
    def displayName(self):
        print(self.firstName + self.lastName)
    
        # instance method for update
    def updateAge(self,inc):
        self.age =  self.age + inc



amol = Student("amol","rao",13)
chinmay = Student("chinmay","deshpande",34)

print(amol.country) # india
print(amol.firstName)
print(amol.lastName)
print(amol.age)

amol.country = "bharat"
print(amol.country) # bharat

print(chinmay.country) # india
Student.changeCountry("INDIA")
sarika = Student("sarika","pansare",34)
print(sarika.country) # INDIA
print(amol.country) # bharat
print(chinmay.country) # INDIA