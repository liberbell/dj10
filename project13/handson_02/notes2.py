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

class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: {}, author: {}, pages: {}".format(self.title, self.author, self.pages6)

b = Book("python", "james", 432)
print(b)

# mylist = [1, 2, 3]
# print(mylist)