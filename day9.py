
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
txt = "python programming"
print(txt.find('pro'))
print("hello".islower())
print("Hello".lower())
print("HELLO".isupper())
print("Hello".isupper())
# isSpace()
print(" ".isspace())
print(". ".isspace())

# istile()
txt3 = "My Name is Chinmay"
print(txt3.istitle())


# join()
info  = ["chinmay","deshpande","7709191441"]
# chinmay-deshpande-7709192441
print("@".join(info))

# chinmay@deshpande@7709191441 ----> ["chinmay","deshpande",7709192441]

txt5 = "hi"
print(txt5.ljust(5,"."))
print(txt5.rjust(5,"."))
txt6 = "h1"
print(txt6.center(6,'.'))


text7 = "chinmay@deshpande@7709191441"
print(text7.split("@"))

txt8 =  " goa "
print(len(txt8))
print(len(txt8.rstrip()))

txt9 =  " goa"
print(len(txt9))
print(len(txt9.lstrip()))

txt9 =  " goa "
print(len(txt9.strip()))

# remove prefix 
txt16 = "unhappy"
q1 = txt16.removeprefix('un')
print(q1)

# remove suffice 
txt17 = "reading.txt"
txt17.removesuffix(".txt")

# replace()
txt18 = "i love dogs"
q2  = txt18.replace("dogs","cats")
print(q2)

# swapcase()
print("chinmay".swapcase())

#title()
info = "i am learning javascript"
print(info.title())

# zfill
txt20 = "42" # 00042
txt21 = "342" #00342
print(txt21.zfill(5))

# partition()
txt22 = "chinmay@deshpande.com"
#("chinmay","@","deshpande.com")
print(txt22.partition("@"))