class Animal():


    def __init__(self,name):
        self.name = name 

    def sound(self):
        print(f"This {self.name} make a sound like an animal!!!")


class Dog(Animal):

    def __init__(self,name):
        self.name = name 

    def sound(self):
        print(f"This {self.name} Bark!!!")

class Cat(Animal):

    def __init__(self,name):
        self.name = name 

    def sound(self):
        print(f"This {self.name } meow!!!")



#instance
firstAnimal = Animal("Animal")
firstAnimal.sound()

firstDog = Dog("Puppy")
firstDog.sound()

firstCat = Cat("Kitty")
firstCat.sound()
