
# names = ["sarika","poorva","shraddha","raj"]
# numbers = [11,22,33,44,55,66]
# info = ["chinmay","deshpande",34,55]

# print(names)
# print(numbers)
# print(info)

# print(type(names))
# print(type(numbers))
# print(type(info))

# # access the value of list 
# cities = ["pune","mumbai","banglore","kolkata"]
# print(cities[0])
# print(cities[1])
# print(cities[2])

# # update the value 
# cities[0] = "nagpur"
# print(cities)

# # a particular value exist or not 
# print("mumbai" in  cities)
# print(cities)

# # min max len del
# numbers = [11,22,33,44]
# print(min(numbers))
# print(max(numbers))
# print(len(numbers))
# del numbers

# # loops 
# #           0           1          2         3
# country = ["india","pakistan","srilanka","bangladesh"]

# # range()
# for x in range(len(country)):
#     #print(x)
#     print(country[x])

# # forEach()
# for c in country:
#     print(c)

# # while()
# i1 = 0
# while(i1 < len(country)):
#     print(country[i1])
#     i1 = i1 + 1


# list
# append() 
#          0      1      2      3
listA  = ["ram","sham","raj","karan"]
listA.append("srk")
print(listA)

# insert()
#          0      1     2      3
listA  = ["ram","sham","raj","karan"]
listA.insert(1,"rahul")
print(listA)

#          0      1      2     3
listA  = ["ram","sham","raj","karan"]
#          -4     -3    -2      -1
listA.pop()
print(listA)
listA.pop(1)
print(listA)
listA.remove("ram")
print(listA)

# program 3
fruits = ["apple","mango","banana","orange"]
print(fruits)
fruits.extend(["papaya","chikoo",'grapes'])
print(fruits)
#   0         1        2         3         4         5        6
#['apple', 'mango', 'banana', 'orange', 'papaya', 'chikoo', 'grapes']
e = fruits.index("chikoo")
print(e)

# program 4
fruits = ["apple","mango","banana","orange","apple","apple","mango"]
e2 = fruits.count("apple")
print(e2)

# program 5
fruits = ["apple","mango","banana","orange","apple","apple","mango"]
fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)

numbers = []
print(numbers)
numbers.append(11)
numbers.append(22)
numbers.append(33)
numbers.append(44)
print(numbers)
numbers.clear()
print(numbers)