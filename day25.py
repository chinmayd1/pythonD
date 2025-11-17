

# Generators 
# Decorators 
# generators 
# return is last statement of any function

def get_numbers():
    return 1
    return 2
    return 3
e = get_numbers()
print(e)

def get_numbers2():
    return [1,2,3]
e2 = get_numbers2()
print(e2)

# A generator is a special type of function , which returns more than one value at a 
#time

def get_numbers3():
    yield 1
    yield 2
    yield 3
    yield 4

gen = get_numbers3()
print(gen)

e1 = next(gen)
print(e1)
print(next(gen))
print(next(gen))
print(next(gen))

#print(next(gen))
#until it hits the last yield value

def infinite_generator():
    n = 1
    while True:
        yield n
        n = n + 1

gen2 = infinite_generator()
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))


def get_numbers3():
    yield 1
    yield 2
    yield 3
    yield 4

for x in get_numbers3():
    print(x)

# decorators 

# before functionA  run some statements
# functionA ---->
# after functionA run some statements


# defining the decorator
def my_decorator(func):
    def wrapper():
        print("before function is called!")
        func()
        print("after function is called!")
    return wrapper

# using the decorator
@my_decorator
def say_hello():
    print("hello")
say_hello()


# program 2

def log_sum(func):
    def wrapper(a,b):
        print(f'Adding the numbers :{a}+{b}')
        result = func(a,b)
        print(f'Result {result}')
        return result
    return wrapper

@log_sum
def sum_numbers(a,b):
    return a + b

sum_numbers(12,3)