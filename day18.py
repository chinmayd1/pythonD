# program 1
birthYear = [1989,1990,1991,1992]
#[36,35,34,33]
ages = []
for x in birthYear:
    #print(2025 - x)
    ages.append(2025 - x)
print(ages)


# map()

e = map(lambda x : 2025 -x ,birthYear)
e2 = list(e)
print(e2)

# program 2
numbers  = [1,2,3,4,5,6,7,8,9,10]
# [2,4,6,8,10,12,14,16,18,20]
#map
# list(mapfn)
e3 = list(map(lambda x : x*2 ,numbers))
print(e3)

# program 2
marks = [94,90,89,45,66,92]
above90 = []
for x in marks:
    if x >= 90:
        above90.append(x)
print(above90)

f = filter(lambda x:x>=90,marks)
above902 = list(f)
print(above902)

# program 3
transactions = [90,45,66,-199,45,66,77,-67,78,12,-34]
deposit = list(filter(lambda x:x>0,transactions))
print(deposit)
withdrawl =list(filter(lambda x:x<0,transactions))
print(withdrawl)

# program 4
arr = [11,22,33]
total = 0
for x in arr:
    total = total + x
    #         0 + 11
    #         11 + 22
    #         33 + 33

print(total)

from functools import reduce
e2 = reduce(lambda total,x:total+x,arr,5)
print(e2)






