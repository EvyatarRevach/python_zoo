from Animal import Animal
import dog
import cat
import skunk
import unicorn
import dragon


# this is the main func
def main():
    new_dog = dog.Dog("Brownie",10)
    new_cat = cat.Cat("Zelda", 3)
    new_skunk = skunk.Skunk("Stinky", 0)
    new_unicron = unicorn.Unicorn("Keith", 7)
    new_dragon = dragon.Dragon("Lizzy", 1450)
    zoo_lst = [new_dog, new_cat, new_skunk, new_unicron, new_dragon]
    new_dog2 = dog.Dog("Doggo", 80)
    zoo_lst.append(new_dog2)
    new_cat2 = cat.Cat("Kitty", 80)
    zoo_lst.append(new_cat2)
    new_skunk2 = skunk.Skunk("Stinky Jr.", 80)
    zoo_lst.append(new_skunk2)
    new_unicron2 = unicorn.Unicorn("Clair", 80)
    zoo_lst.append(new_unicron2)
    new_dragon2 = dragon.Dragon("McFly", 80)
    zoo_lst.append(new_dragon2)
    for animal1 in zoo_lst:
        if animal1.is_hungry() is True:
            print(animal1.__class__.__name__, animal1.get_name())
        while animal1.is_hungry() is True:
            animal1.feed()
        animal1.talk()
    print(Animal.zoo_name)

main()
