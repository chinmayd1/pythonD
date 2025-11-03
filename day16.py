
# funtion as a parameter and function as a return type

# sum of two number using lambda function 

addA = lambda x,y:x+y
q1 = addA(12,3)
print(q1)

# square of number using lambda function 
q2 = lambda x : x * x
print(q2)
q2 = q2(5)
print(q2)

# function as a parameter to another function

mulA = lambda x,y:x*y

# fn = lambda x,y:x*y
# x = 4
# y = 2

def multiplicationA(fn,x,y):
    q3 = fn(x,y)
    return q3

q4 = multiplicationA(mulA,4,2)
print(q4)


# function as a return type
def divideD():
    return lambda x,y:x/y

e = divideD()
#e = lambda x,y:x/y
q5 = e(4,2)
print(q5)


# default parameters
def addN(x=9,y=3):
    print(x+y)
addN()
addN(12,4)

# position arguments
def SubN(x,y):
    print(x-y)
SubN(y =10, x=20)

# y = 10
# x = 20

# *args
#d = [11,22,33,44]
#e = (1,3,4,55,6)
def addAll(*args):
    print(args)
    total = 0
    for x in args:
        total =  total + x
    return total

e3 = addAll(12,3,4,5,6,7,8,5,6,7,4,5,6,7,3,5,6)
print(e3)

# **kwargs