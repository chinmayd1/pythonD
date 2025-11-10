
# expression  loop   condition
birthYear = [1989,1990,1991,1992]
ages =[]
for x in birthYear:
    print(2025 - x)
    ages.append(2025 - x)
print(ages)

# map()
print(list(map(lambda x:2025-x,birthYear)))

#expression  loop   condition
# list comprehension --> list
e2 = [2025 - x for x in birthYear]
print(e2)

numbers = [1,2,3,4,5,6,7,8,9,10]
print([x * 3 for x in numbers])

numbers = [1,2,3,4,5,6,7,8,9,10]
print([x + 10 for x in numbers])

print([x * x for x in numbers])


# program 2
marks = [92,90,89,87,22,33,44,55,66]
above60 = []
for x in marks:
    if x > 60:
        above60.append(x)
print(above60)

# filter 
print(list(filter(lambda x : x > 60,marks)))
#expression  loop   condition
print([x  for x in marks  if x > 60])

transactions = [11,22,33,44,55,-66,77,88,99]
deposit = [x for x in transactions if x > 0]
withdrawl = [x for x in transactions if x < 0]
print(deposit)
print(withdrawl)

# program 3
names = ["chinmay","ram","sham","sarika","satish"]
print([x[0] for x in names])
print([x.upper() for x in names])

# program 4

evenOdd = [44,55,22,33,44,55,66,88]
#[even,odd,even,odd,even,odd,even,even]
w = ["even" for x in evenOdd if x % 2 == 0]
print(w)

# multiple condition -- list comprehension tenary 
#[ternary loop]
w2 = ["even" if x % 2 == 0 else "odd" for x in evenOdd]
print(w2)