
numA = [11,22,33]
numB = numA
print(numB)
print(numA)

numB[1]= 222
print(numA)
print(numB)

# copy

numC = [11,22,33,44]
numD  = numC.copy()
print(numC)
print(numD)
numD[0] = 999
print(numC)
print(numD)
