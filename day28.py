# instance method
# class method method
# static methods -  no interaction with object , writing function inside the class
import random
# program 1
# @  , minskole.in

class StringUtils:
    @staticmethod
    def is_upper(str):
        return str.upper()
    
    # validator
    @staticmethod
    def valid_email(str):
        return "@" in str and  "minskole.in" in str
    
    # id generator
    @staticmethod
    def generator():
        return random.randint(1000,9999)




print(StringUtils.is_upper('amol'))
print(StringUtils.valid_email("chinmay@minskole.in"))
print(StringUtils.valid_email("chinmayminksole.in"))
print(StringUtils.generator())

# program 2

class Employee:
    # class level
    country = "India"
    
    def __init__(self,name,employeeid,salary):
        # instance variables
        self.firstName = name
        self.employeeid = employeeid
        self.salary = salary
        
    def displayName(self):
        return self.name
        
    @classmethod
    def changeCountry(cls,uc):
        cls.country = uc
        
    @staticmethod
    def calculateBonus(sal):
        return sal * 0.10
    
    # instance method
    def displayFinalSalary(self):
        return Employee.calculateBonus(self.salary)+self.salary


e1 = Employee("chinmaydeshpande",1,10000)
e2 = Employee("sarikapansare",1,30000)
e3 = Employee("amolrao",1,40000)


print(e1.displayFinalSalary())
print(e2.displayFinalSalary())
print(e3.displayFinalSalary())

print(Employee.calculateBonus(13000))
print(Employee.changeCountry("india"))