# lamda function
def addA(x,y):
    return x + y

e = addA(12,4)
print(e)

# lambda  - keyword
# x,y - parameter
# return - x + y

addB = lambda x,y:x+y
e2 = addB(12,3)
print(e2)

sqrt = lambda x:x*x
e3 = sqrt(3)
print(e3)

cube = lambda x:x*x*x
print(cube(4))

# int as parameter , int as return 
# float as parameter and float as return 
# string as paramter and string as return 
# dict as paramter and dict as return 
# list as paramter and list as return 
# tuple as paramter and tuple as return 
# set as paramter and set as return 
# boolean as paramter and boolean as return 


# function a parameter and function as return 

addA = lambda x,y:x+y
print(addA)
print(addA(2,1))

c = 10
print(c)


# function as a parameter

addA = lambda x,y:x+y
def additionA(fn,x,y):
    # fn = lambda x,y:x+y
    # x = 12
    # y = 3
    e4 = fn(x,y)
    return e4

e5 = additionA(addA,12,3)
print(e5)



subA = lambda x,y:x-y

# fn = lambda x,y:x+y
# x = 12
# y = 3

def subtraction(fn,x,y):
    e7 = fn(x,y)
    return e7
e8 = subtraction(subA,12,3)
print(e8)


# function as a return type 


def multiplication():
    return lambda x,y:x*y

q5 = multiplication()
print(q5)

# q5 = lambda x,y:x*y
e9 = q5(12,3)
print(e9)