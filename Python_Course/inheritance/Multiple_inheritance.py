class Employee:

    
    
    # constructure
    def __init__(self, name, type):
        # instance varibale
        self.__name = name
        self.__type = type

    @property
    def type(self):
        return self.__type

    @property
    def name(self):
        return self.__name

class Programmer:
    
    # constructure
    def __init__(self, name, language):
        # instance varibale
        self.__name = name
        self.__language = language

    @property
    def language(self):
        return self.__language


class ProgramerEmployee(Programmer, Employee):    

    # class variable
    _type = "Programer"

    # constructure
    def __init__(self, name, language):
        # instance varibale
        Programmer.__init__(self, name, language)
        Employee.__init__(self, name, self._type)


# instances
emp1 = ProgramerEmployee("Ankit", "Python")
emp2 = ProgramerEmployee("Anmmol", "Java")

print(emp1.name)
print(emp1.language)
print(emp1.type)

print(emp2.name)
print(emp2.language)
print(emp2.type)



# print()