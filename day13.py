# setA = {11,22,33}
# setB = {44,55,66,11,22}
# setC = setA.intersection(setB)
# print(setC)
# print(setA)
# print(setB)

# program 2
setA = {11,22,33}
setB = {44,55,66,11,22}

# setA.intersection_update(setB)
# print(setA)
# print(setB)

setB.intersection_update(setA)
print(setA)
print(setB)


# program 2

setD = {22,33,44,77}
setE = {55,66,77,44}

# print(setD.difference(setE))
# print(setE.difference(setD))

# print(setD)
# print(setE)

setD = {22,33,44,77}
setE = {55,66,77,44}

# setD.difference_update(setE)
# print(setD)
# print(setE)

# setE.difference_update(setD)
# print(setE)


# program 3
setG = {44,55,66,99}
setH = {66,77,88,99}

print(setG.symmetric_difference(setH))
print(setG)
print(setH)

setH.symmetric_difference_update(setG)
print(setH)

# program 4
setH = {33,31,55}
setJ = {12,44,77}
print(setH.isdisjoint(setJ))


setA  = {11,22}
setB = {11,22,33,44}
print(setA.issuperset(setB))
print(setB.issuperset(setA))
print(setA.issubset(setB))
print(setA.union(setB))

setA  = {11,22}

setA.discard(22)
print(setA)

# discard() and remove()

# ISTQB 
# ISTQB - AI
