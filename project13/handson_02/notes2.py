class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def whoAmI(self):
        print("ANIMAL")

    def eat(self):
        print("eating")

class Dog(Animal):

    def __init__(self):
        pass


mya = Animal()
mya.whoAmI()
mya.eat()