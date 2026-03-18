x = 1
print(x)
x = 2
print(x)

def add(a, b):
    return a + b

result = add(3, 4)
print(result)

def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)

print( x < 5 )  # True
print( x > 5 )  # False

f = lambda x: x*2

def f(x):
    return x*2