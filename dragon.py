from Animal import Animal

class Dragon(Animal):

    def __init__(self, name, hunger=0, color = "Green"):
        super().__init__( name, hunger)
        self.color = color


    def get_name(self):
        return (self._name)

    def is_hungry(self):
        return (self._hunger > 0)

    def feed(self):
        if self._hunger > 0 :
            self._hunger -= 1

    def talk(self):
        print("Raaaawr")