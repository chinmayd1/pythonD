
print('hello'.upper())
print("Hello".lower())
print("hello".capitalize())


# count()
fruit = "banana"
print(fruit.count("a"))

# startswith() , endswith()
name = "amol"
print(name.startswith("a"))
print(name.startswith("aM"))
print(name.endswith("l"))
print(name.endswith("ol"))

# find
skill = "promgramming"
#print(skill.find("o"))
print(skill.find("ming"))

# format
text = "My name is {} and lasName is {}".format("chinmay","deshpande")
text = "My name is {fname} and lasName is {lastname}".format(lastname = "deshpande",fname = "chinmay")
print(text)

fn = "sarika"
ln = "pansare"
text = f"My firstName is {fn} and lastName is {ln}"


# index()

city = "pune"
# 0  1  2  3
# p  u  n  e
#print(city.index("u"))

# checked methods 

print("abc".isalpha())
print("1bc".isalpha())
print("1232".isdecimal()) # isdigit()
print("a".isalnum())
print('2'.isalnum())
print("2q#".isalnum())