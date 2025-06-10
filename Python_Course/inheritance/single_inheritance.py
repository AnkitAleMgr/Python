class Animal:
    """Base class that represent every Animal"""

    # class varibale
    _no_of_animal = 0
    
    # constructor
    def __init__(self, name, color):
        """it declares the argument whhile creating instances"""
        # instance varibale
        self._name = name
        self._color = color
        Animal._no_of_animal += 1

    # method/behaviour
    def bark(self):
        print("Animal is barking...")

    # detail
    def __str__(self):
        return f"Name : {self._name}\nColor : {self._color}"

    @classmethod
    def no_of_animal(cls):
        return cls._no_of_animal

class Cat(Animal):
    """Cat subclass of Animal"""

    # class variable
    _no_of_cat = 0
    
    # class varibale
    __breed = "ocicat"
    
    def __init__(self, name, color, lifespan):
        # instance variable
        super().__init__(name, color)
        self.__life_span = lifespan
        Cat._no_of_cat += 1
        

    # method/ behaviour
    def bark(self):
        # super().bark()
        print(f"{self._name} is meowing..")

    # detail
    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str}\nBreed : {Cat.__breed}\nLife span : {self.__life_span}"

    @classmethod
    def no_of_cat(cls):
        return cls._no_of_cat

# instances
animal1 = Animal("animal1", "white")
cat1 = Cat("cat1", "Black", 10)

print(animal1.__doc__)
animal1.bark()
print(animal1)
print()

print(cat1.__doc__)
cat1.bark()
print(cat1)
print()

print("Total no:")
print(f"Animal: {Animal.no_of_animal()}")
print(f"Cat: {Cat.no_of_cat()}")
