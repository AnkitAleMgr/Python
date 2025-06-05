class Employee:
    def __init__(self, name, age, nationality):
        self.__name = name
        self.__age = age
        self.__nationality = nationality

    def __str__(self):
        return f"Name: {self.__name}\nAge: {self.__age}\nNationality: {self.__nationality}"

    def detail(self, occupation):
        return f"Name: {self.__name}\nAge: {self.__age}\nNationality: {self.__nationality}\nOccupation: {occupation}"

    @property
    def name(self):
        return self.__name

class Driver(Employee):
    def __init__(self, name, age, nationality, occupation):
        super().__init__(name, age, nationality)
        self.__occupation = occupation

    @property
    def occupation(self):
        return self.__occupation

    def drive(self):
        return f"{self.name} is driving"

class Army(Employee):
    def __init__(self, name, age, nationality, occupation):
        super().__init__(name, age, nationality)
        self.__occupation = occupation

    def salute(self):
        return f"{self.name}, salute!"

    @property
    def occupation(self):
        return self.__occupation

# instances
driver1 = Driver("Ankit", 19, "Nepali", "Driver")
army1 = Army("Ankit", 22, "African", "Army")


print(driver1._Driver__occupation) # <-- name mangling but not recommended
print(driver1.occupation)  # <-- retricing through getter is recommended
print(army1) # <-- directly pritn __str__
print(army1.detail(army1.occupation))

print(driver1.drive)
print(army1.salute)