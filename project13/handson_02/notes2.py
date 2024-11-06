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


mya = Animal()
mya.whoAmI()
mya.eat()

mydog = Dog()
mydog.whoAmI()
mydog.eat()