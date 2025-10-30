# x = 10
# print(x)
# x = 300
# print(x)

# # Arithmetic operation 

# a = 10
# b = 5

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)

# s = 8
# t = 4

# print(s+t)
# print(s-t)
# print(s*t)
# print(s/t)
# print(s%t)
# print(23 % 5)

# # CEO ---> Office sham 
# def Calculator(x,y):
#     print(x+y)
#     print(x-y)
#     print(x*y)
#     print(x/y)
#     print(x%y)
# Calculator(12,3)
# Calculator(4,2)

# function without parameter and without return type

def CalA():
    print(9+9)
CalA()
CalA()
CalA()

# function with parameter and without return type 
def CalB(x,y):
    print(x+y)
CalB(12,3)
CalB(4,2)
CalB(2,1)

# function with parameter and with return
# 100 given , 100 show
# 100 + 100 , 100 - 50 , 100 * 0.10 , 100/10
def CalC(x,y):
    return x + y

e = CalC(12,3)
print(e)
print(e + e) 