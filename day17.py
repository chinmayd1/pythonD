
#default parameter
def addA(x=10,y=7):
    print(x+y)

addA(12,3)
addA()

#postional arguments 
# y = 10
# x = 20

def subB(x,y):
    print(x-y)
subB(y=10,x = 20)


#*args
def addAll(*args):
    print(args)
    total  = 0
    for x in args:
        total = total + x
    return total
e = addAll(12,3,4,5,6,7,8,4,5,6)
print(e)


# **kwargs
def addCity(**kwargs):
    print(kwargs)
    kwargs['city'] ="pune"
    kwargs.update({"language":"marathi"})
    return kwargs

e2 = addCity(fn="chinmay",ln="deshpande")
print(e2)

# operation with every element of list

birthYear = [2000,2001,2002,2003]
# [25,24,23,22]
ages =[] # [25,24,23,22]
for year in birthYear:
   # print(year)
   #print(2025 - year)
   ages.append(2025 - year)
print(ages)



# filtering operation 
marks = [34,37,39,42,33,45,32]
#[37,39,42,45]
above35 = []
for x in marks:
    #print(x)
    if x > 35:
        above35.append(x)
print(above35)



# sum of all elements of list
nums  = [11,22,33]
total = 0
for x in nums:
    #print(x)
    total = total + x
    #         0   +  11 --> 11
    #         11  +  22 --> 33
    #         33  +  33 --> 66
print(total)


    
