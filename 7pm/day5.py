
# conditional statement
# one input and multiple outcome

# numT > 0 and numT <= 5   ------> 10 % discount 
# numT > 5 and numT <= 10  ------> 20 % discount
# numT > 10                ------> 30 % discount

# AND 

# true  and  true  ---> true
# false and  true  ---> false
# true  and  false ---> false
# false and  false ---> false

# if(condition):
#     statement

numT = 17
if(numT > 0 and numT <= 5):
    print("10 % discount")
if(numT > 5 and numT <= 10):
    print("20 % discount")
if (numT > 10):
    print("30 % discount")

# program 2
numT = -17
if numT > 0 and numT <= 5:
    print("10 % discount")
elif numT > 5 and numT <= 10:
    print("20 % discount")
elif numT > 10:
    print("30 % discount")
else:
    print("incorrect input")

# program 3

marks = 92
if marks > 90:
    print("grade A")
if marks >= 75:
    print("grade B")
if marks >= 65:
    print("grade C")


# program 4
marks = 50
if marks > 90:
    print("grade A")
elif marks >= 75:
    print("grade B")
elif marks >= 65:
    print("grade C")
else:
    print("please try again")


# program 5
q1 = 10
q2 = 50
if q1 > q2:
    print("q1 is greater")
else:
    print("q2 is greater")


# program 6

x1 = 10
x2 = 50
x3 = 300

if x1 > x2 and x1 > x3:
    print("x1 is greater")
elif x2 > x1 and x2 > x3:
    print("x2 is greater")
else:
    print("x3 is greater")










