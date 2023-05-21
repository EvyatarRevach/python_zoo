from Animal import Animal

class Cat(Animal):

    def __init__(self, name, hunger=0):
        Animal.__init__(self, name, hunger)


    def get_name(self):
        return (self._name)

    def is_hungry(self):
        return (self._hunger > 0)

    def feed(self):
        if self._hunger > 0 :
            self._hunger -= 1

    def talk(self):
        print("meow	")