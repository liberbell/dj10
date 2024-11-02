def my_func(param1="default"):
    """
    This is the docstring
    """
    print("my first python function! {}".format(param1))

my_func("I`m james bond.")

def hello():
    # print("Hello.")
    return "hello"

result = hello()
print(result)

def addNum(num1, num2):
    if type(num1) == type(num2)==type(10):
        return num1 + num2
    else:
        return "Sorry need integers"

result = addNum(10, 20)
print(result)

result = addNum("2", "3")
print(result)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even_bool(num):
    return num%2 == 0

evens = filter(even_bool, my_list)
print(list(evens))