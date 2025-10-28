# a = 10
# print(a)
# b = 12.4
# print(b)
# c = True
# print(c)
# d = "chinmay"
# print(d)
# e = [11,22,33]
# print(e)
# f = 12,
# print(f)
# g = {
#     "firrstName":"chinmay"
# }

# loop , hasValue , methods , CRUD

# set 
setA = {11,22,33}
print(setA)

setB = {22,33,44,22}
print(setB)
# set does not store duplicate values

# program 2
# does set stores the value by index ? - No

setC = {11,22,33}
#print(setC[0])
#setC[0] = 111 #- No immutable , tuple ,set , string


setD = {133,44,55,66}
print(44 in setD)
print(444 in setD)


# program 3
setF = {11,22,33,44}
for item in setF:
    print(item)

# range() , while
# program 4 
setJ = {11,22,33,22,44,33}
print(len(setJ))

# program 5
setG = {11,22,33,44}
print(min(setG))
print(max(setG))
print(type(setG))

# methods 
# add()
setA = {11,22,33,44}
setA.add(555)
print(setA)


# methods 
setA = {44,55,66}
setA.clear()
print(setA)

#del setA

# pop()
setB = {44,55,66,33}
setB.pop()
print(setB)

# remove()
setB.remove(66)
print(setB)

# setC = {33,44,55,66}
# setC.update([77,88,55])
# setC.update((13,4,55,66))
# setC.update("string")
# setC.update({64,33,55,66})
# print(setC)

setG = {11,23,44}
setN = setG.copy()
# setN = setG
# setG.remove(23)
# print(setG)
# print(setN)
setN.remove(23)
print(setN)
print(setG)







