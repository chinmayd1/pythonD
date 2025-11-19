listA = [1,2,3,4,5,6] # object is created for list
firstName = "chinmay" # object is creted for string

class Person:
    # properties and methods 
    firstName = None
    lastName = None 
    # methif
    def displayName(self):
        # self --> amol
        print(self.firstName + self.lastName)

amol  = Person()
print(amol.firstName)
print(amol.lastName)
#amol.displayName()

amol.firstName = "amol"
amol.lastName = "rao"
print(amol.firstName)
print(amol.lastName)
amol.displayName()

chinmay = Person()
print(chinmay.firstName)
print(chinmay.lastName)
#chinmay.displayName()
chinmay.firstName = "chinmay"
chinmay.lastName = "deshpande"
chinmay.language = "marathi"
chinmay.displayName()
print(chinmay.language)

# program 2

class Person2():
    # constructor
    def __init__(self,fn,ln):
        self.firstName  = fn 
        self.lastName = ln 

    def displayName(self):
        print(self.firstName + self.lastName)

amit = Person2("amit","bhure")
amit.displayName()

chinmay = Person2("chinmay","deshpande")
chinmay.displayName()


class Bank:
    # class level varibale 
    country = "India"
    def __init__(self,fn,accNo,bal):
        self.fullName = fn 
        self.accNumber = accNo
        self.balance = bal

    def deposit(self,amount):
        self.balance  = self.balance + amount
        return self.balance 

    def withdrawl(self,amount):
        if amount < self.balance:
            self.balance  = self.balance - amount
        else:
            print("insufficient balance")

amol  = Bank("amol rao",123,100000)
print(amol.fullName)
print(amol.accNumber)
print(amol.country)
print(amol.balance)

amol.withdrawl(200000)
amol.deposit(100000)
print(amol.balance)



