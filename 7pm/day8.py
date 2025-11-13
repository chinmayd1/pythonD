# intialization 
# while(condition):
    # statement 
    # increment / decrement


# print 1 to 3
i1 = 1
while(i1 <= 3):
    print(i1) # 1 // 2 // 3
    i1 = i1 + 1 #// 2 // 3 // 4

# 1 <= 3 ---> True
# 2 <= 3 ---> True
# 3 <= 3 ---> True
# 4 <= 3 ---> False

# program 2
# print 1 to 5

i2 = 1
while(i2 <= 5):
    print(i2) #1 #2 #3 #4 #5
    i2 = i2 + 1 #2 #3 #4 #5 #6


# program 3
# print hello 3 times
i3 = 1
while(i3 <= 3):
    print("hello") # "hello" #"hello" #"hello"
    i3 = i3 + 1 #2 #3 #4


#program 5
# print 5 to 1
i4 = 5
while(i4 >= 1):
    print(i4) # 5 #4 #3 #2 #1
    i4 = i4 - 1 # 4 #3 #2 #1 #0

#program6
# table of 2
i5 = 1
while(i5 <= 10):
    print(i5*2)
    i5 = i5 + 1

i6 = 2
while(i6 <= 20):
    print(i6)
    i6 = i6 + 2

# table of 5 in reverse 
i7 = 50
while(i7 >= 5):
    print(i7)
    i7 = i7 - 5

# break statement with while loop

i8 = 1
while i8 <= 5:
    print(i8) #1 #2 #3
    if i8 == 3:
        break
    i8 = i8 + 1 #2 #3

i9 = 1
while i9 <= 5:
    if i9 == 3:
        break
    print(i9) #1 #2
    i9 = i9 + 1  #2 #3
