# program 1
str = "chinmay"
print(str)
print(type(str))

# program 2
strB = 'amol' 
print(strB)
print(type(strB))

# program 3

strC = """
    I am learning javascript and
    I am also learning python 
    python is great
"""
print(strC)


# program 4
# String stores the value by index ?? -- Yes
city = "pune"
#  0  1  2   3
#  p  u  n   e
print(city[0])
print(city[1])
print(city[2])

# program 5
# particular sub string exist in string 
info = "i am learning javascript"
print(info)
print("Javascript" in info)

# program 6
city2 = "nagar"
print(len(city2))

# String are immutable 
# city2[0] = "N"
# print(city2)

# number = [11,22,33]
# number[0] = 111
# print(number)

# city = "pune"
# city[0] = "P"

# program 7
# looping through string 

city3  = "nagpur"
# 0   1   2   3   4   5
# n   a   g   p   u   r
# range()
for x in range(len(city3)):
    #print(x)
    print(city3[x])
    
city4 = "chandrapur"
for x in city4:
    print(x)


city5 = "mumbai"
i1 = 0
while(i1 < len(city5)):
    #print(i1)
    print(city5[i1])
    i1 = i1 + 1
