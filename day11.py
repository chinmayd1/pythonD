a = 10 
print(a)
print(type(a))
# 10 ,-10 , 0
a = 1000

b = 10.5
print(b)
print(type(b))
# 10.4 , -12.4 , 0.34
b = 1111.5

c = True
print(c)
print(type(c))
c = False


# collection
d = "chinmay"
print(d)
print(type(d))
d = "shrish"
#d[0] = "a"

# list
#          0  1  2  3  4
numbers = [11,22,33,44,55]
numbers[0] = 333
print(numbers)

dictA = {
    "firstName":"chinmay",
    "lastName":"deshpande"
}  
print(dictA)
dictA['firstName'] = "tanmay"

# tuple 

# define 

a = 11,
print(a)
print(type(a))

b = 11,22
print(type(b))

c = (11,22)
print(c)

# does tuple stores the value by index ??? - yes
names = ("chinmay","shirish","ram")
print(names[0])

# can we update 1 single value ? No , fixed length 
# tuples are fixed length 
# names[0] = "samay"
# names[3] = "sham"

# particular value exist 

names = ("chinmay","shirish","ram")
# in
print("Chinmay" in names)

# number of elements 
print(len(names))
print(max([11,22,33]))
print(max((1,2,3)))
print(min([11,22,33]))
print(min((1,2,3)))

# unpacking 

numbers = (11,22,33)
# a = numbers[0]
# b = numbers[1]
# c = numbers[2]
# print(a)
# print(b)
# print(c)
a , b, c = numbers
print(a)
print(b)
print(c)

#           0  1  2
numbers = (11,22,33)

# for - range()

for x in range(len(numbers)):
    #print(x)
    print(numbers[x])

# while
i1  = 0
while(i1 < len(numbers)):
    #print(i1)
    print(numbers[i1])
    i1 = i1 + 1


# for Each
for a in numbers:
    print(a)


numbersB = (11,22,33,11)
q = numbersB.count(11)
print(q)

v = 11,22,33
r = v.index(11)
print(r)