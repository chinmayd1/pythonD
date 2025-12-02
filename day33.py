
# polymorphism

# Class - better way
# Methods - 

# Encapsulation
# Inheritance -  single , multi-level , herarchical 
# multiple
# Polymorphism 

# overloading 

class MathOps:
    # instance
    def add(self,a= 0,b = 0,c=0):
        return a + b + c

a = MathOps()
print(a.add(1))
print(a.add(1,2))
print(a.add(1,3,4))

# overriding

class Animal:
    def sound(self):
        print("Basic generic sound")
        
class Dog(Animal):
    # override
    def sound(self):
        print("Bark")
        
class Cat(Animal):
    # override
    def sound(self):
        print("Meow")

class Rabbit(Animal):
    pass

a = Animal()
b = Dog()
c = Cat()
d = Rabbit()

# a.sound()
# b.sound()
# c.sound()
# d.sound()

# looping through object
for animal in (a,b,c,d):
    animal.sound()
    
#  same class same method different signature - overlading 
#  different class same method same signature - overriding

# program 3
# Duck typing  - polmorphism
class Duck:
    def speak(self):
        print("Quack Quack")


class Human:
    def speak(self):
        print("hello hi")
        
class Cat:
    def speak(self):
        print("Meow")

def call_speak(obj):
    print(obj.speak())

duckA = Duck()
humanB = Human()
catC = Cat()

call_speak(duckA)
call_speak(humanB)
call_speak(catC)

# Method overloading

print(1 + 2)
print("hello " + "hi")


class BookA:
    def __init__(self,pages):
        self.pages = pages
        
class BookB:
    def __init__(self,pages):
        self.pages = pages
        
bookA = BookA(200)
bookB = BookA(100)
 
print(bookA.pages + bookB.pages)
       
#print(bookA + bookB)
# how to add object ---> tommorow
        



