mylist = [1, 2, 3]
mylist.append(4)
# print(mylist)
# print(type(20.0))

class Sample():
    pass

x = Sample()
print(type(x))

class Dog():
    
    def __init__(self, breed):
        self.breed = breed

mydog = Dog(breed="Lab")
otherdog = Dog(breed="Haskie")
print(mydog.breed)