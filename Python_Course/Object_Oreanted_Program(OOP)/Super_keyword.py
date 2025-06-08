class ParentClass:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def parent_method(self):
        print("This is from parent class")

class ChildClass(ParentClass):

    def __init__(self, name, age, time):
        super().__init__(name, age)
        self._time = time

    def parent_method(self):
        super().parent_method()

    def child_method(self):
        print("This is from child class")

child = ChildClass("ankit", 19, 1990)
child.child_method()
child.parent_method()