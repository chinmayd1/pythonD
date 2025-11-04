# a = 10
# b = 5

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)

# c = 6
# d = 3

# print(c+d)
# print(c-d)
# print(c*d)
# print(c/d)
# print(c%d)

# def Calculator(x,y):
#     print(x+y)
#     print(x-y)
#     print(x*y)
#     print(x/y)
#     print(x%y)
# Calculator(12,3)
# Calculator(11,2)


# int as parameter and int as return int 
def CalA(x,y):
    return x + y
e = CalA(12,3)
print(e)


# float as a parameter and function as return type 
def CalB(x,y):
    return x + y
f = CalB(12.5,12.10)
print(f)

# boolean as a parameter and boolean as return type
def canDrive(age, haveVehcile):
    if age >= 18 and haveVehcile:
        return True
    else:
        return False
f = canDrive(19,True)
print(f)

# string a parameter and string as return type 
def Greet(word):
    return "hello "+ word
g = Greet("chinmay")
print(g)

# list as a parameter and list as a return type 
city = ["pune","mumbai","bnaglore","kolkata"]
def addCity(lst):
    lst.append("nagpur")
    return lst
city2 = addCity(city)
print(city2)

# dict as a parameter and dict as a return type 

info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
}
def addCity(info):
    info['city'] = 'pune'
    return info
e = addCity(info)
print(e)

# tuple as parameter and tuple as return type

numbers = (11,22,33)

def addToTuple(tupA):
    tupA = list(tupA)
    tupA.append(44)
    tupA = tuple(tupA)
    return tupA
f = addToTuple(numbers)
print(f)

# set as a parameter and set as a return type 
setA = {11,22,33}
def addToSet(setC):
    setC.add(55)
    return setC
k = addToSet(setA)
print(k)