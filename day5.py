listA = [11,22,33]
print(listA)
listB  = listA
listB[0] = 111
print(listB)
print(listA)

listA = [11,22,33]
listC = listA.copy() # different memory
listC[0] = 111
print(listA)
print(listC)

# append()
names  = ["sarika","amol","ram","sham","snehal","ram"]
names.append("satish")
print(names)

# clear()
#names.clear()
#print(names)

# sort()
cities = ["pune","mumbai","bangalore","kolkata"]
cities.sort()
print(cities)

# reverse()
cities = ["pune","mumbai","bangalore","kolkata"]
cities.reverse()
print(cities)

# extend()
numA = [11,22,33]
numB = [44,55,66]
#numB.extend(numA)
numA.extend(numB) # [11,22,33,44,55,66]
print(numB)

# remove() pop()
country = ["india","srilanka","china","cuba"]
country.pop()
country.remove("india")
print(country)


country = ["india","srilanka","china","cuba"]
country.insert(2,"pakistan")
print(country)

# index
country = ["india","srilanka","china","cuba","india","US","Uk",'Mexico',"india"]
country.index("india")
e2 = country.index("india",2)
print(e2)
e3 = country.index("india",1,5)
print(e3)

country = ["india","srilanka","china","cuba","india","US","Uk",'Mexico',"india"]
#del country
print(len(country))

numA = [11,22,33]
print(min(numA)) # 11
print(max(numA)) # 33