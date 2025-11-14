
x = 10
print(x)

# how to define list in python 

numbers = [11,22,33,44,55,66]
cities = ["pune","mumbai","banglore","kolkata"]
info = ["chinmay","deshpande",34,True]

print(numbers)
print(cities)
print(info)

print(type(numbers))
print(type(cities))
print(type(cities))

# program 2
#   list stores the value by index
#            0       1       2       3
country = ["india","china","cuba","srilanka"]
print(country[0])
print(country[1])
print(country[2])

# program 3
# updating the value
fruits = ["apple","mango","banana","grapes"]
fruits[0] = "Apple"
print(fruits)

# program 4
# particular element available in list 
#             0           1        2
vegetable = ["tomato","potato","brinjal"]
print("potato" in vegetable)
print("Potato" in vegetable)

# program 5
#           0  1  2  3
numbersB = [11,22,33,44]
print(max(numbersB))
print(min(numbersB))
print(len(numbersB))

# looping through list 
 
#           0       1          2          3      4
cities = ["pune","mumbai","bangalore","chennai","gao"]

# for range()
# startIndex - 0
# endIndex - 4 (included)
# stepSize - 0

for x in range(5):
    #print(x)
    print(cities[x])


# for each 

# while 
#           0       1          2          3      4
cities = ["pune","mumbai","bangalore","chennai","goa"]
i1 = 0
while(i1 < len(cities)):
    #print(i1)
    print(cities[i1])
    i1 = i1 + 1