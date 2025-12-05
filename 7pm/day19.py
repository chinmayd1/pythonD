#         0           1       2   3
info = ["chinmay","deshpande",12,45]
print(info)
print(type(info))

print(info[1])

info2 = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":45,
    "rollNo":12
}
print(info2)
print(type(info2))


# does dictionary stores the value by index - No
info2 = {
    # key:value
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":45,
    "rollNo":12
}
#print(info2[0])
print(info2['firstName'])
print(info2['lastName'])


# updating the value
info2 = {
    # key:value
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":45,
    "rollNo":12
}
city = ["pune","mumbai","bangalore"]
city[0] = "Pune"
print(city)

info2["age"] = 35
print(info2)

# check whether the value exist ??
info2 = {
    # key:value
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":45,
    "rollNo":12
}
print('Age' in info2)
print('age' in info2)

# loop

info2 = {
    # key:value
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":45,
    "rollNo":12
}

# for Each
for key in info2:
    print(key,info2[key])
# methods ?