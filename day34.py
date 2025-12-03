
# operator overloading 

print(1 + 2)
print("hello "+ " world")


# class BookOne:
#     def __init__(self,pages):
#         self.pages = pages 
        
#     def __add__(self,other):
#         return self.pages + other.pages

# class BookTwo:
#     def __init__(self,pages):
#         self.pages = pages
        
# a  = BookOne(12)
# b = BookTwo(13)

# print(a + b)
# #print(a.pages + b.pages)

class BookC:
    def __init__(self,pages):
        self.pages = pages
     
class BookD:
    def __init__(self,pages):
        self.pages = pages
    def __gt__(self,other):
        return self.pages > other.pages
        
       
c =  BookC(12)
d = BookD(6)
#print(c > d)
print(d > c)
#print(c.pages > d.pages)