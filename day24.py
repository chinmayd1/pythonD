from functools import reduce

employees = [
    {"id": 1, "name": "John",   "age": 28, "salary": 45000, "department": "IT"},
    {"id": 2, "name": "Alice",  "age": 34, "salary": 72000, "department": "HR"},
    {"id": 3, "name": "Bob",    "age": 25, "salary": 38000, "department": "IT"},
    {"id": 4, "name": "David",  "age": 42, "salary": 96000, "department": "Finance"},
    {"id": 5, "name": "Sara",   "age": 30, "salary": 55000, "department": "HR"}
]

# extract firstName of all employeed
print(list(map(lambda emp:emp['name'],employees)))
# increase salary of every employee by 10 %
print(list(map(lambda emp:emp["salary"]*1.10,employees)))
print(list(map(lambda emp:{**emp,"salary":emp["salary"]*1.10},employees)))
#explaination
#dictA ={"id": 1, "name": "John",   "age": 28, "salary": 45000, "department": "IT"}
# **kwargs
#**emp,salary:emp["salary"]*1.10

# Employe where salary greater then 50 

print("-------------------------------------------------")
above50 = list(filter(lambda emp:emp['salary']>50000,employees))
print(list(map(lambda emp:emp['name'],above50)))


# employee of IT department

print("-------------------------------------------------")
itdepartment = list(filter(lambda emp:emp['department'] == "IT",employees))
print(list(map(lambda emp:emp['name'],itdepartment)))


# total salary of all employees


# find the employee with highest


# name of employee age > 30


# count of employee in HR department

