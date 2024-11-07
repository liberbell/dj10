class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def whoAmI(self):
        print("ANIMAL")

    def eat(self):
        print("eating")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog CREATED")

    def bark(self):
        print("WOOF")

    def eat(self):
        print("Dog eating")


# mya = Animal()
# mya.whoAmI()
# mya.eat()

# mydog = Dog()
# mydog.whoAmI()
# mydog.eat()
# mydog.bark()

def book():

    def __init__(self, title, author, pages):
        self.title = title

mylist = [1, 2, 3]
print(mylist)