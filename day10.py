

# slicing
#string[start:end(not inclusive):step(1)]

# 0    1    2    3    4    5    6    7    8      9
# c    h    a    n    d    r    a    p    u      r
#-10  -9   -8   -7   -6   -5   -4   -3   -2     -1

city = "chandrapur"
print(city[1::])
print(city[2:6:])
print(city[-8:7:])
print(city[-8:-1:])
print(city[1:-1:])
print(city[-1:-4])
print(city[::2])
print(city[::3])
print(city[::-1])

#list[start:end:step]
city = ["pune","mumbai","nagpur","chennai","kolkata"]