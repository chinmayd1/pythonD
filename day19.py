
# conditional statement


# one input and multiple outcomes 
# numT > 0 and numT <= 5   ---> 10 % discount 
# numT > 5 and numT <= 10  ---> 20 % discount
# numT > 10                ---> 30 % discount

# if condition:
#     statement

# program 1
numT = 17
if numT > 0 and numT <= 5:
    print("10 % discount")
if numT > 5 and numT <= 10:
    print("20 % discount")
if numT > 10:
    print("30 % discount")

# program 2
numT = -11
if numT > 0 and numT <= 5:
    print("10 % discount")
elif numT > 5 and numT <= 10:
    print("20 % discount")
elif numT > 10:
    print("30 % discount")
else:
    print("please try again ...")

# program 3
marks = 55
# if marks > 90:
#     print("Grade A")
# if marks >= 75:
#     print("Grade B")
# if marks >= 65:
#     print("Grade C")

if marks > 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 65:
    print("Grade C")
else:
    print("please try again ...")

# program 6
x = 10
y = 50
if x > y:
    print("x is greater")
else:
    print("y is greater")


# program 7

q1 = 8
q2 = 40
q3 = 200

if q1 > q2 and q1 > q3:
    print("q1 is greater")
elif q2 > q3 and q2 > q1:
    print("q2 is greater")
else:
    print("q3 is gretaer")

