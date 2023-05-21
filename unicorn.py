from Animal import Animal
class Unicorn(Animal):

    def __init__(self, name, hunger=0):
        super().__init__( name, hunger)


    def get_name(self):
        return (self._name)

    def is_hungry(self):
        return (self._hunger > 0)

    def feed(self):
        if self._hunger > 0 :
            self._hunger -= 1

    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("I’m not your toy...")