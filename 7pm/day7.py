

# for loop 

# range(startIndex, endIndex,stepSize)
# range(5) # startIndex - 0  endIndex-5 , stepSize -1
# range(1,5) # startIndex - 1  endIndex-5 , stepSize -1
# range(2,20,2) startIndex - 2 endIndex-20 , stepSize -2


# print 0 to 3 
for x in range(4):
    print(x)

# program 2
# print 1 to 3
for x in range(1,4):
    print(x)

# program 3
for x in range(1,6):
    print(x)

# program 4
# table of 2 
for x in range(1,11):
    print(x * 2)

# program 5
# table of 2
# 2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21
for x in range(2,21,2):
    print(x)

# program 6
for x in range(3,31,3):
    print(x)

# program 7 
# print 5 to 1
# reverse - step size should be negative
for x in range(5,0,-1):
    print(x)

# program 8
for x in range(20,1,-2):
    print(x)

# program 9
# table of 5 in reverse 
for x in range(50,4,-5):
    print(x)

# break statement with for loop 

for x in range(1,6):
    print(x) #1 #2 #3
    if x == 3:
        break

for x in range(5,0,-1):
    print(x)# 5 #4 #3
    if x == 3:
        break

for x in range(1,6): #2 #3
    if x == 3:
        break
    print(x)  #1 #2

# continue statement with for loop
# continue on certain condition loop will continue
for x in range(1,6):#2 #3 #4 #5
    if x == 3:
        continue
    print(x) #1 #2 #4 #5
    
# while loop

