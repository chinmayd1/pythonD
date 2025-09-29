# x = 10
# print(x)
# x = 9000
# print(x)

# # Arithmetic operation 

# a = 8 
# b = 4

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)


# s = 6
# t = 3

# print(s+t)
# print(s-t)
# print(s*t)
# print(s/t)
# print(s%t)


# # function 
# def Calculator(x,y):
#     print(x+y)
#     print(x-y)
#     print(x*y)
#     print(x/y)
#     print(x%y)

# Calculator(12,3)
# Calculator(6,3)


# # function without parameter and without return type 

# def addA():
#     print(9+9)
# addA()
# addA()
# addA()
    
# # function with parameter and with return type 

# def addB(x,y):
#     print(x+y)
# addB(12,3)
# addB(12,2)
# addB(12,1)

# # function with parameter and with return 

# def addC(x,y):
#     return x + y
# e = addC(12,3)
# print(e)
# print(e + e)
# print(e * 0.10)



# types 

a = 10
print(a)
print(type(a))
# 10 , -10 , 0

b = 5.5
print(b)
print(type(b))
# 10.5 , -10.55 ,0.45

c = True
print(c)
print(type(c))
# True or False

d = "chinmay"
print(d)
print(type(d))
# "chinm","3,"4324" , "234",'@#$',"234"

# comparison 
# entity < entity ==> boolean --- true or false
# < , > , <= , >= , == ,!=
print(2 > 1)
print(2 < 1)
print(2 >= 1)
print(2 <= 1)
print(2 == 2)
print(2 != 2)
print(2 == 3)
print(2 >= 2)
print(2 <= 2)

# logical operator
# and 

# True  and   True   ----> True
# False and   True   ----> False
# True  and   False  ----> False
# False and   False  ----> False

print(2 == 2  and 3 == 3)
print(2 != 2  and 3 == 3)
print(2 == 2  and 3 != 3)
print(2 != 2  and 3 != 3)


# or 
# True  or  True   ----> True
# False or   True   ----> True
# True  or  False  ----> True
# False or   False  ----> False


print(2 == 2  or 3 == 3)
print(2 != 2  or 3 == 3)
print(2 == 2  or 3 != 3)
print(2 != 2  or 3 != 3)


# not
# not True  ---> False
# not False ---> True
print(not (3 == 3))
print(not 4 == 5)



# conditional statement 
# one input and multiple outcomes 

numT = -17

# if numT > 0 and numT <= 5:
#     print('5% discount')
# if numT > 5 and numT <= 10:
#     print("10 % discount")
# if numT > 10:
#     print("20 % discount")

# if numT > 0 and numT <= 5:
#     print('5% discount')
# elif numT > 5 and numT <= 10:
#     print("10 % discount")
# elif numT > 10:
#     print("20 % discount")
# else:
#     print('incorrect input !')

# program 2

marks = 92

# if marks > 90:
#     print("grade A")
# if marks >= 75:
#     print("grade B")
# if marks >= 65:
#     print("grade C")



if marks > 90:
    print("grade A")
elif marks >= 75:
    print("grade B")
elif marks >= 65:
    print("grade C")
else:
    print("please try ...")

d = 8
e = 4

if d > e:
    print("d is greater")
else:
    print('e is greater')


x1 = 10
x2 = 50
x3 = 300

if x1 > x2 and x1 > x3 :
    print("x1 is greater")
elif x2 > x1 and x2 > x3:
    print('x2 is greater')
else:
    print("x3 is greater")


# ternary operator
#statement 1 if condition else statement


e = 90
f = 500
print("e id greater") if e > f else print("f is greater")

age = 18
e = "can drive" if age >= 18 else "cannot drive"
print(e)


# 8.00 pm js 
# 9.00 pm python (loops)
# 8:30 pm sql


















