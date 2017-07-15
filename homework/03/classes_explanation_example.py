class Mammal():
    kind = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        return "Hello. My name is {0}".format(self.name)


# my_cat = Mammal('Майор Мурлычкин', 6)

class Canis(Mammal):
    kind = "Canis"
    legs = 4

    def __init__(self, name, age, owner = None):
        super().__init__(name, age)
        self.owner = owner

class HomoSapiens(Mammal):
    kind = "HomoSapiens"
    legs = 2

    def __init__(self, name, age, dog = None):
        super().__init__(name, age)
        self.dog = dog

    def my_dog(self):
        if self.dog:
            return 'My dog\'s name is {0}'.format(self.dog.name)
        return 'I have not a dog'


