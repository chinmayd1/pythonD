
# Abstraction
# abstraction in python 
# instance method , static method , class method , abstractmethod
# abstract method will not have body 
# to abstract method ---> you have to inherit ABC class
# we cannot create object of abstract class 

from abc import ABC, abstractmethod

class WorldBank(ABC):
    @abstractmethod
    def save(self):
        pass
    @abstractmethod
    def loan(self):
        pass
    
class SBI(WorldBank):
    def country(self):
        print("India")

    def save(self):
        print("SBI save")
    
    def loan(self):
        print("SBI loan")

#nyc = WorldBank()

nagpur = SBI() 
nagpur.loan()
nagpur.save()
