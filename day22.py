# program 1
numbers = [1,2,3,4,5]
e = list(map(lambda x:x*x,numbers))
print(e)

# program 2

names = ["ninad dani","sarika pansare","rahul singh","amol rao"]
#print(names[0].split(" ")[0]) # ["ninad","dani"]
# ["ninad","sarika","rahul","amol"]

# for loop 
firstNames = []
for x in names:
    firstNames.append(x.split(" ")[0])#["ninad","dani"]
print(firstNames)

# map
e2 = list(map(lambda fn:fn.split(" ")[0],names))
print(e2)

# list comprehension
# [expression loop condition]
e3 = [fn.split(" ")[0] for fn in names]
print(e3)

# program 2

numbers = [1,2,3,4,2,3,4,5]
e4 = list(filter(lambda x : x % 2 == 0,numbers))
print(e4)

e5 = [x for x in numbers if x % 2 == 0]
print(e5)

# program 3
names = ["John","","Alice","","Bob"]
o = filter(lambda str:len(str) > 0,names)
print(list(o))


students  = [

    {
        "fn":"chinmay",
        "ln":"deshpande",
        "age":23
    },
    {
        "fn":"amol",
        "ln":"rao",
        "age":34

    },
    {
        "fn":"sarika",
        "ln":"pansare",
        "age":35
    }
]

e2 = [dictA for dictA in students if dictA["age"] > 30]
print(e2)




