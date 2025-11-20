
info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":36
}
print(info)

# dictionary does not store value by index
#print(info[0])
# how to retrive the value from dictionary

info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":36
}
print(info)
print(info['firstName'])

# updating the dictionary update
info['firstName'] = "ram"
print(info)

# add the new value
info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":36
}
info['age'] = 34
info['city'] = "pune"
print(info)

# len()
e2 = len(info)
print(e2)

#deleting the dictionary
#del info
# particular property exist in dictionary
info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":36
}
print("age" in info)


# methods in dictionary

info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":36
}
