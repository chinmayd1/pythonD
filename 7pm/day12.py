#          fn         ln       rn age
info = ["chinmay","deshpande",23,45]
# descriptive data type 
dictA = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23,
    "rollNo":45
}
print(dictA)
print(type(dictA))


# program 2
vehicle = {
    "color":"red",
    "type":"sedane"
}
print(vehicle)


# does dict stores the value by index ? - No
print(type(vehicle))
#print(vehicle[0])
vehicle = {
    "color":"red",
    "type":"sedane"
}
print(vehicle)
print(vehicle['color'])
# udating the property of dictionary
vehicle['color'] = "blue"
print(vehicle)
# add the property
vehicle['regNo'] = 123
print(vehicle)


# program 3

animal = {
#     key:value
    "color":"red",
    "leg":4
}
print(animal)

# retrive
print(animal['color'])
# update
animal['color'] = "blue"
print(animal)
# add
animal['age'] = 12
print(animal)

# del
#del animal
animal = {
#     key:value
    "color":"red",
    "leg":4
}
print("Color" in animal)

# len()
print(len(animal))