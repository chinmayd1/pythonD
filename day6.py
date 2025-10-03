
info = ["chinmay","deshpande",7709192441,34,55]


# dictionary
info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "mobileNumber":7709192441,
    "age":55,
    "rollNo":34
}

#           0         1       2     3       4         5       6
names = ["sarika","chinmay","ram","sham","satish","chinmay","sarika"]
print(type(names))

# does list stores the value by index
# retrive
print(names[1])

# update
names[1] = "tanmay"
print(names)
# add
names.append('omkar')
names.insert(1,'shraddha')
print(names)
#delete 
names.pop()
names.remove('ram')

# does list allows to store duplicate values ?
print(names)


# how many elements in list 
print(len(names))


# for - range
for x in range(len(names)):
    #print(x)
    print(names[x])

# while 
i1 = 0
while(i1 < len(names)):
    #print(i1)
    print(names[i1])
    i1 = i1 + 1

# for each
numA = [11,22,33,44]
for y in numA:
    print(y)


vehicle = {
    # key:value
    # property:value
    "color":"red",
    "type":"sedane",
    "type":"SUV"
}
print(type(vehicle))
#print(vehicle[0])

# retrive 
print(vehicle['color'])
print(vehicle['type'])

# update
vehicle['color']  = "blue"
print(vehicle)

# add
vehicle['logo'] = "circle"
print(vehicle)

# remove
# vehicle.pop('type')
# print(vehicle)

# allow duplicate keys ? - NO 

# number of key values 
print(len(vehicle))


vehicle = {
    "color":"red",
    "type":"sedane",
    "type":"SUV"
}

for key in vehicle:
    print(key,vehicle[key])