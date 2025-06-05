class Students:

    def __init__(self, name, grade):
        self._grade = grade
        self._name = name

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100.")
        else:
            self._grade = grade

student1 = Students("Ankit", 60)
print(student1._grade)
student1.grade = 50
print(student1._grade)