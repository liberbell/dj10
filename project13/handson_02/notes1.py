mylist = [1, 2, 3]
mylist.append(4)
# print(mylist)
# print(type(20.0))

class Sample():
    pass

x = Sample()
# print(type(x))

class Dog():
    spiceis = "mammal"
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

mydog = Dog(breed="Lab", name="Sammy")
# otherdog = Dog(breed="Haskie")
# print(mydog.breed, mydog.name)
# print(mydog.spiceis)
# print(otherdog.breed)

class Circle():
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

myc = Circle(3)
print(myc.area())