a = "chinmay"
print(a)
print(type(a))

b = 'shirish'
print(b)
print(type(b))

c = """
    hello i am learning python
    python is go to language for AI
"""

c = '''
    I am learning python and 
    python is go to language for AI
'''

print(type(c))
print(type(c))

# program 2
# string concat
fn = "chinmay"
ln = "deshpande"
# my firstName is chinmay and my lastName is deshpande
print("my firstName is "+fn+" and my lastName is "+ln)
print(f"my firstName is {fn} and my lastName is {ln}")

# program 2
names = ["sarika","poorva","ram"]
print(names[0])
names[0] = "chinmay"
print(names)

# str immutable -  python
fn = "chinmay"
fn = "rahul"
print(fn[0])
#fn[0] = "d"

# program 3
# does string stores the value by index ?

# 0     1     2    3
# p     u     n    e
cities = ["pune","nagpur","wardha"]
print('pune' in cities)
city = "pune"
print(city[2])
# for range
for x in range(4):
    #print(x)
    print(city[x])

# for Each 
for char in city:
    print(char)

# while loop
i1 = 0
while(i1 < len(city)):
    #print(i1)
    print(city[i1])
    i1 = i1 +1 


# substring exist in string - ? yes or no
fruits = "apple  mango banana orange grapes"
print("Mango" in fruits)

# methods in string 

# lower()
s1  = "Pune"
print(s1.lower())

# upper()
s2 = "mumbai"
print(s2.upper())

# capitalize()
s3 = "nagpur"
print(s3.capitalize())




