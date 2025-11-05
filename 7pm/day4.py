
# comparison operator

print(3 > 2)
print(3 > 2)
print(3 >= 2)
print(3 <= 2)
print(3 == 3)
print(3 != 3)
print(2 != 1)
print(2 == 1)
print(2 >= 2)
print(2 <= 2)

# logical operator
# and   or   not 
# True   and   True   ----> True
# False  and   True   ----> False
# True   and   False  ----> False 
# False  and   False  ----> False

print(2 == 2 and 3 == 3)
print(1 == 0 and 2 == 2)
print(2 == 2 and 3 == 1)
print(5 == 3 and 3 == 1)

# or 
# True    or   True  ---> True
# False   or   True  ---> True
# True    or   False --->True
# False   or   False ---> False

print(2 > 1 or 2 == 2)
print(1 > 2 or 3 == 3)
print(2 == 2 or 4 == 3)
print(2 == 1 or 4 == 1)

# conditional statement
# one input and multiple outcomes 
# numT > 0 and numT <= 5  ---> 10 % discount
# numT > 5 and numT <= 10 ---> 20 % discount
# numT > 10               ---> 30 % discount

#if(condition):
    # statement

numT = 17
if numT > 0 and numT <= 5:
    print("10 % discount")
if numT > 5 and numT <= 10:
    print("20 % discount")
if numT > 10:
    print("30 % discount")

# program 2
numT = -2
if numT > 0 and numT <= 5:
    print("10 % discount")
elif numT > 5 and numT <= 10:
    print("20 % discount")
elif numT > 10:
    print("30 % discount")
else:
    print("incorrect input")