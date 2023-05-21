from Animal import Animal

class Skunk(Animal):

    def __init__(self, name, hunger=0, stink_count=6):
        super().__init__( name, hunger)
        self.stink_count = stink_count


    def get_name(self):
        return (self._name)

    def is_hungry(self):
        return (self._hunger > 0)

    def feed(self):
        if self._hunger > 0 :
            self._hunger -= 1

    def talk(self):
        print("tsssss")