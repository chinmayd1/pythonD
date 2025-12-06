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

# dict methods 
student = {  
    "firstName":"amol",
    "lastName":"rao",
    "age":12,
    "rollNo":45
    
}
print(student)
print(type(student))

# retrive value
e = student.get('firstName')
print(e)

# program 2
student = {  
    "firstName":"amol",
    "lastName":"rao",
    "age":12,
    "rollNo":45
    
}
student.update({"city":"pune","language":"hindi"})
print(student)

# program 3
student = {  
    "firstName":"amol",
    "lastName":"rao",
    "age":12,
    "rollNo":45
    
}
for key in student.keys():
    print(key)

for val in student.values():
    print(val)
    
for (k,v) in student.items():
    print(k,v)

# program 4

student = {  
    "firstName":"amol",
    "lastName":"rao",
    "age":12,
    "rollNo":45
    
}
e5 = student.clear()
print(e5)
print(student)


student = {  
    "firstName":"amol",
    "lastName":"rao",
    "age":12,
    "rollNo":45
    
}
student.pop('age')
print(student)
student.popitem()
print(student)



student = {  
    "firstName":"amol",
    "lastName":"rao",
    "age":12,
    "rollNo":45
    
}

info2 = dict.fromkeys(['fn','ln','city','language'])
print(info2)



student = {  
    "firstName":"amol",
    "lastName":"rao",
    "age":12,
    "rollNo":45
    
}

student2 = student.copy()
student2.update({"city":"pune"})
print(student)
print(student2)

student = {  
    "firstName":"amol",
    "lastName":"rao",
    "age":12,
    "rollNo":45
    
}
e2 = student.setdefault('age',44)
print(e2)
print(student)