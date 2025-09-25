
# intialization
# while(condition):
 # statement 
 # increment / decrement 


# program 1
# print 1 to 3
i1 = 1
while(i1 <= 3):
    print(i1) #1 #2 #3
    i1 = i1 + 1 #2 #3 #4

# print 1 to 5
i2 =1
while(i2 <= 5):
    print(i2) #1 #2 #3 #4 #5
    i2 = i2 + 1 #2 #3 #4 #5 #6

# print hello 3 times
i3 = 1
while(i3 <= 3):
    print("hello") # hello # hello # hello
    i3 = i3 + 1 # 2 #3 #4

# print 5 to 1
i4 = 5
while(i4 >= 1):
    print(i4) #5 #4 #3 #2 #1
    i4 = i4 - 1 #4 #3 #2 #1 #0

# table of 2 
i5 = 1
while(i5 <= 10):
    print(i5 * 2) #1-------------> 10
    i5 = i5 + 1 #2 ---------------> 11

i6 = 2
while(i6 <= 20):
    print(i6) #2 #4 #6 ------> 20
    i6 = i6 + 2 #4 #6 #8 -------> 22

# table of 3 in reverse 
i7 = 30
while (i7 >= 3):
    print(i7)
    i7 = i7 - 3

# table of 5 in reverse
i8 = 50
while (i8 >= 5):
    print(i8)
    i8 = i8 - 5

# break statement with for loop

q = 1
while(q <= 5):
    print(q) #1 #2 #3
    if(q == 3):
        break
    q = q + 1 #2 #3

q = 1
while(q <= 5):
    if(q == 3):
        break
    print(q)  #1 #2
    q = q + 1  #2 #3

# continue with while loop 

x = 1
while(x <= 5):
    if x == 3:
        x = x + 1 #4
        continue
    print(x) #1  #2 #4 #5
    x = x+ 1 #2 #3 #5 #6