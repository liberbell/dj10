# x = 25

def my_func():
    x = 50
    return x

# print(x)
# print(my_func())
# my_func()
# print(x)

# lambda x: x ** 2
name = "This is a global name"

def greet():
    # name = "summy"

    def hello():
        print("Hello " + name)

    hello()

# greet()

x = 50
def func():
    global x

    print("x is ", x)
    
    x = 1000

    print("local x is change to ", x)

print("before func call, x is ", x)
func()
print("after func call, x is ", x)