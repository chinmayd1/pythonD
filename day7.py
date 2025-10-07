info = {
    # property:value
    # key:value
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":24,
    "rollNo":35
}
print(info)
print(type(info))

# does dictionary stores the value by index ?
#print(info[0])
# retrive
q1  = info['firstName']
print(q1)
# update
info['firstName'] = "tanmay"
print(info)
# add
info['language'] = "marathi"
print(info)

# remove
info.pop('age')
print(info)


# program 2

vehicle = {
    "color":"red",
    "type":"sedane",
    "passing":"pune",
    "color":"blue"

}
print("color" in vehicle)
print("Color" in vehicle)
print(vehicle)


vehicle = {
    "color":"red",
    "type":"sedane",
    "passing":"pune",
    "color":"blue"

}

for key in vehicle:
    print(key) #key
    print(vehicle[key]) # values


# program 3

student = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":12,
    "rollNo":36
}   

# print(student['firstName'])
# print(student.get('age'))

print("hello")
#print(student['language']) # execution halt
print(student.get('language'))
print('bye')

# program 4

student = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":12,
    "rollNo":36
}   

student.clear()
print(student)

# program 5

student = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":12,
    "rollNo":36
}

student.update({"language":"marathi","city":"pune"})
print(student)
print(len(student))

# program 6

student = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":12,
    "rollNo":36
}
# student.pop('firstName') # passing property
# print(student)

student.popitem()
print(student)


# program 7 

student = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":12,
    "rollNo":36
}

for x in student.keys():
    print(x)

for x in student.values():
    print(x)

for x in student.items():
    print(x)


# program 8


student = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":12,
    "rollNo":36
}

# if property exist will return its value , else will set the default value
print(student.setdefault('age',22))
# if property does not exist ?
print(student.setdefault('city',"pune"))
print(student)


# program 8
print(dict.fromkeys(["key1","key2","key3","key4"]))

student = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":12,
    "rollNo":36
}

studentA = student
studentA['firstName'] = "rahul"

print(student)
print(studentA)



# e = [11,22,33]
# e1 = e
# e1[0] = 111
# print(e)
# print(e1)