
# methods str

firstName = "chinmay"
strA = firstName.upper()
print(strA)

lastName = "Deshpande"
strB = lastName.lower()
print(strB)

city ="pune"
strC = city.capitalize()
print(strC)


# program 2
# My firstName is "chinmay" and lastName name is "deshpande"

firstName = "chinmay"
lastName = "deshpande"

print("My firstName is "+firstName + "my lastName is "+lastName)
# latest
print(f"My firstName is {firstName} and my lastName is {lastName}")
print("My firstName is {} and my lastName is {}".format(firstName,lastName))

# program 3 
# checked methods 

firstName = "Chinmay"
e2 = firstName.islower()
print(e2)

lastName = "DESHPANDE"
e3 = lastName.isupper()
print(e3)

# istile()
info = "I Am Learning javascript"
e4  = info.istitle()
print(e4)

# startswith()
info2 = "chinmay"
e = info2.startswith("c")
print(e)

# endswith()
info3 = "saad"
e2 = info3.endswith("ad")
e3 = info3.endswith("Ad")
print(e2)
print(e3)


info4 = "chinmay"
e5 = info4.isalpha()
print(e5)

info4 = "32139123921930A"
e6 = info4.isdigit()
print(e6)

# numbers , alpha , both
info5 = "312312%"
print(info5.isalnum())
print(info5.isalnum())

#isSpace()
info6 = " A"
print(info6.isspace())
