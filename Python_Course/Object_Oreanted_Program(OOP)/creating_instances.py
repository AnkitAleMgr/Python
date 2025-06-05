class Person:
    # making constructure for instance
    def __init__(self , name , age, occupation, color):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.color = color

    # action/ methond
    def speak(self):
        print(f"Hello, My name is {self.name}. I am {self.age} years old. I am {self.occupation} and my color is {self.color}.")

# instance 1 crated
person1 = Person("Ankit", 19 , "student", "brown")
person1.speak()

# instance 2 created
person2 = Person("Anmol", 17 , "student", "brown")
person2.speak()
