#      0123456789
str = "hello world"
e = str.find("world") # 6
print(e)

city = "pune"

# 0  1  2  3
# p  u  n  e

e2 = city.index("u")
print(e2)

# modify and replace methods 
info = "i am learning javascript"
e3 = info.replace("javascript",'python')
print(e3)


city3 = "goa"
print(len(city3))

city3 = " goa "
print(len(city3))
e5 = city3.strip()
print(len(e5))

city3 = " goa"
e6 = city3.lstrip()
print(len(e6))

city3 = " goa "
e7 = city3.rstrip()
print(len(e7))

# Split and joining

email = "chinmaydeshpande010@gmail.com"
#["chinmaydeshpande010","gmail.com"]
e8 = email.split("@")
print(e8)

name = "chandrapur"
#["ch","ndr","pur"]
e9  = name.split("a")
print(e9)

str = "saad sayyed"
e10 = str.count("a")
print(e10)

# formating methods 

str3 = "hi"
print(str3.center(10,"*"))
print(str3.rjust(5,"*"))  #"***hi"
print(str3.ljust(5,"*"))  # "hi***"
