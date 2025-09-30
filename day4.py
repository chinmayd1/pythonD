
# append
names = ["sarika","ram","sham"]
names.append('rahul')
print(names)

# program 2
# pop()
fruits = ["apple","mango","banana","grapes"]
e2 = fruits.pop()
print(e2)
print(fruits)


# program 3
fruits = ["apple","mango","banana","grapes"]
fruitsB = ["chikoo","oranges"]
e = fruits.extend(fruitsB)
print(e)
print(fruitsB)
print(fruits)

# program 4
fruits = ["apple","mango","banana","grapes"]
fruits.remove("banana")
print(fruits)

# program 5
cities = ["pune","mumbai","bangalore","kolkata","pune"]
e3 = cities.count("pune")
print(e3)

# clear()
country = ["india","pakistan","srilanka","bangladesh"]
country.clear()
print(country)


country = ["india","pakistan","srilanka","bangladesh"]
country.reverse()
print(country)

country.sort()
print(country)


country.sort()
country.reverse()
print(country)


# program 6
#            0         1          2           3
country = ["india","pakistan","srilanka","bangladesh"]
country.insert(2,"china")
print(country)